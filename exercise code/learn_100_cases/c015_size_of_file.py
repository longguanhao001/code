# 获取文件的大小与目录下所有文件的大小
import os
print(os.path.getsize("English_article.txt"))

sum_size = 0
for file in os.listdir("."):
    if os.path.isfile(file):
        sum_size += os.path.getsize(file)

print("all size of dir: ",sum_size/1024)