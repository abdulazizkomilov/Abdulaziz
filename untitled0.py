# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:42:24 2021

@author: Abdulaziz
"""

# d = {"Uzbekistan" : "Toshkint",
#      "AQSH" : "Washington D. C.",
#      "UK" : "London",
#      "Russia" : "Maskva",
#      "Germaniya" : "Berlin",
#      "Ispaniya" : "Madrid",
#      "China" : "Pekin"}


# country = input("Davlat nomini kiriting: ").lower()

# print(d.get(country))
python = {"uzbekistan" : "toshkint",
          "aqsh" : "washington d. c.",
          "uk" : "london",
          "russia" : "maskva",
          "germaniya" : "berlin",
          "ispaniya" : "madrid",
          "china" : "pekin"}

question = input("Kalit so`z kiriting: ").lower()

print(python.get(question))