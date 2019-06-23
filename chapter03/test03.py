# _*_coding  ： UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/23 11:10
# 文件名称    ： test03.PY
# 开发工具    ： PyCharm
import datetime

print("当前年份：" + str(datetime.datetime.now().year))

print("当前日期时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))