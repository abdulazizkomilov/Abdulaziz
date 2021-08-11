# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:26:26 2021

@author: Abdulaziz
"""

oila = {"dadam" : "sobirjon ashurov", "yosh" : "1977", "tugulgan" : "samarqand viloyati"}
print(f"Dadam {oila['dadam'].title()} {oila['yosh']} - yil {oila['tugulgan'].capitalize()} tug`ulan")
print(' ')
taomlar = {"birinchi" : "osh", "ikkinchi" : "shurva", "uchinchi" : "kabob", "to`rtinchi" : "somsa", "beshinch" : "lag`mon"}
ismlar = {1 : "Ali", 2 : "Vali", 3 : "Nodir", 4 : "Miraziz", 5 : "Nurali"}
print(f"""{ismlar[1]}ning sevimli taomi {taomlar['birinchi']} \n
{ismlar[2]}ning sevimli taomi {taomlar['ikkinchi']} \n
{ismlar[3]}ning sevimli taomi {taomlar['uchinchi']}"""), "\n"
python = {"integir" : "buiymatlarni o`nli kasr typiga tegishli kanligini bildiradi",
           "boolen" : "True or False ekanligini ko`rsatadi",
           "title" : "matndagi har bir so`zni bosh harfini katta qiladi",
           "lower" : "barcha harfni k qiymatlarni butun sonlar typiga tegishliligini ko`rsatadi",
           "string" : "bu qiymatlarni matn typiga tegishli ekanligini bildiradi",
           "float" : "bu qichik qiladi",
           "upper" : "barcha harfni katta qiladi",
           "capitalize" : "matn boshidagi harfni katta qiladi",
           "if" : "agar",
           "elif" : "aks holda agar",
           "else" : "aks holda"}
print(python), "\n"


# question = input("Kalit so`z kiriting: ")
# if question.lower() == "integir":
#     print(python["integir"])
# elif question.lower() == "string":
#     print(python["string"])
# else:
#     print("Bunday kalit so`z yuq")
# print(" ")

question = input("Kalit so`z kiriting: ").lower()
# print(python.get(question, "Bunday kalit so`z yuq"))
print(python.get(question)), "\n"



