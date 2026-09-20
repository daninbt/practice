# 1)
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end="\t")
    print()

# 2)
num1 = int(input("please enter a number : "))
num2 = int(input("please enter a number : "))


if num2 < num1:
    spare = num1
    num1 = num2
    num2 = spare

primes = []
for num in range(num1, num2+1):

    flag = 0
    for i in range(1, num):
        if num % i == 0:
            flag += i

    if flag == num:
        primes.append(num)


print(primes)


# 3)

a = [1, 50, 60, [2, 3, 4, 5,[ 6, 7,8 ,9 ], 10, 11], 12 ,13]

total = []
for i in a:
    if type(i) == int:
        total.append(i)
    else:
        for j in i:
            if type(j) == int:
                total.append(j)
            else:
                for z in j:
                   total.append(z)

print(total) 

# 4)
colors = ['crimson', 'blue', 'coral', 'red', 'crimson', 'blue', 'black', 'crimson']

uniqe = []

for i in colors:
    if i not in uniqe:
        uniqe.append(i)

print(uniqe)