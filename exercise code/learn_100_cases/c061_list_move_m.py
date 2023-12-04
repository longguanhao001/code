# 有n个整数，使其前面各数顺序向后移动m个位置，最后的m个数变成最前面的m个数
# a是已知的
# a = [1,2,3,4,5,6,7,8]
# b = [0,0,0,0,0,0,0,0]
# a是未知的,n也是未知的
n = int(input("please input n: "))
a = []
b = []
for i in range(n):
    a.append(int(input("num: ")))
    b.append("0")
m = int(input("please input m: "))
if m <= n:
    t = 0
    for i in range(m, len(b)):
        b[i] = a[t]
        t += 1
    for i in range(len(b) - t):
        b[i] = a[t]
        t += 1
    print(b)
else:
    print("m应该要小于等于n")