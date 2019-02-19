# if
'''
if中的判断 等于：== 不等于：!=,当需要判断多个条件的时候可以使用 and 此参数只要条件中一个结果为False那么结果就是False
也可以使用 or 此参数只要条件中一个为True 结果就会为True，不会在去判断下面的条件，全部条件为Fales，才为False
if中判断是否包含：使用 in ,不包含：使用 not in
'''
name1 = ["mac", "leven", "book"]
for i in name1:
    if i == "mac":
        print(i.upper())
    else:
        print(i.title())
print("-------------------------------------------------")

# if组合判断
index = input("请输入你的年龄：")
if int(index) <= 4:
    print("免费")
elif int(index) < 18:
    print("半价")
else:
    print("全票")
print("-------------------------------------------------")

# if语句里面如果将列表名&元组名用在条件表达试里面，那么python会先判断这个列表或元组是否为空，为空False，不为空True，因此下面的结果为2
name2 = ()
if name2:
    print("1")
else:
    print("2")
print("-------------------------------------------------")


name3 = ["admin", "root", "cat"]
for st in name3:
    if st in name3 and st in "admin":
        print(st + "Hello Word*")
    else:
        print(st + "login")




