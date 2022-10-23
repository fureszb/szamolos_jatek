def osszead():
    from random import seed
    from random import randint
    import os
    seed(1)
    a = int(input("Hány feladatot szeretnél?: "))
    print("Miyen tartományban szeretnél számokat?: ")
    intervallumkez = int(input("Kezdő érték: "))
    intervallumveg = int(input("Vég érték: "))
    os.system('cls')
    for x in range(1,a+1):
        rnd1 = randint(intervallumkez, intervallumveg)
        print(str(x) + ". ",rnd1, "+",end=" ")
        rnd2 = randint(intervallumkez, intervallumveg)
        print(rnd2,"= ",end="")
        eredmeny = int(input())
        if(eredmeny != rnd1+rnd2):
            print("A válaszod helytelen!")
