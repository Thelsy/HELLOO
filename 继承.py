#!/Users/lsy python
# coding:utf-8
# lsy

# 定义汽车类
class Car():
    def __init__(self,engine,gasoline):
        # 初始化属性
        self.engine = engine
        self.gasoline = gasoline
        # 发动机更换方法
    def engineAsy(self,enginea):
        self.engine = enginea
    def print(self):
        print(self.engine +":"+self.gasoline)
if __name__ == '__main__':
    update = Car('德国','三星')
    update.print()
    update.engineAsy('日本')
    update.print()

