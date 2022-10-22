import osztas
import szorzas

print("[1] Összeadás")
print("[2] Kivonás")
print("[3] Szorzás")
print("[4] Osztás")
val = int(input("Melyik jatekkal akarsz játszani?: "))
while (val<1) | (val>4):
    print("NINCS ilyen számú játék! \n Kérek Válasz újat!")
    print("[1] Összeadás")
    print("[2] Kivonás")
    print("[3] Szorzás")
    print("[4] Osztás")
    val = int(input("Melyik jatekkal akarsz játszani?: "))

import osszeadas
import kivonas
import valasztas

if(val == 1):
    osszeadas.osszead()
if (val==2):
    kivonas.kivonas()
if (val == 3):
        szorzas.szorzas()
if (val == 4):
        osztas.osztas()

print("A játék végetért!!")
valasz = input("Akarsz új játékot indítani['igen' vagy 'nem']?: ")
while (str(valasz) == "igen"):
    print()
    valasztas.valasztas()
    if (val == 1):
        osszeadas.osszead()
    if (val == 2):
        kivonas.kivonas()
    if (val == 3):
        szorzas.szorzas()
    if (val == 4):
        osztas.osztas()
    print("A játék végetért!!")
    valasz = input("Akarsz új játékot indítani[igen' vagy 'nem']?: ")
print("A játék kilép")