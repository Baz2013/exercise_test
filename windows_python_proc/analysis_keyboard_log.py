# -*- coding:utf-8 -*-

import base64
import time
import os
import os.path
import datetime

day_dict = {}


class Day(object):
    """
        docs
    """

    def __init__(self, r_day, r_max="00:00:01", r_min="23:59:59"):
        self.day = r_day
        self.max_time = r_max
        self.min_time = r_min

    def get_second(self, time_string):
        d = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        time_sec_float = time.mktime(d.timetuple())
        return int(time_sec_float)

    def update(self, r_time):
        cur_daytime = self.day + ' ' + r_time
        cur_sec = self.get_second(cur_daytime)
        max_sec = self.get_second(self.day + ' ' + self.max_time)
        min_sec = self.get_second(self.day + ' ' + self.min_time)

        if cur_sec < min_sec:
            self.min_time = r_time
        else:
            pass

        if cur_sec > max_sec:
            self.max_time = r_time
        else:
            pass

        return


def process_record(r_datetime):
    """
    :param r_datetime:  like "2016-03-07 21:24:24"
    :return:
    """
    day = r_datetime.split(' ')[0]
    time = r_datetime.split(' ')[1]

    if day_dict.has_key(day):
        d_value = day_dict.get(day)
        d_value.update(time)
        day_dict[day] = d_value
    else:
        log_day = Day(day)
        log_day.update(time)
        day_dict[day] = log_day


log_file = r'E:\output.txt'

with open(log_file) as handle:
    lines = handle.readlines()

lst = []
for line in lines:
    line = line.strip('\n')
    if len(line) == 0:
        decode_txt = base64.decodestring(''.join(lst))  # .decode('gbk')
        v_time = decode_txt.split('|', 1)
        process_record(v_time[0])
        # print v_time[0]
        # f_handle.write(decode_txt + '\n')
        lst = []
    else:
        lst.append(line)


def get_seconds(time_string):
    d = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(d.timetuple()))


daytime_elements = day_dict.items()
for daytime in daytime_elements:
    # print daytime[0],daytime[1].min_time,daytime[1].max_time
    day, min_time, max_time = daytime[0], daytime[1].min_time, daytime[1].max_time
    hours = ((get_seconds(day + ' ' + max_time) - get_seconds(day + ' ' + min_time))/1800)/2.0
    print day,hours
