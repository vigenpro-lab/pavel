# user = int(input())
# answer = 0
# for i in range(2, user // 2 + 1):
#     if user % i == 0:
#         answer = answer + 1
# if answer <= 0:
#     print("простое")
# idk


def isprime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


user = int(input())
for i in range(user):
    if isprime(i):
        print(i)
