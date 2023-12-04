a = [1,2,7,3,18,10,4,3]
print((len(a))//2)

for i in range(0,len(a)//2):
    temp = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = temp
print(a)