# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 17:33
# 文件名称    ： test11.PY
# 开发工具    ： PyCharm
import re
from builtins import print

pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern, string, re.I)
print('匹配值的起始位置：', match.start())
print('匹配值的结束位置：', match.end())
print('匹配位置的元组：', match.span())
print('要匹配的字符串：', match.string)
print('匹配数据：', match.group())
