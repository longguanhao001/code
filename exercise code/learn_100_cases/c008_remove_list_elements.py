# 移除列表的元素

def  remove_elements_from_list(lista,listb):
    for item in listb:
        lista.remove(item)
    return lista



lista = [1,5,7,9,11,15]
listb = [5,11]
print(f" from {lista} remove {listb} result: ", remove_elements_from_list(lista,listb))



lista = [1,5,7,9,11,15]
listb = [5,11]
data = [item for item in lista if item not in listb]
print(f" from {lista} remove {listb} result: ", data)