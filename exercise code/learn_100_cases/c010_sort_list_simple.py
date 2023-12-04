# 对简单列表进行排序，升序排序和降序排序
lista=[10,50,666,777,20,3]
lista.sort()
lista=[10,50,666,777,20,3]
listb = sorted(lista)
lista.sort(reverse=True)
listd = sorted(lista,reverse=True)

print(f"lista is {lista}")
print(f"listb is {listb}")
print(f"lista is {lista}")
print(f"lista is {listd}")