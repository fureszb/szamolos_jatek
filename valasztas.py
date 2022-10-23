val = 0
def valasztas():
    import os
    from time import sleep
    print("[1] Összeadás")
    print("[2] Kivonás")
    print("[3] Szorzás")
    print("[4] Osztás")
    global val
    val = int(input("Melyik jatekkal akarsz játszani?: "))
    while (val < 1) | (val > 4):
        os.system('cls')
        print("NINCS ilyen számú játék! \n Kérek Válasz újat!")
        sleep(1)
        print()
        print("[1] Összeadás")
        print("[2] Kivonás")
        print("[3] Szorzás")
        print("[4] Osztás")
        val = int(input("Melyik jatekkal akarsz játszani?: "))