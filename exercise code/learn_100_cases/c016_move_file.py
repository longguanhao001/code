"""
按文件后缀名整理文件夹
获取文件后缀名
import os
os.path.splitext('/path/to/aaa.mp3')
    输入:('/path/to/aaa', '.mp3')

移动文件
import shutil
shutil.move("aaa.txt", "dir/bbb.foo")

"""

import os
import shutil
dir = "./arrange_dir"
for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")



    soucre_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(soucre_path, target_path)

