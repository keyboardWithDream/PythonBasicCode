def mgGen():
    print("生成器被执行！")
    yield print("第二次执行！")
    yield print("第三次执行！")

myG = mgGen()
next(myG)
print("===========")
next(myG)
print("===========")


def fibs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


for each in fibs():
    if each > 100:
        break
    print(each, end=" ")