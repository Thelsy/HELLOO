# 字符串
# title() 将首字母小写转大写
name = "hello word"
print(name.title())
print("--------------------------------------------------------------------------------")
# upper() 将字母全部转成大写
name1 = "Hello Word Django"
print(name1.upper())
print("--------------------------------------------------------------------------------")
# lower() 将字母全部转成小写
name2 = "HELLO WORD DJANGO"
print(name2.lower())
print("--------------------------------------------------------------------------------")
# 拼接字符串
name3 = "Hello Word"
name4 = "Django"
print(name3+" "+name4)
# 制表符 \n=换行 \t=空格
print("--------------------------------------------------------------------------------")
# rstrip() 删除右侧空白字符
name5 = "python       "
print(name5.rstrip())
print("--------------------------------------------------------------------------------")
# lstrip() 删除左侧空白字符
name6 = "       python"
print(name6.lstrip())
print("--------------------------------------------------------------------------------")
# strip() 删除左右2侧空白字符，值得注意的是这样的情况是不会删除空白字符的 " py  thon "
name7 = "   python  "
print(name7.strip())
