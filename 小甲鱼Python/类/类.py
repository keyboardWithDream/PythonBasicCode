import random as r
import os

def move():
    steps = 0
    directions = input('请输入方向(WASD):').upper()
    while directions not in ['W', 'A', 'S', 'D']:
        print('输入有误，请重新输入!')
        directions = input('请输入方向(WASD):').upper()
    steps = int(input('请输入步数(最大两步):'))
    while steps > 2 or steps < 1:
        print('输入有误！请重新输入!')
        steps = int(input('请输入步数(最大两步):'))
    return directions, steps


class Turtle:
    def __init__(self):
        self.power = 10
        self.set = [r.randint(1, 10), r.randint(1, 10)]

    def move(self, direction, step):
        if direction == 'S':
            new_y = self.set[1] + step
            if new_y > 10:
                self.set[1] = 10 - (new_y - 10)
            else:
                self.set[1] = new_y
        elif direction == 'W':
            new_y = self.set[1] - step
            if new_y < 1:
                if self.set[1] == 1:
                    self.set[1] = self.set[1] + step
                else:
                    self.set[1] = step
            else:
                self.set[1] = new_y
        elif direction == 'A':
            new_x = self.set[0] - step
            if new_x < 1:
                if self.set[0] == 1:
                    self.set[0] = self.set[0] + step
                else:
                    self.set[0] = step
            else:
                self.set[0] = new_x
        else:
            new_x = self.set[0] + step
            if new_x > 10:
                self.set[0] = 10 - (new_x - 10)
            else:
                self.set[0] = new_x
        self.power -= 1
        return self.set

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        self.set = [r.randint(1, 10), r.randint(1, 10)]

    def move(self):
        # 确定行走方向
        direction = r.choice([0, 1, 2, 3])
        if direction == 0:
            new_y = self.set[1] + 1
            if new_y > 10:
                self.set[1] = 10 - (new_y - 10)
            else:
                self.set[1] = new_y
        elif direction == 1:
            new_y = self.set[1] - 1
            if new_y < 0:
                self.set[1] = 10 + (new_y - 10)
        elif direction == 2:
            new_x = self.set[0] - 1
            if new_x < 0:
                self.set[0] = 10 + (new_x - 10)
            else:
                self.set[0] = new_x
        else:
            new_x = self.set[0] + 1
            if new_x > 10:
                self.set[0] = 10 - (new_x - 10)
            else:
                self.set[0] = new_x
        return self.set


# 初始乌龟
def start_turtle():
    turtle = Turtle()
    return turtle


# 初始鱼
def start_fish():
    fish = []
    for i in range(10):
        creat_fish = Fish()
        fish.append(creat_fish)
    return fish


# 初始棋盘
def rest_local():
    local_set = []
    for i in range(10):
        for j in range(10):
            local_set.append([j + 1, i + 1, 0])
    return local_set


# 打印棋盘
def show_local(turtle, fish, local_set):
    for i in range(100):
        local_set[i][2] == 0
    for i in range(len(fish)):
        fish_set = fish[i].set
        cont = 0
        while cont < 100:
            if local_set[cont][0] == fish_set[0] and local_set[cont][1] == fish_set[1]:
                local_set[cont][2] = 2
                break
            else:
                cont += 1
    cont = 0
    while cont < 100:
        if local_set[cont][0] == turtle.set[0] and local_set[cont][1] == turtle.set[1]:
            local_set[cont][2] = 1
            break
        else:
            cont += 1
    for i in range(100):
        if local_set[i][0] == 10:
            if local_set[i][2] == 1:
                print('O')
            elif local_set[i][2] == 2:
                print('X')
            else:
                print('-')
        else:
            if local_set[i][2] == 1:
                print('O  ', end='')
            elif local_set[i][2] == 2:
                print('X  ', end='')
            else:
                print('-  ', end='')


# 重置
turtle = start_turtle()
fish = start_fish()
local_set = rest_local()
list1 = []
print(len(fish))
# 开始
show_local(turtle, fish, local_set)
# 当鱼被吃完或体力消耗完时结束
while len(fish) > 0 and turtle.power > 0:
    # 乌龟移动
    where = move()
    turtle.move(where[0], where[1])
    # 乌龟吃了鱼 鱼-1 体力+20
    for i in range(len(fish)):
        if turtle.set[0] == fish[i].set[0] and turtle.set[1] == fish[i].set[1]:
            fish.pop(i)
            turtle.eat()
            break
        else:
            pass
    print('提示：你现在吃了%d条鱼，目前体力：%d,还剩下%d条鱼！' % (10-len(fish), turtle.power, len(fish)))
    # 鱼移动
    for i in range(len(fish)):
        fish[i].move()
    # 更新打印
    local_set = rest_local()
    show_local(turtle, fish, local_set)
print('你赢了！！！')
os.system('pause')

