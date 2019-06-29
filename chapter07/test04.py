# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 11:35
# 文件名称    ： test04.PY
# 开发工具    ： PyCharm
str1 = '明 日 学 院 官 网 >>> www.mingrisoft.com'
print('源字符串：', str1)
list1 = str1.split()
list2 = str1.split('>>>')
list3 = str1.split('.')
list4 = str1.split(' ', 4)
print(str(list1) + '\n' + str(list2) + '\n' + str(list3) + '\n' + str(list4) + '\n')
list5 = str1.split('>')
print(list5)

