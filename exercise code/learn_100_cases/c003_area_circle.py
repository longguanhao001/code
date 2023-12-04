import math
# 计算圆的面积，结果保留两位小数
def area_of_circle(r):
    return round(math.pi * r * r, 2)


print("半径是2的圆的面积是：", area_of_circle(2))
print("半径是7.2的圆的面积是：", area_of_circle(7.2))
print("半径是15.6的圆的面积是：", area_of_circle(15.6))
print("半径是8.88的圆的面积是：", area_of_circle(8.88))
