import os

contents=[]
data_dir = "./data/many_texts"
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path,encoding="utf-8") as fin:
            contents.append(fin.read())

    final_contents = "\n".join(contents)

with open("./data/many_texts.txt", "w", encoding="utf-8") as fount:
    fount.write(final_contents)
