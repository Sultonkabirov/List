str="Man Abdulloh man mdghsjgfu"
s=[]
c=""
for i in range(len(str)):
    if str[i].isalpha():
        c+=str[i]
    else:
        s.append(c)
        c=""
    if i==len(str)-1:
        s.append(c)


print(s)








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
