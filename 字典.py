# 字典以键值对的方式存在，以{}来表示,其中键唯一不允许重复，值可以重复
name1 = {"color": "green", "color1": "red"}
print(name1["color"])
print("-------------------------------------------------------------------------------------")
# 添加字典注意python向相字典中添加元素时，不关心字典元素中的排列顺序，只关心元素键值对的关联关系
name2 = {"id": 1, "userame": "yu" , "password": 123456}
print(name2)
print("-------------------------------------------------------------------------------------")
name2["bed"] = "1996-10-05"
print(name2)
print("-------------------------------------------------------------------------------------")
# 修改字典中的元素，值得注意的是可以使用键获取值来进行修改值，但是不能通过值获取键，来修改键，键唯一，不可直接修改
name3 = {"color": "green"}
print(name3)
print("-------------------------------------------------------------------------------------")
name3["color"] = "red"
print(name3)
# 删除元素 删除时需要指定需要删除的字典名称&字典键
name4 = {"id": "1", "name": "yu"}
print(name4)
print("-------------------------------------------------------------------------------------")
del name4["id"]
print(name4)
print("-------------------------------------------------------------------------------------")
#
name5 ={"name": "小明",
        "age": "25",
        "city": "杭州"}
print(name5)
# 字典遍历 值得注意的是for循环定义的参数是相互呼应的，其中key代表获取字典中所有的键值，value获取所有的值，这2个参数名称是可以随意起的，但是要遵守命名规范
# 字典遍历之遍历键 for key in name6.keys():，通过此方法可以获取到字典中所有的键
# 字典遍历之获取值 for value in name6.values(): 通过此方法可以获取到字典中的值，而不含键，由于字典中的值是可以重复的，当需要进行去重时，可以使用set()来获取不重复的值元素
name6 ={"id": "1",
        "name": "python",
        "user": "lsy"}
print(name6)
print("-------------------------------------------------------------------------------------")
for key,value in name6.items():
    print("\n键值为:"+key.title())
    print("值为:"+value.title())
print("-------------------------------------------------------------------------------------")
# 按照顺序遍历字典，解决字典遍历不按顺序排列
name7 = {"id": 1,
         "name": "yu",
         "city": "杭州"}
for key,value in sorted(name7.items()):
    print(key.title()+":"+str(value).title())
print("-------------------------------------------------------------------------------------")
name8 ={"tpy": "bm",
        "ydh": "yd",
        "jn": "chid"}
for key in sorted(name8.keys()):
    print("河流的名称:"+key.title())
print("-------------------------------------------------------------------------------------")
for value in sorted(name8.values()):
    print("河流经过的国家:"+ value.title())
print("-------------------------------------------------------------------------------------")
# 在字典中可以进行嵌套，其中字典中可以嵌套列表，而列表中也可以嵌套字典
name9 = {"java": ["jar", "jre", "jdk"],
         "python": ["django"],
         "c": ["c++", "c#"]}
for key ,value in sorted(name9.items()):
    print(key.title()+"包含的语言如下:")
    for v in value:
        print(v.title())
print("-------------------------------------------------------------------------------------")