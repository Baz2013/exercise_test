# -*- coding:utf-8 -*-

import redis
from article_range import *

if __name__ == '__main__':
    redis_conn = redis.Redis(host='123.57.14.82', port=7001, db=0)

    # #test article post
    # article_user = 'gucb1'
    # article_title = 'break news of China'
    # article_link = 'www.gucb.com/break_news.html'
    #
    # id = post_article(redis_conn,article_user,article_title,article_link)
    # print 'artile:',id

    # test vote function
    article_vote(redis_conn, 'yiing', 'article:1')
    article_vote(redis_conn, 'wang', 'article:1')

    # test get articles from redis
    article_lst = get_articles(redis_conn,1)
    print article_lst

    # add and remove groups
    add_remove_groups(redis_conn,'1',to_add=['break_news','america_news'])
    add_remove_groups(redis_conn,'2',to_add=['break_news'])

    group_article_lst = get_group_articles(redis_conn,'america_news',1)
    print group_article_lst
