#!/Users/lsy python
# coding:utf-8
# lsy
'''
在类中使用迭代器
raise StopIteration 为了防止无限循环，设置条件，当循环到一定次数停止循环
'''
# 在类中使用迭代器
class Myname():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

if __name__ == '__main__':
    myclass = Myname()
    my = iter(myclass)
    for i in my:
        print(i)
