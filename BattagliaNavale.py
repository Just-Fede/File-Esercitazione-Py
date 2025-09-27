import random
import os
import time

COST_NAVI = random.randint(1,5)
COST_MAX_COLPI = COST_NAVI*3
PUNTI = 0

CAMPO = [[0 for _ in range(5)] for _ in range(5)]

# 0 = nulla
# 1 = nave
# 2 = colpo a vuoto
# 3 = nave colpita

def CaricamentoFigo():

    os.system("cls")
    print("\n> Caricamento Battaglia Navale . . .\n")

    for i in range(1,21):

        BARRA = "#" * i + "-" * (20-i)
        PERCENTUALE = i * 5
        print(BARRA + " " + str(PERCENTUALE) + "%",end="\r")

        time.sleep(0.1)

    print("\n\n> Caricamento Completato!")
    time.sleep(2)
    os.system("cls")

def CreaNavi(x:int):
    for i in range(x):
        CAMPO[random.randint(0, 4)][random.randint(0, 4)] = 1

def PrintMappa():
    print("   1  2  3  4  5")
    for x in range(5):
        print(x+1,end=" ")
        for y in range(5):
            if CAMPO[x][y] == 0:
                print("[-]", end="")

            if CAMPO[x][y] == 1:
                print("[X]", end="")

            if CAMPO[x][y] == 2:
                print("[M]", end="")

            if CAMPO[x][y] == 3:
                print("[H]", end="")
        print("")

def Spara(x,y):
    global PUNTI
    os.system('cls')
    print("Spari in [" + str(SparoX+1) + "-" + str(SparoY+1) + "]")

    if CAMPO[x][y] == 0:
        print("[Hai mancato!]\n")
        CAMPO[x][y] = 2

    elif CAMPO[x][y] == 1:
        print("[Hai colpito!]\n")
        PUNTI = PUNTI+1
        CAMPO[x][y] = 3
    
    PrintMappa()

#############################################################################
VITTORIA = False
SCONFITTA = False

COLPI = 0

os.system('cls')

CaricamentoFigo()

CreaNavi(COST_NAVI)
PrintMappa()

while not (VITTORIA or SCONFITTA):
    print("\nColpi (" + str(COLPI) + " / " + str(COST_MAX_COLPI) + " )")
    COLPI = COLPI+1

    SparoX = int(input("Scegli la X dove sparare > "))-1
    SparoY = int(input("Scegli la Y dove sparare > "))-1

    Spara(SparoY,SparoX)

    if PUNTI == COST_NAVI:
        os.system('cls')
        print("[ --- HAI AFFONDATO TUTTI I NEMICI! --- ]")
        VITTORIA = True

    if COLPI >= COST_MAX_COLPI:
        os.system('cls')
        print("[ --- HAI FINITO TUTTI I COLPI --- ]")
        SCONFITTA = True

input("\nPremi qualsiasi tasto per chiudere...")
