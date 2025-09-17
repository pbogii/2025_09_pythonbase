""" Szökőév ellenőrző
Kérj be egy évet, és írd ki, hogy szökőév-e.
 (Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)
"""

ev = int(input("Kérlek adj meg egy évet! "))

if ev % 400 == 0:
    print("Ez egy szökőév!")
elif ev % 100 == 0:
    print("Ez nem szökőév!")
elif ev % 4 == 0:
    print("Ez egy szökőév!")
else:
    print("Ez nem szökőév!")