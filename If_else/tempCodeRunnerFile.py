# lst1=[1,2,3,4,5,6,7,8,9,10,20,30,40]
# s=[i**0.5
#     for i in lst1 if i%2==0 if i%5==0  ]
# print(s)
import math
numbers = list(range(1, 100))  # 1 dan 99 gacha bo'lgan sonlar

result = (
    [round(x**2.8 if x % 5 == 0 else x ** 3, 2) for x in numbers if x % 2 == 0 and (x**0.5 == int(x**0.5) or x % 5 != 0)]
)[-10:]
print(result)
result1=[]
for i in numbers:
    if i%2==0 and i**0.5==int(i**0.5) or i%5!=0:
        result1.append(round(i**2.8 if i % 5 == 0 else i ** 3, 2))
result1.sort()
print(result1)
   









# if str[i]==" ":
    #     s.append(c)
    #     c=" "
    # else:
    #     c+=str[i]








# def is_juft(num):
#     r=num
#     while True:
#         r=r/2
#         qol=r-int(r)
#         if qol==0:
#             return False
#         else:
#             return True

# tst =123456
# tst1=str(tst)
# count=[]
# for i in tst1:
#     if is_juft(i):
#       count.append(i)
# print(count)      
