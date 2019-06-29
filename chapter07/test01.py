# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 10:28
# 文件名称    ： test01.PY
# 开发工具    ： PyCharm
str1 = '我今天一共走了'
num = 12098
str2 = '步'
# print(str1 + num + str2) 字符不能与数字直接拼接
print(str1 + str(num) + str2)
