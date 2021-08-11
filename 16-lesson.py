# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:11:44 2021

@author: Abdulaziz
"""

shoirlar = {
    "alisher" : {"familya" : "naviy",
                 "tyil" : "1441",
                 "tjoy" : "buxora",
                 "vyil" : "1501",
                 "asarlar" : ["o`tkan kunlar",
                              "mehrabdan chayon",
                              "obid ketmon"]},
    "abdulla" : {"familya" : "qodiriy",
                 "tyil" : "1894",
                 "tjoy" : "toshkent",
                 "vyil" : "1934",
                 "asarlar" : ["tong nafasi",
                              "o`zbegim", "qo`shiqlarim sizga"]},
    "erkin" : {"familya" : "voxidov",
               "tyil" : "1936",
               "tjoy" : "xirot",
               "vyil" : "2016",
               "asarlar" : ["xamsa", "mahbub al-qulub",
                            "lison ut-tayr"]}
    }


for ism, info in shoirlar.items():
    print(f"{ism.title()} {info['familya'].title()} {info['tyil']}-yil {info['tjoy'].title()} da tug`ulgan, {info['vyil']}yil vafot etgan")
    for asar in info['asarlar']:
        print(f"{asar.title()}")
    print(" ")


kitoblar = {
    "ali" : {['terminator', 'rambo', 'titanic']},
    "vali" : {['tenet', 'inception', 'inertellar']},
    "hasan" : {['abdullajon', 'bomba', 'shaytanat']}
    }

for ism , an in kitoblar.items():
    print(f"{ism.title()}ning sevimli kitobi: ")
    for a in an:
        print(f"{a.title()}")