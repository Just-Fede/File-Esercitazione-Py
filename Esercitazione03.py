import random
import os

####################################################################################################

def Esercizio01(lista):
    print("\n- Esercizio 01")
    lista[len(lista)-1] = 60
    lista[0] = 5
    print("La lista cotiene " + str(len(lista)) +" elementi")
    print(lista)

def indexOf(lista,valore):
    for i in range(len(lista)):
        if lista[i] == valore:
            return i

def Esercizio02(lista,verificaEsistenziale,conteggio,trova):
    print("\n- Esercizio 02")

    contatore = 0
    trovato1 = True
    trovato2 = True

    for s in lista:
        if(s == verificaEsistenziale and trovato1):
            print("Ho trovato " + str(verificaEsistenziale))
            trovato1 = False

        if(s == conteggio):
            contatore += 1
        
        if(s == trova and trovato2):
            print("Ho trovato " +str(trova) + " in posizione " + str(indexOf(lista,trova)+1) )
            trovato2 = False

    if(trovato1):
        print("Non ho trovato " +str(verificaEsistenziale))

    print("Ho contato " + str(contatore) + " volte l'elemento " + str(conteggio))

def Esercizio03(lista,daEliminare):
    print("\n- Esercizio 03")

    print("Elimino l'elemento " + str(daEliminare))
    lista.pop(indexOf(lista,daEliminare))

    print("Elimino il primo elemento")
    lista.pop(0)

    print("Elimino l'ultimo elemento")
    lista.pop()
    
    print("Lista dopo le modifiche" + str(lista))

def Esercizio04(lista,secondaLista):
    print("\n- Esercizio 04")

    print("Aggiungo a " + str(lista))
    print("La lista " + str(secondaLista))

    lista += secondaLista
    print("\nRisultato " + str(lista) +"\n")

    print("I primi 3 elementi sono " + str(lista[0:3]))
    print("Gli ultimi 2 elementi sono " + str(lista[len(lista)-2:]))
    print("Gli elementi dal secondo al quarto sono " + str(lista[1:4]))

def Esercizio05(lista):
    print("\n- Esercizio 05")

    lista.sort()
    print("Lista ordinata (CRE) " + str(lista))

    print("\nElemento più grande " + str(lista[len(lista)-1]))
    print("Elemento più piccolo " + str(lista[0]))

    lista.reverse()
    print("\nLista ordinata (DEC) " + str(lista))

def Esercizio06(lista,valore,daCercare):
    print("\n- Esercizio 06")

    lista.append(valore)
    print("Lista aggiornata " + str(lista))

    if daCercare in lista:
        print("Ho trovato " + str(daCercare))

    else:
        print("Non ho trovato " + str(daCercare))

    lista.sort()
    print("Riordino la lista " + str(lista))

####################################################################################################

numeri = [0]*random.randint(5,5)

for i in range(len(numeri)):
    numeri[i] = random.randint(1,100)

os.system("cls")

print(numeri)
Esercizio01(numeri)

Esercizio02(numeri,int(input("cosa verifico esista? > ")),int(input("cosa conto? > ")),int(input("cosa cerco? > ")))

Esercizio03(numeri,int(input("Cosa elimino? > ")))

numeriLaVendetta = [0]*random.randint(5,5)

for i in range(len(numeriLaVendetta)):
    numeriLaVendetta[i] = random.randint(1,100)

Esercizio04(numeri,numeriLaVendetta)

Esercizio05(numeri)

Esercizio06(numeri,int(input("Cosa aggiungo? > ")),int(input("Cosa cerco? > ")))

