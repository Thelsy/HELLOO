#!/Users/lsy python
# coding:utf-8
# lsy
''' 迭代是python最强大的功能之一，是访问集合元素的一种方式
    迭代器是可以记住遍历位置的对象
    迭代器对象从集合的第一个元素开始访问，直到所有元素访问完毕，迭代器只能往前不会后退
    迭代器有2个基本的方法：iter()和next()
    字符串中。列表或元组都可以创建迭代器对象
'''
import sys
list = [1,2,3,4]
li = iter(list)
print(next(li))
print(next(li))
print(next(li))
print(next(li))

# 迭代器使用for循环遍历
it = iter(list)
for i in it:
    print(i, end=' ')
print()

# 使用while循环 next()方法
iq = iter(list)
while True:
    try:
        print(next(iq))
    except Exception as e:
        print(e)
        sys.exit()






