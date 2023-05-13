# user = input()
# correct = []
# incorect = []
#
# for i in user:
#     if int(i) % 2 == 0:
#         correct.append(i)
#     else:
#         incorect.append(i)
# print(correct)
# print(incorect)


inp = input().split()
for i in range(0, len(inp)):
    inp[i] = int(inp[i])

for i in inp:
    if i % 2 == 0:
        print(i)
