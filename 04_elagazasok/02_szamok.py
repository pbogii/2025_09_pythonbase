"""Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""
szamegy = float(input("Kérlek adj meg egy számot!"))
szamketto = float(input("Kérlek adj meg mégegyet!"))
szamharom = float(input("Kérlek mégegyet!"))

if szamegy > szamketto and szamegy > szamharom:
    print(f"A legnagyobb: {szamegy}")
elif szamketto > szamegy and szamketto > szamharom:
    print(f"A legnagyobb: {szamketto}")
elif szamharom > szamegy and szamharom > szamketto:
    print(f"A legnagyobb: {szamharom}")
else:
    print("Ugyan akkorák!")