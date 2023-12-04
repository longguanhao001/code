# 输入三个数字，比较大小
num1=int(input("please input: "))
num2=int(input("please input:"))
num3=int(input("please input:"))
a = []
a.append(num1)
a.append(num2)
a.append(num3)
# b = sorted(a)# 如果需要转换成新的列表，需要使用sorted
a.sort()
# a.sort(reverse=True)  # 从大到小
print(a)

# if num1 >= num2 >= num3: print(num1, num2, num3)
# elif num1 >= num3 >= num2: print(num1, num3, num2)
# elif num2 >= num1 >= num3: print(num2, num1, num3)
# elif num2 >= num3 >= num1: print(num2, num3, num1)
# elif num3 >= num1 >= num2: print(num3, num1, num2)
# elif num3 >= num2 >= num1: print(num3, num2, num1)