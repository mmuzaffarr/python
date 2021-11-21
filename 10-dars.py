# cars = ["audi", "volvo", "bmw", "kia", "hyundai"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())


# ism = input("Ismingizni kiriting: ")

# if ism.lower() != "ali":
#     print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
# else:
#     print("Salomm, Ali")

# javob = float(input("12 x 6 nechiga teng? >>>>"))
# if javob != 72:
#     print("Javob xato!")
# else:
#     print(True)


# yosh = int(input("Yoshingiz nechida?: "))
# if yosh >= 18:
#     print("Welcome")
# else:
#     print("You don't have permisson!")


# login = input("Yangi login kiriting: ")
# if len(login) <= 5:
#     print("5 tadan ko'p bo'lishi kerak!")


# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2021 - yil < 18:
#     print(f"Yoshingiz {2021 -yil} da ekan,")
#     print("Kirish mumkin emas!")
# else:
#     print("Welcome")





# AMALIYOT

# Ro'yxat bilan ishlash
cars = ["toyota", "mazda", "hyundai", "kia", "gm"]
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())


# Teng emas operatori yordamida
cars = ["toyota", "mazda", "hyundai", "kia", "gm"]
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())



# Login kiritish
foydalanuvchi_ismi = input("Loginni kiriting: ")

if foydalanuvchi_ismi.lower() == "admin":
    print("Xush kelibsiz, Admin. \nFoydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {foydalanuvchi_ismi.title()}!")


# Sonlar tengligini tekshirish
a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))

if a == b:
    print("Sonlar teng!")
else:
    print("Sonlar teng emas.")


# Musbat va manfiylikni aniqlash
a = int(input("Ixtiyoriy sonni kiriting: "))
print("Manfiy son") if a < 0 else print("Musbat son")


# Ildiz hisoblash
a = int(input("Sonni kiritng: "))
print(a**0.5) if a > 0 else print("Musbat sonni kiriting!")