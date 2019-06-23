# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/23 17:47
# 文件名称    ： test06.PY
# 开发工具    ： PyCharm

print("2018俄罗斯世界杯四强：")
team = ["法国", "比利时", "英格兰", "克罗地亚"]
for item in team:
    print(item)

for index, item in enumerate(team):
    print((index + 1), item)
