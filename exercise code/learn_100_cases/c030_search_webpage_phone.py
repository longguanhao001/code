# 读取一个文件，把里面的所有电话号码都匹配出来
import re
file_content=""
with open("./data/web_page_phone.txt", encoding='utf-8') as fin:
    file_content=fin.read()

pattern = r"(?<!\d)1[3-9]\d{9}(?!\d)"
results = re.findall(pattern, file_content)

for result in results:
    print(result)