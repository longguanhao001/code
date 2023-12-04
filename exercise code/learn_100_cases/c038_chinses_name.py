# content="""
# 李明喜欢韩美美，他俩早恋了
# """
with open("./data/鹿鼎记.txt", encoding="utf-8") as fin:
    content=fin.read()
import jieba.posseg as posseg
words=[]
for word,flag in posseg.cut(content):
    if flag == "nr":
        words.append(word)

import  pandas as pd

print(pd.Series(words).value_counts()[:20])