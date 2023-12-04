import re
with open("data/English_article.txt") as fin:
    content=fin.read()
# print(content)
words = re.split(r"[\s.()-?@#$%^&*.,]+", content)

import pandas as pd
print(pd.Series(words).value_counts()[:20])