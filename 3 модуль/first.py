import numpy

question = input().split()
for i in range(0, len(question)):
    question[i] = int(question[i])
print(numpy.mean(question))

# question = input().split()
# for i in range(0, len(question)):
#     question[i] = int(question[i])
# print(sum(question) / len(question))
