# Import delle librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system('cls')

# Caricamento del dataset
df = pd.read_csv("dataset_film.csv")

def Esercizio01():
    print("------------------------------------ Primi 5 elementi ------------------------------------")
    print(df.head(5))

    print("\n------------------------------------ Ultimi 5 elementi ------------------------------------")
    print(df.tail(5))

    print("\n------------------------------------ Informazioni Utili ------------------------------------")

    print("\nLa tabella è " + str(df.shape))

    print("\nLa tabella è composta: \n" + str(df.dtypes))

    print("\nInformazioni su anno e durata: \n" + str(df[['Anno','Durata_min']].describe()))

    print("\nInformazioni generali: \n")
    df.info()

def Esercizio02():
    print("\n------------------------------------ Titolo & Anno ------------------------------------\n")
    print(df[["Titolo","Anno"]])

    print("\n------------------------------------ Film di Nolan ------------------------------------\n")
    print(df[df["Regista"] == "Christopher Nolan"])

    print("\n------------------------------------ Film dopo il 2010 ------------------------------------\n")
    print(df[df["Anno"] >= 2010])

    print("\n------------------------------------ Film Americani maggiori di 150 min ------------------------------------\n")
    print(df[(df["Durata_min"] >= 150) & (df["StatoProduzione"] == "USA")])

def Esercizio03():
    df["Decennio"] = (df["Anno"] // 10 ) * 10
    df["FilmLungo"] = (df["Durata_min"] >= 150)
    
    df["Coppia"] = df["AttorePrincipaleMaschile"].astype(str) + " & " + df["AttricePrincipaleFemminile"].astype(str)
    newDF = pd
    newDF = df.drop(["AttorePrincipaleMaschile","AttricePrincipaleFemminile"], axis = 1)

    newDF = newDF.sort_values(['Anno','Durata_min'], ascending=True)

    print(newDF)

def Esercizio04():
    print("Durata Media: " + str(df["Durata_min"].mean()))
    print("\nDurata Media Per " + str(df.groupby("StatoProduzione")["Durata_min"].mean()))

    print("\nRegista con maggiori film: \n" + str(df.groupby('Regista').size().sort_values(ascending=False).head(1)))

    newDF = df.groupby("Decennio")["Durata_min"].mean()
    print(newDF)

def Esercizio05():
    # Raggruppa i film per regista e conta quanti film ha ciascuno
    conteggio_film = df.groupby("Regista").size()

    # Grafico a barre
    conteggio_film.plot(kind="bar", figsize=(10,5), color="skyblue")

    plt.title("Numero di film per Regista")
    plt.xlabel("Regista")
    plt.ylabel("Numero di film")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # per evitare taglio delle etichette
    plt.show()
    
    plt.figure(figsize=(8,5))
    plt.hist(df["Durata_min"], bins=15, color="skyblue", edgecolor="black")
    plt.title("Distribuzione delle Durate dei Film")
    plt.xlabel("Durata (minuti)")
    plt.ylabel("Numero di film")
    plt.show()

    plt.figure(figsize=(10,5))
    df.boxplot(column="Durata_min", by="StatoProduzione", grid=False, patch_artist=True)
    plt.title("Durata dei Film per Stato di Produzione")
    plt.suptitle("")  # rimuove il titolo automatico di pandas
    plt.xlabel("Stato di Produzione")
    plt.ylabel("Durata (minuti)")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(8,5))
    plt.scatter(df["Anno"], df["Durata_min"], color="green", alpha=0.6)
    plt.title("Anno vs Durata dei Film")
    plt.xlabel("Anno")
    plt.ylabel("Durata (minuti)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

        
##########################################################################################

def main():
    #Esercizio01()
    #Esercizio02()
    #Esercizio03()
    #Esercizio04()
    Esercizio05()

main()