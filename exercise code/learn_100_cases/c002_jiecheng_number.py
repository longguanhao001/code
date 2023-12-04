# 数字的阶乘
def jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return  result

print("6!=",jiecheng(6))
print("10!=",jiecheng(10))
print("0!=",jiecheng(0))

