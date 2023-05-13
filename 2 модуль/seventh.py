import itertools
#
text = list(input())
# print(list(itertools.combinations(text, len(text))))

# from itertools import combinations
# x = ["f", "d", "Ä", "f"]
# print(list(combinations(x, 4)))

perm_set = itertools.permutations(text)
print(list(perm_set))