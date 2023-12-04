"""
递归搜索目录，找出最大的文件
for root, dirs, files in os.walk('python/Lib/email'):
 root代表当前目录
 dirs代表当前目录下的子目录
 files代表当前目录下的普通文件
"""
import os
search_dir = "./arrange_dir"
result_files = []
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(".txt"):
            file_path = {f"{root}/{file}"}
            result_files.append((file_path, os.path.getsize(file_path)/1024))


print(
    sorted(result_files,
             key=lambda x: x[1],
             reverse=True)
)