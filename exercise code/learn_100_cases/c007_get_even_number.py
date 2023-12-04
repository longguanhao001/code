# 返回开始结束区间的偶数（不包含结束值）
def get_even_number(begin,end):
    result = []
    for i in range(begin,end):
        if i % 2 == 0:
            result.append(i)
    return result


begin = 0
end = 15
print(f"begin={begin} end={end} even number : " , get_even_number(begin,end))


# [列表,for循环,判断]
data=[i for i in range(begin,end) if i %2 == 0]
print(f"begin={begin} end={end} even number : " , data)