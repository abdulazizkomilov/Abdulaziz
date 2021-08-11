# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:13:15 2021

@author: Abdulaziz
"""

# a = "Yaxshi ko`rgan kitobingizni nomini kiriting: \n"
# a += "[dasuni tugatish uchun 'exit' deb yozing \n >>> "
# while True:
#     qiymat = input(a)
#     if qiymat == 'exit':
#         break
#     else:
#         print(qiymat)
# print(" ")

yosh = "Yoshingizni kiriting \n"
yosh += "(Dasturdan chiqish uchun 'exit' yoki 'quit' deb yozing) \n"

while True:
    savol = input(yosh)
    if savol == "exit" or "quit":
        break
    else:
        
        s = int(savol)
    
        if 7 >= s:
            print("Sizga bilet narxi 2000 so`m")
        elif 7 < s and 18 > s:
            print("Sizga bilet narxi 3000 so`m")
        elif 18 < s and 65 > s:
            print("Sizga bilet narxi 10000 so`m")
        elif 65 < s:
            print("Siz muziyimizni bepul tomosha qiling!")
print("Dastur tugadi!\n") 