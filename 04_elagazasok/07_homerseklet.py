"""Hőmérséklet tanács
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
0 alatt: „Nagyon hideg, öltözz melegen!”
0–20: „Hűvös, kabát ajánlott.”
21–30: „Kellemes idő.”
30 felett: „Forróság, igyál sok vizet!”
"""

homerseklet = int(input("Kérlek adj meg egy hőmérsékletet! (celsiusban)"))

if homerseklet < 0:
    print("Nagyon hideg, öltözz melegen!")
elif 0 <= homerseklet <=20:
    print("Hűvös, kabát ajánlott.")
elif 21 <= homerseklet <= 30 :
    print("Kellemes idő.")
elif 30<= homerseklet:
    print("Forróság, igyál sok vizet!")


