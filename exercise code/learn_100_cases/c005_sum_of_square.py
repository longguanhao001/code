# 前N项的和，1^2 + 2^2 + 3^2 + …… + N^2
def sum_of_square(n):
    result = 0
    for number in range(1,n+1):

        result += number * number
    return  result

print("前3项的平方和：",sum_of_square(3))
print("前10项的平方和：",sum_of_square(10))
print("前54项的平方和：",sum_of_square(54))
print("前100项的平方和：",sum_of_square(100))
