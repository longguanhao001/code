student_like_count={}
with open("./data/student_like.txt",encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        sname, likes = line.split(" ")
        like_list = likes.split(",")
        for like in like_list:
            if like not in student_like_count:
                student_like_count[like] = 0
            student_like_count[like] += 1


print(student_like_count)

