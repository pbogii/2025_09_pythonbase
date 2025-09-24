""" Feladat
 A program a pénzfeldobást modellezi. 
 Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!"""

fej = 1
iras = 2

lekeres = (input("Fej vagy Írás?"))

import random
random_szam = random.randint(1, 2)

if random_szam == fej:
    print("Fej")

else :
    print("Írás")