import re
from collections import Counter

import jieba

with open("ming_shi.txt", encoding="utf-8") as f:
    text = f.read()

counts = Counter()
for word in jieba.cut(text):
    word = word.strip()
    if word and re.search(r"[\u4e00-\u9fff\w]", word):
        counts[word] += 1

print("最常见的前10个词:")
for word, count in counts.most_common(10):
    print(f"{word}\t{count}")

with open("top10_words.txt", "w", encoding="utf-8") as f:
    for word, count in counts.most_common(10):
        f.write(f"{word}\t{count}\n")
