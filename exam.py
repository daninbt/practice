# 1)

a = float(input("طول ضلع اول را وارد کنید: "))
b = float(input("طول ضلع دوم را وارد کنید: "))
c = float(input("طول ضلع سوم را وارد کنید: "))


if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("این اعداد یک مثلث متساوی‌الاضلاع می‌سازند.")
    else:
        print("این اعداد یک مثلث می‌سازند اما متساوی‌الاضلاع نیستند.")
else:
    print("این اعداد اصلا نمی‌توانند یک مثلث بسازند!")

# 2)

num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))
num3 = float(input("عدد سوم را وارد کنید: "))


بزرگترین = max(num1, num2, num3)

print(f"بزرگترین عدد وارد شده {بزرگترین} است.")

# 3)

year = int(input("یک سال را وارد کنید: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"سال {year} کبیسه است.")
else:
    print(f"سال {year} کبیسه نیست.")

# 4)

score = float(input("نمره دانش‌آموز (بین ۰ تا ۲۰) را وارد کنید: "))


if score < 0 or score > 20:
    print("نمره وارد شده معتبر نیست! لطفاً عددی بین ۰ تا ۲۰ وارد کنید.")
elif score < 10:
    print("وضعیت: ضعیف")
elif score < 15:
    print("وضعیت: متوسط")
elif score < 18:
    print("وضعیت: خوب")
else: 
    print("وضعیت: عالی")

# 5)

num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))


operator = input("عملگر را وارد کنید (+, -, *, /): ")


if operator == '+':
    result = num1 + num2
    print(f"نتیجه: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"نتیجه: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"نتیجه: {result}")
elif operator == '/':
    if num2 == 0:
        print("خطا: تقسیم بر صفر امکان‌پذیر نیست!")
    else:
        result = num1 / num2
        print(f"نتیجه: {result}")
else:
    print("خطا: عملگر ناشناخته بود!")