# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 10:06
# 文件名称    ： test09.PY
# 开发工具    ： PyCharm
import random
randomnumber = (random.randint(10, 100) for i in range(10))
print("生成的元组为：", randomnumber)
randomnumber = tuple(randomnumber)
print("生成的元组为：", randomnumber)

number = (i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number = tuple(number)
print("转换后：", number)
