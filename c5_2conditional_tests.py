str1 = "shenzhicheng"
str2 = "shengzhichen"
print(str1 == str2)

print("\n")

str1 = "Shenzhicheng"
str2 = "shenzhicheng"
print(str1.lower() == str2)

print("\n")

num1 = 1
num2 = 2
print(num1 > num2)
print(num1 == num2)
print(num1 < num2)
print(num1 != num2)
print(num1 >= num2)
print(num1 <= num2)

print("\n")

#and & or

print(1 <= 2 and 3 > 2)
print(1 > 2 and 3 > 2)
print(1 > 2 or 3 > 0 )
print(1 == 2 or 3 == 4)

print("\n")

#in & not in

names = ["jack","rose","tom","jason"]
if 'jack' in names:
    name = 'jack'
    print(name.title() + " is in the list")
if 'Mac' not in names:
    name = 'mac'
    print(name.title() + " is not in the list")
