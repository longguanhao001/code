# 统计文章中出现单词的次数，打印出现次数最多的单词

count_word = {}

with open("./English_article.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()

        for word in words:
             if word not in count_word:
                 count_word[word] = 0

             count_word[word] += 1

# print(count_word)
print(
    sorted(
        count_word.items(),
        key= lambda x: x[1],
        reverse = True
    )[:10]
)
