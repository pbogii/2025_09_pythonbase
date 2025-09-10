"""Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!"""

print("Enter a radius: ") # lekérek a felhasználótól egyrádiusz értéket
radius = int(input())  # radius erteke cm ben
PI = 3.14 # pi erteke
circle_ker = PI * radius * 2 # szamitasok6
circle_ter = PI * radius * radius
print (f"A kör kerülete : {circle_ker} cm") #valaszok
print (f"A kör területe : {circle_ter} cm2") 

