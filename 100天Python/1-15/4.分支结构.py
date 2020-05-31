"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 骆昊
"""

data = input("请输入长度+单位：")
unit = str(data[len(data) - 3:])
if unit.isalpha():
    value = float(data[:len(data) - 3])
    cm = value * 2.54
    print("%.3f英寸 = %.3f厘米" % (value, cm))
else:
    value = float(data[:len(data) - 2])
    mil = value / 2.54
    print("%.3f厘米 = %.3f英寸" % (value, mil))

print("========================")

"""
百分制成绩转换为等级制成绩

Version: 0.1
Author: 骆昊
"""

score = float(input("请输入成绩："))
if score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "C"
elif 70 > score >= 60:
    grade = "D"
else:
    grade = "E"
print("成绩等级为：" + grade)

print("=========================")

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
"""
length = ""
length = input("请输入3条边长，空格隔开:")
a = float(length[0])
b = float(length[2])
c = float(length[4])
if a + b > c and b + c > a and c + a > b:
    perimeter = a + b + c
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("周长为：%.2f,面积为：%.2f" % (perimeter, area))
else:
    print("不能构成三角形")
