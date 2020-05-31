class Parent:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('正在调用父类方法！')

    def getName(self):
        print(self.name)


class Child(Parent):
    def getName(self):
        print('这是对父类方法的复写!')


p = Parent('Harlan')
p.hello()
p.getName()
c = Child('没名字')
c.hello()
c.getName()
