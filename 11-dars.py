# # OR dan foydalanish
# kun = input("Bugun nima kun? >>> ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Dam olish kuni")
# else:
#     print("Ish kuni")


# # AND dan foydalanish
# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? >>> "))

# if (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat >= 30:
#     print("Cho'milgani ketdik")
# elif (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat < 30:
#     print("Uyda o'tiramiz.")


# # Restoran
# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy:
#     print("Choy olindi")
#     narh = narh + 3000

# if salat:
#     print("Salat olindi")
#     narh = narh + 5000

# if non:
#     print("Non olindi")
#     narh = narh + 2500

# if kompot:
#     print("Kompot olindi")
#     narh = narh + 8000

# if assorti:
#     print("Assorti olindi")
#     narh = narh + 20000

# print(f"Jami {narh} so'm bo'ldi")



# # IN operatori
# menu = ["osh", "kabob", "shashlik", "norin", "somsa"]
# print("somsa" in menu)


# # IN operatoriga misol
# menu = ["osh", "kabob", "shashlik", "norin", "somsa"]
# ovqat = input("Nima ovqat yeysiz? >>> ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q.")


# # Solishtirish
# menu = ["osh", "kabob", "shashlik", "norin", "somsa"]
# buyurtmalar = ["osh", "shashlik", "manti", "sho'rva", "norin"]

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Menuda {taom} mavjud emas.")
# else:
#     print("Buyurtmalar bo'sh")










# AMALIYOT

# Juftligini tekshirish
son = int(input("Juft son kiriting >>> "))
if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu juft son emas.")


# Chipta narxi
yosh = int(input("Yoshingizni kiriting >>> "))
if yosh <= 4 or yosh >= 60:
    narh = "bepul"
elif yosh < 18:
    narh = 10000
else:
    narh = 20000

print(f"Sizga kirish {narh}.")


# Katta yoki kichiklik
son_1 = int(input("Birinchi sonni kiriting >>> "))
son_2 = int(input("Ikkinchi sonni kiriting >>> "))

if son_1 > son_2:
    print(f"{son_1} > {son_2}")
elif son_1 < son_2:
    print(f"{son_1} < {son_2}")
else:
    print(f"{son_1} = {son_2}")


# Mahsulotlarni tekshirish
mahsulotlar = ["pepsi", "anor", "go'sht", "non", "uzum", "anor", "limon", "sabzi", "guruch", "zira"]

savat = []

for i in range(5):
    savat.append((input(f"Savatga {i + 1} - mahsulotni qo'shing: ")))

bor_mahsulotlar = []
mavjud_emas = []

for mahsulot in savat:
        if mahsulot in mahsulotlar:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Do'konimizda siz so'ragan barcha mahsulot bor.")


# Login tekshirish
users = ["admin", "anvar", "asad", "asal", "aliya"]
user = input("Yangi login kiriting: ")

if user.lower() in users:
    print("Login band, yangi login tanlang.")
else:
    print("Xush kelibsiz!")


# 2 dan 10 gacha qoldiqsiz bo'linishni tekshirish
son = int(input("Istalgan butun son kiriting: "))

for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi.")
