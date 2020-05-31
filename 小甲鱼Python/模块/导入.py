from 小甲鱼Python.模块 import hi
import 小甲鱼Python.模块.test.TemperatureConversion as tc

hi()
print('32摄氏度 = %.2f华氏度' % tc.c2f(32))
print('99华氏度 = %.2f摄氏度' % tc.f2c(99))
