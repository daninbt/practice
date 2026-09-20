# 1)

list1 = [1, 5, 50, 3, 8, 90]

list1[4] = 80

print(list1)

print("="*40)

# 2)

list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list2[2][2].insert(2, 7000)

print(list2)

print("="*40)

# 3)

a = "1403"

b = ""

c = "۰۱۲۳۴۵۶۷۸۹"

b = b + c[int(a[0])]
b = b + c[int(a[1])]
b = b + c[int(a[2])]
b = b + c[int(a[3])]

print(b)

# 4)

a = int(input("please enter a number : "))

if a % 2 == 0 and a % 3 == 0:
    print(f"{a}it is divisible by 6 ..!")
else:
    print(f"{a} it isn't divisible by 6 ..!")


# 5)
a = "pass"
b = "4567"

c = input("please enter your username : ")
d = input("please enter your password : ")

if c == a and d == b:
    print("welcome")
else:
    print("username or password is wrong")


# 6)
a = input("please enter your grade with (A, B, C, F) : ")

if a == "A":
    print("your grade is between 17 and 20 ..!")
elif a == "B":
    print("your grade is between 14 and 17 ..! ")
elif a == "C":
    print("your grade is between 10 and 14 ..! ")
elif a == "F":
    print("your grade is under than 10 ..!")
else:
    print("the grade is invalid !! please enter A, B , C , F ..!")