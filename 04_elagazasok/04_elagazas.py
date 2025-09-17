"""Szamok pzitiv negativ float nem float"""
# szam = float(input("Adj meg egy számot!"))
# if szam < 0 :
#     print("Ez a szám negatív!")
# elif szam == 0 :
#     print("Ez a szám nulla!")
# else :
#     print("Ez a szám pozitív!")

# if szam.is_integer():
#     print("Ez egy egész szám.")
# else:
#     print("Ez nem egész szám.")
    
szam = int(input("Adj meg egy számot!"))

if szam % 2== 0 and szam !=0:
    print("Páros")
elif szam == 0 :
    print("Nulla")
else :
    print("Páratlan")
