# 读取文件计算科目的最高分、最低分以及平均分
course_grade = {}


with open("course_student_grade.txt",encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, grade = line.split(",")
        if course not in course_grade:
            course_grade[course] = []
        course_grade[course].append(int(grade))

for course, grade in course_grade.items():
    print(
        course,
        max(grade),
        min(grade),
        sum(grade)/len(grade)
    )