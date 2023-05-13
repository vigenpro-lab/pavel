str1 = input()
str2 = input()
str1_list = list(str1)
str1_list.sort()
str2_list = list(str2)
str2_list.sort()

print(str1_list == str2_list)
