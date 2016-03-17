# -*- coding:utf-8 -*-

# redis in action 第一章 文章排名示例

import redis
from const_vars import *
import time


def post_article(conn, user, title, link):
    """
    发布文章
    :param conn: redis 连接
    :param user: 文章创建者
    :param title: 文章标题
    :param link: 文章链接
    :return: 返回文章id
    """
    article_id = str(conn.incr('article:'))

    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)

    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
    })

    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)

    return article_id


def article_vote(conn, user, article):
    """
    实现文章的投票功能
    :param conn: redis connection
    :param user: article user
    :param article:
    :return:
    """
    cutoff = time.time() - ONE_WEEK_IN_SECONDS

    if conn.zscore('time:', article) < cutoff:
        return

    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)


def get_articles(conn, page, oder='score:'):
    """
    文章获取功能
    :param conn:  redis connection
    :param page:
    :param oder:
    :return:
    """
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE - 1

    # 获取多个文章id
    ids = conn.zrevrange(oder, start, end)
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)
        article_data['id'] = id
        articles.append(article_data)

    return articles


def add_remove_groups(conn, article_id, to_add=[], to_remove=[]):
    """
    将文章添加到群组里面,以及从群组里面移除
    :param conn:
    :param article_id:
    :param to_add:
    :param to_remove:
    :return:
    """
    article = 'article:' + article_id
    for group in to_add:
        conn.sadd('group:' + group, article)

    for group in to_remove:
        conn.srem('group:' + group, article)


def get_group_articles(conn, group, page, oder='score:'):
    """
    从群组里获取一整页文章
    :param conn:
    :param group:
    :param page:
    :param oder:
    :return:
    """
    key = oder + group
    if not conn.exists(key):
        conn.zinterstore(key,
                         ['group:' + group, oder],
                         aggregate='max')
        conn.expire(key, 60)

    return get_articles(conn, page, key)
