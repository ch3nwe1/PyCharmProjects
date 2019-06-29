# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 12:18
# 文件名称    ： test08.PY
# 开发工具    ： PyCharm

template = '编号：%09d\t公司名称：%s \t官网：http://www.%s.com'
context1 = (7, '百度', 'baidu')
context2 = (8, '明日学院', 'mingrisoft')
print(template%context1)
print(template%context2)
