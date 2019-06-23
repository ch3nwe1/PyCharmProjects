# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/23 19:02
# 文件名称    ： test08.py.PY
# 开发工具    ： PyCharm

player = ["莫德里奇", "梅西", "C罗", "苏亚雷斯", "内马尔", "格列兹曼", "莫德里奇"]
num = player.count("莫德里奇")
print(num)

team = ["西班牙", "阿根廷", "葡萄牙", "德国", "法国", "瑞典", "克罗地亚"]
position = team.index("阿根廷")
print(position)

grade = [98, 99, 97, 100, 100, 96, 94, 89, 95, 100]
total = sum(grade)
print("Python理论总成绩为：", total)

print("原列表：", grade)
grade.sort()
print("升 序：", grade)
grade.sort(reverse=True)
print("降 序：", grade)

char = ["cat", "Tom", "Angela", "pet"]
char.sort()
print("区分字母大小写:", char)
char.sort(key=str.lower)
print("不区分字母大小写:", char)

grade = [98, 99, 97, 100, 100, 96, 94, 89, 95, 100]
grade_as = sorted(grade)
print("升序：", grade_as)
grade_des = sorted(grade, reverse=True)
print("降序：", grade_des)
print("原序列：", grade)

price = [1200, 5330, 2988, 6200, 1998, 8888]
sale = [int(x * 0.5) for x in price]
print("原价:", price)
print("打五折的价格：", sale)

sale = [x for x in price if x > 5000]
print("价格高于5000的", sale)
