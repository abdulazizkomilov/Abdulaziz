# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:35:00 2021

@author: Abdulaziz
"""

belad = {"As-Saudia", "Misr", "USA", "UK", "Uzbekistan"}
print(belad)
print("  ")
print("These are countries length:  ", len(belad))
print("  ")
print(sorted(belad))
print("  ")
print(sorted(belad, reverse=True))
print("  ")
a = list(range(120, 1201, 2))
print(a)
print("  ")
b = sum(a)
print(b)
c = max(a) -  min(a)
print(c)
print("  ")
print(len(a))
print("  ")
ab = list(range(199, 1201))
print("20 from the beginning:  ", ab[:21])
print("  ")
print("20 from the finishing:  ", ab[-20:])
print("  ")
print("20 from the middling:  ", ab[530:550])
print("  ")
foods = ["somsa", "kabob", "lavash", "osh", "kushare"]
print(foods)
breakfast = foods[:]
print(breakfast)
new_breakfast = [foods[2], foods.pop(4), "milk", "soap"]
print(new_breakfast)
