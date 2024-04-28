import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import mysql.connector
import logging
import matplotlib.pyplot as plt

# Connessione al database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="golfclub"  # Specifico il database da utilizzare
    )
    mycursor = mydb.cursor()
except Exception as e:
    logging.warning("Errore nella connessione al database: " + str(e))


# Estrai i dati dal database
try:
    mycursor.execute("SELECT id, nome, punti_totali, punti_classifica_parziale FROM partecipanti")
    myresult = mycursor.fetchall()

    if not myresult:
        print("Nessun dato disponibile per l'addestramento del modello.")
    else:
        # Creazione di un DataFrame pandas con i dati estratti dal database
        df = pd.DataFrame(myresult, columns=['id', 'nome', 'punti_totali', 'punti_classifica_parziale'])

        # Ordina il DataFrame per punteggio totale e classifica parziale
        df_sorted = df.sort_values(by=['punti_totali', 'punti_classifica_parziale'], ascending=[False, False])

        # Seleziona il miglior giocatore
        best_player = df_sorted.iloc[0]

        # Stampa il miglior giocatore
        print(f"Il miglior giocatore è il giocatore {best_player['nome']} con ID {best_player['id']}.")

except Exception as e:
    logging.warning("Errore nell'estrazione dei dati dal database: " + str(e))
finally:
    # Chiudi la connessione al database alla fine
    mycursor.close()
    mydb.close()

