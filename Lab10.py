import pandas as pd
import os
os.system('cls')

DF = pd.read_csv('persone.csv')

print(DF.head(5))
print("\n---------------------------------------------------------")


print(DF.describe())
print("\n---------------------------------------------------------")


print(DF['Mondo'].value_counts())
print("\n---------------------------------------------------------")
print(DF['Ruolo'].value_counts())
print("\n---------------------------------------------------------")

DF['Buono'] = (DF['Ruolo']!='Antagonista')
print(DF)
print(DF['Buono'].value_counts())

print("\n---------------------------------------------------------")
DF.rename(columns={'AnnoNascita':'Anno Di Nascita'},inplace=True)
DF['Eta'] = (2025 - DF['Anno Di Nascita'])
print(DF)

print("\n---------------------------------------------------------")
DF = DF.sort_values('Eta', ascending=True)
print(DF)

print("Ho trovato dei Bilbo")
print(DF[DF['Nome']=='Bilbo'])
print("\n---------------------------------------------------------")
print("In totale sono " + str((DF['Nome']=='Bilbo').sum()))
print(DF.sort_values('Nome',ascending=True))

print("\n---------------------------------------------------------")
print(DF['Nome'].describe())
print(DF['Cognome'].describe())