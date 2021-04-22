"""
#抽取想要的内容
"""

import re

listA = []
num = 0
for i in open('test01.txt'):
    mm = re.findall("^第", i)
    if len(mm) > 0:
        print(i, mm)
