from collections import Counter

word = input()
c = Counter(word)
print(c.most_common(1)[0][0])
