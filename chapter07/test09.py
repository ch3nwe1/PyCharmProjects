# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 16:56
# 文件名称    ： test09.PY
# 开发工具    ： PyCharm
template = '编号：{:0>9s}\t公司名称：{:s} \t官网：http://www.{:s}.com'
context1 = template.format('7', '百度', 'baidu')
context2 = template.format('8', '明日科技', 'mingrisoft')
print(context1)
print(context2)
