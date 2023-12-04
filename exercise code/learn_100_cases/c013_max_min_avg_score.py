# 读取文件内的数据，计算分数最大值、最小值、平均值
def computer_score():
    score = []
    with open("./student_grade_input.txt", encoding='utf-8') as fin:
        for line in fin:
            line = line[:-1]
            fields = line.split(",")
            score.append(int(fields[-1]))

    max_score = max(score)
    min_score = min(score)
    avg_score= round(sum(score)/len(score),2)
    return max_score, min_score, avg_score

max_score, min_score, avg_score = computer_score()

print(f"max_score : {max_score}, min_score : {min_score} , avg_score : {avg_score} ")




