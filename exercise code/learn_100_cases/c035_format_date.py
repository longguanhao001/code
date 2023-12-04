content="""
白日2023/03/20依山尽，
黄河入2022.05.15海流，
欲穷千里11-06-2023目，
更5/29/2020上一层楼
"""
import re
content = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", content)
content = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", content)

content = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", content)
content = re.sub(r"(\d{1})/(\d{2})/(\d{4})", r"\3-0\1-\2", content)
print(content)