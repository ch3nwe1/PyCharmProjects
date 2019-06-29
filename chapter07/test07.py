# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 12:06
# 文件名称    ： test07.PY
# 开发工具    ： PyCharm
str1 = ' http://www.mingtisoft.com   \t\n\r'
print('源字符串:', str1 + '。 ')
print('字符串：' + str1.strip() + '。')
str2 = '@明日科技.@.'
print('源字符串str2:' + str2 + '。')
print("字符串：" + str2.strip('@.') + '。')
