# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 18:09
# 文件名称    ： test16.PY
# 开发工具    ： PyCharm
import re
pattern = r'[?|&]'
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern, url)
print(result)
