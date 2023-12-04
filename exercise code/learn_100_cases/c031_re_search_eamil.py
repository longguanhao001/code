content=""""
ejjadooj附近的角色分配1523021@qq.com
djdj进口的方式连接4512541#163.com
计算机都i及khjddh@163.com
而瓦解hi哦是小小年纪开发51254ddfdhj@gmail.com
ajskdkads得很生动ifjsfjkdf@dsdd.fdlfk.cn
顶顶顶aaa@must.edu.mo
哇哇哇哇skfsj@must.aaa#f减肥的经济法dkfdj.com
"""

import re
# 这种写法@后面有多个.的话就只会保留第一段
# pattern = re.compile(r"""
#     [a-zA-Z0-9-_]+
#     @
#     [a-zA-Z0-9]+
#     \.
#     [a-zA-Z]{2,4}
# """, re.VERBOSE)


pattern = re.compile(r"""
    [a-zA-Z0-9-_]+
    @
    [\w.]+
""", re.VERBOSE)

results = pattern.findall(content)
for result in results:
    print(result)