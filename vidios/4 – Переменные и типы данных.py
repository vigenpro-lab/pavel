number = 5  # int

digit = 4.54356876  # float
word = "Результат:"  # str
boolean = True  # bool

str_num = "5"  # str

# print(word + str(digit))

print(word, number)
print(word + str(number + bool(str_num)))

print("Результат:", number)

del number

number = 7
print("Результат:", number)

num1 = int(input("Введите первое число: "))

num2 = int(input("Ведите второе число: "))

num1 += 5

print("Результат:", num1 + num2)
print("Результат:", num1 - num2)
print("Результат:", num1 / num2)
print("Результат:", num1 * num2)
print("Результат:", num1 ** num2)
print("Результат:", num1 // num2)

word = "Hi"
print(word * 2)

word = True
