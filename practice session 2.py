# 1

word ="international"
print(word[0] ,word[len(word)//2],word[-1])
print("="*40)
# 2

str1 = "python"
str2 = "programing"

e = str2[len(str2)//2]
f = str1 + e
print(f)
print("="*40)
# 3

a = "DjAnGOFraMeWork"

b = ""
c = ""

for i in a:
    if i.isupper():
        c = c + i
    else:
        b = b + i

print(b + c)

print("="*40)
# 4

spiderman = "[۱۲][۱۱][۹][۱۰]مرد عنکبوتی(به انگلیسی: spider-Man) با نام واقعی پیتِر بِنجامین پارکِر، یک شخصیت تخیلی ابرقهرمان در کتاب‌های داستان مصور آمریکایی است که توسط مارول کامیکس منتشر می‌شود. این شخصیت حاصل همکاری استن لی، نویسنده و خالق چندین ابرقهرمان معروف مارول، و استیو دیتکو است."

spiderman = spiderman.replace("[۹]", "")
spiderman = spiderman.replace("[۱۰]", "")
spiderman = spiderman.replace("[۱۱]", "")
spiderman = spiderman.replace("[۱۲]", "")
b = spiderman.split()
print(len(b))