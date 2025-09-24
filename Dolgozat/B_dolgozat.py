"""B csoport:
Készítsünk programot, amely segíti a burkoló mesterek munkáját.
A szükséges csempe mennyiségének a kiszámításához a program kérje be a terület szélességét és a magasságát centiméterben, #kesz
valamint, hogy hány darab csempét vásároltunk már, majd számolja ki a területét (a*b), és
hogy a 20cm*20cm méretű csempék esetén hány darabra van szükség a munka elvégzéséhez (a plusz 10%-ot az illesztések miatt illik rászámolnunk).
A program azt is állapítsa meg, és közölje a felhasználóval, hogy kell-e még vásárolnunk csempét!
"""

szelesseg = int(input("Kérlek írd be a szélességet ! :"))
magassag = int(input("Kérlek írd be a magasságot ! :"))
csempe = int(input("Kérlek írd be a már megvásárolt csempék számát! :"))

terulet = szelesseg * magassag
csempe_allando = 20 * 20 


csempe_kell = terulet / csempe_allando * 1.1

# print (f"{csempe_kell}")

if csempe >= csempe_kell :
    print ("Elég csempéd van!")

else :
    print ("Nincs elég csempéd!")


