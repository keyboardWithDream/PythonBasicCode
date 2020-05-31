class MyProperty:
    def __init__(self, f_get=None, f_set=None, f_del=None):
        self.f_get = f_get
        self.f_set = f_set
        self.f_del = f_del

    def __get__(self, instance, owner):
        return self.f_get(instance)

    def __set__(self, instance, value):
        return self.f_set(instance, value)

    def __delete__(self, instance):
        self.f_del(instance)


class Test:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


test = Test()
test.x = 10
print(test.x, test.getX())
del test.x
print(getattr(test, 'x', '没有x属性'))
print('====================================')


class ConvertToC:
    def __init__(self, f_get=None, f_set=None, f_del=None):
        self.f_get = f_get
        self.f_set = f_set
        self.f_del = f_del

    def __get__(self, instance, owner):
        return (self.f_set(instance)-32) * 5 / 9

    def __set__(self, instance, value):
        self.f_set(instance, value)

    def __delete__(self, instance):
        self.f_del(instance)


class ConvertToF:
    def __init__(self, f_get=None, f_set=None, f_del=None):
        self.f_get = f_get
        self.f_set = f_set
        self.f_del = f_del

    def __get__(self, instance, owner):
        return self.f_set(instance) * 9 / 5 + 32

    def __set__(self, instance, value):
        self.f_set(instance, value)

    def __delete__(self, instance):
        self.f_del(instance)


class Temperature:
    def __init__(self):
        self._temperature = None

    def getTemperature(self):
        return self._temperature

    def setTemperature(self, value):
        self._temperature = value

    def delTemperature(self):
        del self._temperature

    f = ConvertToF(getTemperature, setTemperature, delTemperature)
    c = ConvertToC(getTemperature, setTemperature, delTemperature)


t = Temperature()
t.f = 2
print(t.f)