# -*- coding:utf-8 -*-

import os
import sys
import time
import pythoncom
import pyHook
import base64

handle = open(r'E:\software\keyboard_keeper_log\test\mouse.txt', 'a')
# key_handle = open(r'E:\software\keyboard_keeper_log\keyboard.txt', 'a')


# print "MessageName:", event.MessageName
# print "Message:", event.Message
# print "Time:", event.Time
# print "Window:", event.Window
# print "WindowName:", event.WindowName
# print "Ascii:", event.Ascii, chr(event.Ascii)
# print "Key:", event.Key
# print "KeyID:", event.KeyID
# print "ScanCode:", event.ScanCode
# print "Extended:", event.Extended
# print "Injected:", event.Injected
# print "Alt", event.Altprint "Transition", event.Transition


class KeyType(object):
    """
    按键类
    """

    def __init__(self, message_name, message, time, window, window_name, ascii_code, ascii_chr, key, key_id, scan_code,
                 extended, injected):
        self.message_name = message_name
        self.message = message
        self.time = time
        self.window = window
        self.window_name = window_name
        self.ascii_code = ascii_code
        self.ascii_chr = ascii_chr
        self.key = key
        self.key_id = key_id
        self.scan_code = scan_code
        self.extended = extended
        self.injected = injected

        # 特殊键处理
        if key == 'Escape':
            self.ascii_chr = '<ESC>'
        else:
            pass


# 记录栈,只执行append,pop,从头遍历,清空 操作
key_stack = []


def write_log(log_txt):
    cur_month = time.strftime('%Y_%m')
    log_file = r'E:\software\keyboard_keeper_log\test\{0}_keyboard.txt'.format(cur_month)
    file_handle = open(log_file, 'a')
    file_handle.write(log_txt)
    file_handle.flush()
    file_handle.close()


def on_mouse_event(event):
    # 监听鼠标事件
    # print "MessageName:", event.MessageName
    # print "Message:", event.Message
    # print "Time:", event.Time
    # print "Window:", event.Window
    # print "WindowName:", event.WindowName
    # print "Position:", event.Position
    # print "Wheel:", event.Wheel
    # print "Injected:", event.Injected
    # print"---"
    # write_str = str(event.MessageName) + '|' + str(event.Message) + '|' + str(event.Time) + '|' + str(event.Window) + \
    #             '|' + str(event.WindowName) + '|' + str(event.Position) + '|' + str(event.Wheel) + '|' + str(
    #         event.Injected) + '\n'
    # handle.write(write_str)
    # handle.flush()

    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True


def on_keyboard_event(event):
    # 监听键盘事件
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Time:", event.Time
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Ascii:", event.Ascii, chr(event.Ascii)
    print "Key:", event.Key
    print "KeyID:", event.KeyID
    print "ScanCode:", event.ScanCode
    print "Extended:", event.Extended
    print "Injected:", event.Injected
    print "Alt", event.Alt
    print "Transition", event.Transition
    print "---"
    # 同鼠标事件监听函数的返回值
    global key_stack
    if event.Key == 'Back':
        if len(key_stack) != 0:
            key_stack.pop()
        else:
            pass
    # if event.key == 'Escape':
    #     key_stack
    elif event.Key != 'Return':
        key_stack.append(
                KeyType(event.MessageName, event.Message, event.Time, event.Window, event.WindowName, event.Ascii,
                        chr(event.Ascii), event.Key, event.KeyID, event.ScanCode, event.Extended, event.Injected))
    else:
        # print '#' * 120
        # write_line = []
        write_line = process_special_char(key_stack)
        # for key in key_stack:
        #     # 过滤掉Ctrl Alt Shift 键
        #     if key.ascii_code != 0:
        #         write_line.append(key.ascii_chr)

        if len(write_line) > 0:
            cur_time = time.strftime('%Y-%m-%d %H:%M:%S')
            cur_window = key_stack[-1].window_name
            write_str = cur_time + '|' + cur_window + '---------->' + ''.join(write_line)
            # 过滤掉敏感信息,排除keepass窗口
            if '.kdbx' not in cur_window:
                write_str = base64.encodestring(write_str)
                write_log(write_str + '\n')
            else:
                pass

        key_stack = []

    return True

def process_special_char(r_key_stack):
    str_lst = []
    stack_len = len(r_key_stack)
    for j, item in enumerate(r_key_stack):
        if item.key in ('Lcontrol', 'Rcontrol') and j < stack_len - 2\
                and r_key_stack[j + 1].key not in ('Lcontrol', 'Rcontrol'):
            tmp_str = '<Ctrl-{0}>'.format(r_key_stack[j + 1].key)
            str_lst.append(tmp_str)
        elif item.key in ('Lshift', 'Rshift') and j < stack_len - 2\
                and r_key_stack[j + 1].key not in ('Lshift', 'Rshift'):
            tmp_str = '<Shift-{0}>'.format(r_key_stack[j + 1].key)
            str_lst.append(tmp_str)
        else:
            str_lst.append(item.ascii_chr)

    return str_lst


def main():
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = on_keyboard_event
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 监听所有鼠标事件
    hm.MouseAll = on_mouse_event
    # 设置鼠标“钩子”
    hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
    handle.close()
    # key_handle.close()
