# Autore: Gnavi Alex

# Azienda: Max Cambi

# data: 23/01/2024

# Nome progetto: Golden Golf Tutor

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
# Configurazione del modulo di logging
logging.basicConfig(filename='data_set.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

while True:
    try:
        file_path = input("Inserisci il percorso del file (digita 'exit' per uscire): ")

        if file_path.lower() == 'exit':
            print("Programma chiuso.")
            break  # Esce dal loop
        #creo il dataset
        data = pd.read_csv(file_path)

        print(data)
        logging.info("lettura csv corretta")
        logging.info(data.info())

    except FileNotFoundError as e:
        print(f"Errore: {e} - File non trovato.")
        logging.error(f"Errore: {e} - File non trovato.")
    except DeprecationWarning as e:
        print(e)
        logging.error(e)
    except pd.errors.EmptyDataError as e:
        print(f"Errore: {e} - Il file CSV è vuoto.")
        logging.error(f"Errore: {e} - Il file CSV è vuoto.")
    except pd.errors.ParserError as e:
        print(f"Errore: {e} - Errore durante la lettura del file CSV.")
        logging.error(f"Errore: {e} - Errore durante la lettura del file CSV.")
    except Exception as e:
        print(f"Errore: {e}")
        logging.error(f"Errore: {e}")