for i in range(1, 6, 2):
    print(i)
count = 0
word = "Hello world"
for i in word:
    if i == "w":
        count += 1

print(count)

isHasCar = True

while isHasCar:
    if input() == "Stop":
        isHasCar = False

for i in range(1, 11):
    if i == 5:
        break

    if i % 2 == 0:
        continue

    print(i)

found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False

print(found)
