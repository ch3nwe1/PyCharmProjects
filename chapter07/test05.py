# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/29 11:44
# 文件名称    ： test05.PY
# 开发工具    ： PyCharm

str1 = '@明日科技 @扎克伯格 @雷军'
print(str1.count('@'))

print(str1.find('@', 2))
print(str1.rfind('@'))

print(str1.index('@'))
# print(str1.index('#'))  ValueError: substring not find

print(str1.startswith('@'))

print(str1.endswith('@'))
