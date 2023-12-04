
content="""
小明买了12斤黄瓜花了8元;
小明买了2斤葡萄花了13.5元;
小明买了5斤白菜花了5.4元;

"""
# 要求提取(1、黄瓜、8)、(2、葡萄、13.5)、(5、白菜、5.4)
import re
for line in content.split("\n"):
    # print(line)
    pattern=r"(\d+)斤(.*)花了(\d+(\.\d+)?)元"
    match= re.search(pattern, line)
    if match:
        print(f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}")