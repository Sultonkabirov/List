malumotlar=[
    {
    "name":"Abdulloh",
    "Yoshi":18,
    "Oyligi":"150$"
    },
    {
    "name":"Abdulboriy",
    "Yoshi":20,
    "Oyligi":"200$"
    },
    {
    "name":"Muhammad",
    "Yoshi":22,
    "Oyligi":"300$"
    },
    {
    "name":"Akmal",
    "Yoshi":25,
    "Oyligi":"350$"
    }
    ]
b=len(malumotlar)
a=0
for matn in malumotlar:
      if matn["Yoshi"]:
            a+=matn["Yoshi"]
# print(a/b)   
c=0
for matn1 in malumotlar:
    c+=int(matn1["Oyligi"].removesuffix("$"))    
print(c/b,a/b)

# matn = "Salom, dunyo!"
# yangi_matn = matn.replace("dunyo", "")
# print(yangi_matn)