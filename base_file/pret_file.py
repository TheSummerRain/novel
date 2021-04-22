"""
预处理文件，对文件内容进行排重。
"""

list01 = []
key = 0
for i in open('yushouzhai.txt'):
   # 测试前1000行内容是否排重
    # if key >= 1000:
    #     break
    # else:
    #     key = key + 1

    if i in list01:
        continue
    print(i)
    list01.append(i)
with open('test01.txt', 'w') as handle:
    handle.writelines(list01)
