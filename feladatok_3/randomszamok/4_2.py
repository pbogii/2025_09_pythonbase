""" Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, 
szintén ebbe a tartományba eső számmal! 
Az összehasonlítás eredményéről tájékoztassa a felhasználót!"""

lekert_szam = int(input("Adj meg egy számor 1 és 3 között!"))

import random
random_szam = random.randint(1, 3)

if lekert_szam == random_szam:
    print ("Eltaláltad! Erre gondoltam!")

else :
    print ("Nem erre gondoltam.")

