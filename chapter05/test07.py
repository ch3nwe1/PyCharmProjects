# _*_ coding:UTF-8 _*_
# 开发人员    ： Administrator
# 开发时间    ： 2019/6/23 18:31
# 文件名称    ： test07.PY
# 开发工具    ： PyCharm

phone = ["摩托罗拉", "诺基亚", "三星", "OPPO"]
print(len(phone))
phone.append("iPhone")
print(len(phone))
print(phone)

verse = ["德国队小组赛回家", "西班牙传控打法还有未来吗", "C罗一人对抗西班牙队"]
print(verse)
verse[2] = "梅西、C罗相约回家"
print(verse)

del verse[-1]
print(verse)

verse.remove("西班牙传控打法还有未来吗")
print(verse)
