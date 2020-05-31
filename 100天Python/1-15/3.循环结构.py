from math import sqrt

"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

num = int(input("请输入一个正整数："))
end = int(sqrt(num)) + 1
is_prime = True
for i in range(2, end):
    if not num % i:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)

print("=====================")
