# 面向对象编程
# 创建和使用类
# 方法 __init__(self)是一个特殊的方法，每当根据类创建新实例的时候,python都会运行他，开头&末尾2个下划线，这是python中的一种约定，为了避免与普通方法发生冲突
'''
__init__(self，age,name)在这个方法中有一个特殊的形参self，这个形参位置必须在其他形参位置的前面，以self为前缀的变量，可以供类中的所有方法使用
那么为什么要定义这个实参,因为当调用Dog类创建实例的时候，会自动向这个方法传递self实参，所以只需要向Dog类传入实参就可以
'''
class Dog():
    def __init__(self,age,name):
        # 初始化属性
        self.age = age
        self.name = name

    def sit(self):
        print(self.name.title())

    def update(self,mo,st):
        self.age = mo
        self.name = st
if __name__ == '__main__':
     my_dog = Dog(18,'wwww')
     my_dog.sit()
     my_dog.update(22,'qqq')
     print(my_dog.name.title()+' '+str(my_dog.age))
     print
