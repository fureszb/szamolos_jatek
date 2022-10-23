def kivonas():
    from random import seed
    from random import randint
    import os
    seed(1)
    kivonas=0
    a = int(input("Hány feladatot szeretnél?: "))
    os.system('cls')
    for x in range(1,a+1):
        rnd1 = randint(0, 10)
        print(str(x) + ". ",rnd1, "-",end=" ")
        rnd2 = randint(0, 10)
        print(rnd2,"= ",end="")
        eredmeny = int(input())
        if(eredmeny != rnd1-rnd2):
            print("A válaszod helytelen!")