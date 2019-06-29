# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 17:46
# 文件名称    ： test12.PY
# 开发工具    ： PyCharm
import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.search(pattern, string, re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern, string, re.I)
print(match)
