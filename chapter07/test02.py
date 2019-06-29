# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 10:34
# 文件名称    ： test02.PY
# 开发工具    ： PyCharm
str1 = "人生苦短，我用Python!"
length = len(str1)
print(length)  # 14

length = len(str1.encode())
print(length)  # 28

length = len(str1.encode('gbk'))
print(length)  # 21
