# 去除列表重复元素
def get_unqie_list(lista):
    result=[]
    for item in lista:
        if item not in result:
            result.append(item)

    return result

lista = [5,7,6,9,10,6,7]
print(f" source list: {lista} unqie list:", get_unqie_list(lista))


lista = [5,7,6,9,10,6,7]
print(f" source list: {lista} unqie list:", list(set(lista)))