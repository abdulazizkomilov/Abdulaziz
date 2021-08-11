#print("  Sizga kerak mahsulotlar ro'yxatini tuzing. \n")
#mahsulotlar = []
#ask = True
#n = 1
#while ask:
#	mahsulot = input(f"  {n} mahsulot nomini kiriting:  ")
#	mahsulotlar.append(mahsulot.capitalize())
#	print(f"  Mahsulotlar ro'yxati {mahsulotlar}")
#	quit = input('  Davom etish uchun "again" deb yozing yoki tugatish uchun "stop" \n  deb yozing:  ')
#	n += 1
#	if quit == "stop":
#		ask = False
#print(f"  {mahsulotlar}")


# print("  Sizning mahsulotlaringiz ro'yxatini tuzing. \n")
# mahsulotlar = {}
# s = True
# n = 1
# while s:
#  	mahsulot = input(f"  {n} mahsulot nomini kiriting:  ")
#  	mahn = input(f"   {mahsulot.capitalize()} narxini kiriting:  ")
#  	mahsulotlar[mahsulot] = int(mahn)
#  	quits = input("Dasturni davom ittirasizmi (ha/yuq)")
#  	n += 1
#  	if quits == "stop":
#          s = False
# for mah, narx in mahsulotlar.items():
#  	print(f"  {mah.title()}ning narxi {narx} so'm")
    
# print("  Sizning mahsulotlaringiz ro'yxatini tuzing. \n")
# mahsulotlar = {}
# s = True
# n = 1
# while s:
#  	mahsulot = input(f"  {n} mahsulot nomini kiriting:  ")
#  	mahn = input(f"   {mahsulot.capitalize()} narxini kiriting:  ")
#  	mahsulotlar[mahsulot] = int(mahn)
#  	quits = input("Dasturni davom ittirasizmi (ha/yuq)")
#  	n += 1
#  	if quits == "yuq":
#           s = False
# for mah, narx in mahsulotlar.items():
#  	print(f"  {mah.title()}ning narxi {narx} so'm")


# print("  Sizga kerak mahsulotlar ro'yxatini tuzing. \n")
# buyirtma = ["olma", "sut", "sabzi"]
# ask = True
# n = 1
# while ask:
# 	mahsulotd = input(f"  {n} mahsulot nomini kiriting:  ")
#  	if mahsulotd in buyirtma.index(2):
#          print(mahsulotlar[mahsulotds])
# 	quita = input("Dasturni davom ittirasizmi (ha/yuq)")
# 	n += 1
# 	if quita == "yuq":
# 		ask = False


mahsulot = input("Sizga kerak mahsulot nomini kiriting:  ")
mahsulotlar = {'olma':20000,
                'shaftoli':25000,
                'tarvuz':18000,
                'uzum':22000}

a = 1
while a < 2:
    if mahsulot in mahsulotlar.keys():
        narh = mahsulotlar[mahsulot]
        print(f"{mahsulot.title()} - {narh} so'm")
        a += 1
    else:
        print(f"Bizda {mahsulot} yo'q")