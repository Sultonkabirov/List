# def counter_dict(nums: list[int])->dict:
#     d={}
#     for i in range(len(nums)):d[nums.count(nums[i])] = nums[i]
#     return d



# print(counter_dict([1,2, 1, 1, 1]))
# Loyihacha
#  
contacts = {}


def see():
    print("1.Qoshish")
    print("2.O'zgartirish")
    print("3.Qidirish")
    print("4.O'chirish")
    print("5.Ko'rish")


def add_to_contact():
    try:
        name = input("Name: ")
        number = input("Phone number: ")
        contacts[name] = number
        print("Qushildi!!")
    except Exception as e:
        print(f"Error: {e}")


def change_contact():
    try:
        name = input("Name: ")
        number = input("Phone number: ")
        contacts[name] = number
        print("O'zgartirildi!!")
    except Exception as e:
        print(f"Error: {e}")


def find_contact():
    try:
        name = input("Name: ")
        print(name, contacts[name])
    except Exception as e:
        print(f"Error: {e}")


def remove_contact():
    try:
        name = input("Name: ")
        del (contacts[name])
        print("O'chirildi!! ")
    except Exception as e:
        print(f"Error: {e}")


def see_contacts():
    try:
        for k, v in contacts.items():
            print(k, v)
    except Exception as e:
        print(f"Error: {e}")


while True:
    see()
    num = int(input("\nTanlovni kiriting:"))
    match num:
        case 1:  add_to_contact()
        case 2:  change_contact()
        case 3:  find_contact()
        case 4:  remove_contact()
        case 5:  see_contacts()
        case _:
            print("Warning !!!")
            break
    print("\n")
#----------------------------

# def  merge_list(l1:list[str],l2:list[int])->dict:
#    a={}
#    for i in range(len(l1)):
#       a[l1[i]]=l2[i]
#    return a

# res=merge_list([1, 2, 3],["a", "b", "c"])
# print(res)


# def str_counter(strs: list[str]) -> dict:
#     d = {}
#     for i in strs:
#         a = len(i)
#         d[a] = i
#     return d


# print(str_counter(["Helloo","olmaawdwd","salom","olma"]))


# 26-masala
# name=input("Komanda nomini kiriting:")
# age=input("Natijani yozing:")
# if  age=="Yutdi" or age=="yutdi":
#     print("Tabriklaymiz!!")
# else:
#     print("Afsusdamiz!!")

# 25-masala
# name=input("Kitob nomini kiriting:")
# if len(name)>0:
#     print("Kitob ugan man")
# else:
#     print("Kitob uqimagan man !")

# 24-masala
# count=int(input("Bajargan ishingizni sonni :"))
# if count>=5:
#     print("Yaxshi natija !!")
# else:
#     print("Yomon natija !!")


# 23-masala
# reja=input("Reja kiriting:")
# if len(reja)>0:
#     print("Sayohatga chiqamziz !!")
# else:
#     print("Sayohatga chiqmaymiz !!")


# 22-masala
# vazn = float(input("Vazningizni kiriting (kg): "))
# boy = float(input("Bo'yingizni kiriting (m): "))

# bmi = vazn / (boy ** 2)

# print(f"Sizning BMI ko'rsatkichingiz: {bmi:.2f}")

# if bmi < 18.5:
#     print("Siz ozg'insiz. Sog'lig'ingizni yaxshilash uchun ovqatlanishni muvozanatlang.")
# elif 18.5 <= bmi < 24.9:
#     print("Sizning vazningiz me'yorida.")
# elif 25 <= bmi < 29.9:
#     print("Sizda ortiqcha vazn bor. Sog'lom turmush tarzini olib borishga harakat qiling.")
# else:
#     print("Sizda semizlik mavjud. Sog'lig'ingizni yaxshilash uchun shifokorga murojaat qiling.")


# 21-masala
# yosh = int(input("Yoshingizni kiriting: "))

# if 5 <= yosh <= 12:
#     print("Sizga mos sport turlari: gimnastika, suzish, futbol, basketbol.")
# elif 13 <= yosh <= 18:
#     print("Sizga mos sport turlari: futbol, voleybol, yengil atletika, basketbol, jang san'ati.")
# elif 19 <= yosh <= 40:
#     print("Sizga mos sport turlari: yugurish, tennis, suzish, fitnes, yoga.")
# elif yosh > 40:
#     print("Sizga mos sport turlari: yoga, yurish, suzish, velosport.")
# else:
#     print("Kechirasiz, yosh noto‘g‘ri kiritilgan.")


