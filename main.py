import osztas
import szorzas
import osszeadas
import kivonas
import valasztas
import os
from time import sleep

valasztas.valasztas()
sleep(1)
os.system('cls')
if(valasztas.val == 1):
    osszeadas.osszead()
if (valasztas.val==2):
    kivonas.kivonas()
if (valasztas.val == 3):
        szorzas.szorzas()
if (valasztas.val == 4):
        osztas.osztas()
sleep(1)
os.system('cls')
print("A játék végetért!!")
print()
sleep(1)
valasz = input("Akarsz új játékot indítani['igen' vagy 'nem']?: ")
os.system('cls')
while (str(valasz) == "igen"):
    print()

    valasztas.valasztas()

    if (valasztas.val == 1):
        osszeadas.osszead()
    if (valasztas.val == 2):
        kivonas.kivonas()
    if (valasztas.val == 3):
        szorzas.szorzas()
    if (valasztas.val == 4):
        osztas.osztas()
    sleep(1)
    os.system('cls')
    print("A játék végetért!!")
    sleep(1)
    valasz = input("Akarsz új játékot indítani[igen' vagy 'nem']?: ")
    os.system('cls')
print("Köszönjök hogy velünk játszottál! \nA játék kilép 3 másodpercen belül")
sleep(3)
exit(0)