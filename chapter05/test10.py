# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 10:13
# 文件名称    ： test10.PY
# 开发工具    ： PyCharm

number = (i for i in range(4))
for i in number:
    print(i, end=" ")
print(tuple(number))
