import random


n=int(input("请输入数字："))




a = random.randint(1,100)

while n != a:
    if n > a:
        n=int(input("数字大了，请重新输入数字："))
    elif n < a:
        n=int(input("数字小了，请重新输入数字："))


print("你赢了")