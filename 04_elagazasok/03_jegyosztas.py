"""3️ Jegyosztályozás
Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
0–49: Elégtelen
50–64: Elégséges
65–79: Közepes
80–89: Jó
90–100: Jeles
"""
pont = int(input("Kérlek add meg a pontszámod! "))
if 90 <= pont <= 100:
    print("Jeles")
elif 80<= pont <=89:
    print("Jó")
elif 65<= pont <=79:
    print("Közepes")
elif 50<= pont <=64:
    print("Elégséges")
elif 0<= pont <=49:
    print("Elégtelen")
    