"""Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""

jelszo = "titok"

input("Kérlek adj meg egy jeszót: ")
if input == jelszo:
    print("Belépés engedélyezve!")
else:
    print("Helytelen jelszó!")