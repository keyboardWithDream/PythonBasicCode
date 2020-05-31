from math import pi

"""
将华氏温度转换为摄氏温度
华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

Version: 0.1
Author: 骆昊
"""

f = float(input("请输入华氏度："))
c = (f - 32) / 1.8
print("%.1f华氏度 =  %.1f摄氏度" % (f, c))

print("=======================")

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""

r = float(input("请输入圆的半径："))
perimeter = 2 * pi * r
area = pi * (r ** 2)
print("%.3f半径的圆，周长为：%.3f,面积为：%.3f" % (r, perimeter, area))

print("========================")

"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""

year = input("请输入年份：")
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(True)
else:
    print(False)
