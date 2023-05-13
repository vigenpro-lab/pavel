n = int(input())
cnt = 1
for i in range(2, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == 2:
        print("простое")
    else:
        print("не простое")

n = int(input())
cnt = 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        cnt += 1
    if cnt == 2:
        print("простое")
    else:
        print("не простое")
