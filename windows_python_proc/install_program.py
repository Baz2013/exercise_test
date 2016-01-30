# -*- coding:utf-8 -*-

import os
import sys

print sys.path
env = os.environ

for k, v in env.items():
    print '%s---------->%s' % (k, v)
