import os
import random

#Esercizio 1: data in input una sequenza di 8 valori che rappresentano le temperature rilevate durante un giorno, cacolare l'escursione termica.

def escursione_termica(temperature):

    tempMax = temperature[0]
    tempMin = temperature[0]

    for t in temperature:
        if t > tempMax:
            tempMax = t
            
        if t < tempMin:
            tempMin = t
    
    return tempMax - tempMin

#### Esercizio 2: data in input una sequenza di numeri, calcolare la somma dei numeri pari.

def numeri_Pari(numeri):

    cont = 0

    for i in numeri:
        if i%2 == 0:
            cont = cont+1

    return cont

#### Esercizio 3: Verificare se un numero è primo: 1) scrivere una funzione che pernde in input un numero intero n e resitutisce vero se n è primo, falso altrimenti. 2) Verificare con la lista di numeri numeri_test = [1, 2, 3, 4, 5, 17, 25, 29, 97, 100, 101]

def is_Primo(numero):

    if numero == 1:
        return False
    
    for i in range(2,numero-1):
        if numero % i == 0:
            return False
        
    return True

######################### MAIN #########################
os.system("cls")

print("--- Esercizio 1 ---")

temperature_Registrate = [0]*8

for i in range(8):
    temperature_Registrate[i] = random.randint(20,36)

print("Temperature Registrate " + str(temperature_Registrate))

print("Escursiote termica [ " + str(escursione_termica(temperature_Registrate)) + " ]")

print(" \n--- Esercizio 2 --- ")

numeri = [0]*random.randint(1,50)

for i in range(len(numeri)):
    numeri[i] = random.randint(1,100)

print("Serie casuale di numeri casuali " + str(numeri))
print("Contiene " + str(numeri_Pari(numeri)) + " numeri pari su " + str(len(numeri)) + " numeri")

print(" \n--- Esercizio 3 --- ")

numeri = [0]*random.randint(1,50)

for i in range(len(numeri)):
    numeri[i] = random.randint(1,1000)

print("Data la serie di numeri " + str(numeri))

for i in range(len(numeri)):
    if is_Primo(numeri[i]):
        print("[ "+ str(numeri[i]) +" ] è primo")