# 20 -masala
# salary=int(input("Maoshingizni kiriting:"))
# deposit=int(input("Qarz miqdorini kiriting:"))
# if salary>deposit:
#     print("Siz qarz berishingiz mumkin!!")
# else:
#     print("Sizga qarz berish mumkin emas!!")

# 19-masala
# while True:
#   passport=input("Parolingizni kiriting:")
#   if len(passport)>=8:
#     print("Parol muvaffaqiyatli qo'shildi")
#     break
#   else:
#     print("Parol 8 ta harf bilan boshlanishi kerak")

# 18-masala
# time=int(input("Vaqtni kiriting:"))
# if 5<=time and time <=16:
#     print("Hayrli kun")
# else:
#     print("Xayrli tun")

# 17-masala
# reyt=int(input("Reytingni kiriting:"))
# if reyt>=100:
#     print("Siz reytingni yangilashiz kerek !!!")
# else:
#     print("Yangilashga hali bor !!!")


# 16-masala
# age=int(input(" Yoshini kiriting:"))
# jins=input("Jinsni kiriting:")
# if age>=10 and jins=="Erkak"  or jins=="erkak":
#     print("Siz telefon sovg'a qilishingiz mukin")
# elif age>=10 and jins=="Ayol" or jins=="ayol":
#     print("Siz gul sovg'a qilishingiz mukin")

# 15-masala
# kilo=int(input("Kilometrni kiriting:"))
# age=int(input("Moshinani yoshini kiriting:"))
# if age>=10:
#     print("Ehtiyot qismlarni tekshiring !!")
# else:
#     print("Moshinangiz hali kup xizmat qiladi !!")


# 14-masala
# eat=input("Qaysi taomni aytasiz :")
# print("Taom qilinyapti :",eat)


# 13-masala
# num=int(input("Bahoni kiriting:"))
# num1=int(input("Bahoni kiriting:"))
# num2=int(input("Bahoni kiriting:"))
# if num==5 and num1==5 and num2==5:
#     print("A'lo")
# elif num==5 or num==4  and num1==5 and num2==4:
#     print("Yaxshi")
# elif num==5 or num==4 and num1==4 or num2==5 or num2==4:
#     print("Yaxshi")
# elif num==4 or num==3  and num1==3 or num2==3:
#     print("Yomon")
# 12-masala
# num=int(input("Oyninig raqamini kiriting:"))
# if num==1 or num==2 or num==12:
#     print("Qish")
# elif num==3 or num==4 or num==5:
#     print("Bahor")
# elif num==6 or num==7 or num==8:
#     print("Yoz")
# elif num==9 or num==10 or num==11:
#     print("Kuz")
# else:
#     print("[1:12] bulgan raqam kiritishingiz kerak !!")


# 11-masala
# cong=input("foizini kiriting:")
# if cong>="70%":
#     print("Sertifikat olishingiz mumkin ")
# else:
#     print("Sertifikat olishingiz mumkin emas")


# 10-masala
# card=input("Qaysi usulda tulov qilasz :")
# if card=="Karta"  or card=="karta":
#     print("Tulov uchun:",8600, 1235 ,2563 ,2589)
# else:
#     print("Tulov naqd berishingiz kerak !!")

# 9-masala
# wait=input("Ob havoni kiriting:")
# if wait=="qor"or wait=="Qor" and wait=="yomg'ir" or wait=="Yonmg'ir":
#     print("Kuylak kiyish tavsiya etilmaydi !!")
# else:
#     print("Kuylak kiyish tavsiya etildi !!")

# 8-masala
# age=int(input("Enter your age: "))
# if age>=18:
#     print("Kattalar")
# else:
#     print("Bolalar")


# 7-masala
# frand=int(input("Enter number: "))

# if 80<=frand and frand<=89:
#     print("A")
# elif 70 <=frand and frand<=79:
#     print("B")
# elif 60 <=frand and frand<=69:
#     print("C")
# elif 60 >frand :
#     print("F")
