# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 18:05
# 文件名称    ： test15.PY
# 开发工具    ： PyCharm
import re
pattern = r'1[34578]\d{9}'
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern, '1XXXXXXXXXXX', string)
print(result)
