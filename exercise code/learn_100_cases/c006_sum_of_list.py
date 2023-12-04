# 求列表的元素之和
def sum_of_list(param_list):
    total = 0
    for i in param_list:
        total += i

    return total
list1=[1,5,8,6,2]
list2=[7,5,3,0,12]
print(f"sum of {list1} , ",sum_of_list(list1))
print(f"sum of {list2} , ",sum_of_list(list2))

