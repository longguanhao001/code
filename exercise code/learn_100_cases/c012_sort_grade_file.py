def read_file():
    result = []
    with open("./student_grade_input.txt", encoding='utf-8') as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))

    return result
def sort_grade(datas):
    return sorted(datas,
                  key=lambda x: int(x[2]),
                  reverse=True)
def write_file(datas):
    with open("./student_grade_output.txt",  "w", encoding='utf-8') as fout:
        for data in datas:
            fout.write(",".join(data) + "\n")


# 1.读取文件,读取文件，对文件内的数据按分数倒序排列
datas= read_file()
print("read_file datas ", datas)

# 2.将数据进行排序
datas= sort_grade(datas)
print("read_file datas ", datas)

# 3.输出文件
write_file(datas)