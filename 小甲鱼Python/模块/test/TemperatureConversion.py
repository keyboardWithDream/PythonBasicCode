def c2f(c):
    f = c * 1.8 + 32
    return f


def f2c(f):
    c = (f - 32) / 1.8
    return c


def test(num):
    print('%.2f华氏度 = %.2f摄氏度' % (num, f2c(num)))
    print('%.2f摄氏度 = %.2f华氏度' % (num, c2f(num)))


if __name__ == '__main__':
    test(0)