content="""
今日推荐拜入大苏打
 180153656661111
无锡电信￥5200大大大jj0ds1
 19881892666
达州移动￥4900大苏打都是对的
 18301050106
"""
import re
# pattern=r"(1[3-9]\d{9})"
# print(re.sub(pattern, r"\1******", content))




pattern=r"(1)(\d{6})"

def replace(m):
    return m.group(1) + "******"

print(re.sub(pattern, replace, content))