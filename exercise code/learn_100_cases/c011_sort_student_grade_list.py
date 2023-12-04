# 对学神成绩进行排序
students_grade = [
    {"stuno":"101", "name":"李四", "grade":95 },
    {"stuno":"111", "name":"王五", "grade":53 },
    {"stuno":"121", "name":"王大雷", "grade":68 },
    {"stuno":"131", "name":"朱建军", "grade":59 },
    {"stuno":"141", "name":"Sally", "grade":85 },
]
students_grade_sorts=sorted(students_grade,
                            key=lambda x: x["grade"],
                            reverse=True)
print(students_grade)

print(students_grade_sorts)

