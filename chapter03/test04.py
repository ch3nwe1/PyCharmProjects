# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/23 14:54
# 文件名称    ： test04.PY
# 开发工具    ： PyCharm

height = float(input("请输入您的身高："))
weight = float(input("请输入您的体重："))
bmi = weight / (height * weight)

# 判断身材是否合理
if bmi < 18.5:
    print("您的BMI指数为：" + str(bmi))
    print("体重过轻")
if 18.5 <= bmi < 24.9:
    print("您的BMI指数为：" + str(bmi))
    print("正常范围，注意保持")
if 24.9 <= bmi < 29.9:
    print("您的BMI指数为：" + str(bmi))
    print("体重过重")
if bmi >= 29.9:
    print("您的BMI指数为：" + str(bmi))
    print("肥胖")
