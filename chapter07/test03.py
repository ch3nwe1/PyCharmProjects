# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 10:40
# 文件名称    ： test03.PY
# 开发工具    ： PyCharm
str1 = '人生苦短，我用Python!'
substr1 = str1[1]
substr2 = str1[5:]
substr3 = str1[:5]
substr4 = str1[2:5]
print('源字符串 ', str1)
print(substr1 + '\n' + substr2 + '\n' + substr3 + '\n' + substr4)

try:
    substr5 = str1[15]
except IndexError:
    print('指定索引不存在')
