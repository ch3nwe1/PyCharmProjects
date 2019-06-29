# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 17:58
# 文件名称    ： test14.PY
# 开发工具    ： PyCharm
import re
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1 = '127.0.0.1 192.168.1.66'
match = re.findall(pattern, str1)
# print(match)

for item in match:
    print(item[0])
