user = input()
answer = []
for i in user:
    answer.append(max(i))
    user.replace(answer[0])
    for i in user:
        answer.append(max(i))
print(sum(answer))
