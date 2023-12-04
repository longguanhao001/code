"""
写一个函数，验证密码是否符合条件
1.长度位于[6, 20]之间
2.必须包含至少一个小写字母
3.必须包含至少一个大写字母
4.必须包含至少一个数字
5.必须包含至少一个特殊字符
返回
    True, None
    或者False， 原因
"""

import re
def check_passsword(password):
    if not  6 <= len(password) <= 20:
        return False, "密码长度必须在6-20之间"
    if not re.findall(r"[a-z]", password):
        return False, "必须包含至少一个小写字母"

    if not re.findall(r"[A-Z]", password):
        return False, "必须包含至少一个大写字母"

    if not re.findall(r"[0-9]", password):
        return False, "必须包含至少一个数字"
    if not re.findall(r"[^0-9a-zA-Z]", password):
        return False, "必须包含至少一个特殊字符"
    else:
        return True, None

print("Hello#123455", check_passsword("Hello#123455"))
print("hello#123455", check_passsword("hello#123455"))
print("Hello123455", check_passsword("Hello123455"))
print("Hello#", check_passsword("Hello#"))