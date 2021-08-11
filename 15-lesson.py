# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:52:12 2021

@author: Abdulaziz
"""

keys = {"integir":"Butun son",
        "float":"O'nlik son",
        "if":"Biror amalni shart orqali tekshiradi",
        "string":"Matn",
        "else":"Boshqa biri 'yani shartdagi boshqa amalni bajaradi"}
for key, values in sorted(keys.items()):
    print(f"{key.title()} - {values.capitalize()}", ("\n"))
    
davlatlar = {"uzbekistan":"toshkint",
             "aqsh":"washington d. c.",
             "uk":"london",
             "russia":"maskva",
             "germaniya":"berlin",
             "ispaniya":"madrid",
             "china":"pekin"}

for k, q in sorted(davlatlar.items()):
    print(f"{k.title()}   {q.title()}")  
    
# for q in sorted(davlatlar.values()):
#     print(f"{q.title()}")

country = input("Davlat nomini kiriting: ").lower()

print(davlatlar.get(country))