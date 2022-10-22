def valasztas():
    print("[1] Összeadás")
    print("[2] Kivonás")
    print("[3] Szorzás")
    print("[4] Osztás")
    val = int(input("Melyik jatekkal akarsz játszani?: "))
    while (val < 1) | (val > 4):
        print("NINCS ilyen számú játék! \n Kérek Válasz újat!")
        print("[1] Összeadás")
        print("[2] Kivonás")
        print("[3] Szorzás")
        print("[4] Osztás")
        val = int(input("Melyik jatekkal akarsz játszani?: "))