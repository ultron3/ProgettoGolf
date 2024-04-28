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
        # Estrai gli ID, nomi e punteggi come liste separate
        player_ids = [result[0] for result in myresult]
        player_names = [result[1] for result in myresult]
        scores_str = [result[2] for result in myresult]
        partial_scores = [result[3] for result in myresult]

        # Converti i punteggi in numeri
        scores = pd.to_numeric(scores_str, errors='coerce')

        # Considera un'ipotetica feature aggiuntiva (ad esempio, l'ID del giocatore)
        # Nel caso in cui hai ulteriori feature, includile nel processo di addestramento.

        # Creazione di un'ipotetica lista di ID giocatori per scopi dimostrativi
        player_ids = list(range(1, len(scores) + 1))

        # Prepara i dati di input e output per il modello
        X = np.array(player_ids).reshape(-1, 1)  # Input feature (potrebbe essere aggiunta l'età, esperienza, etc.)
        y = np.array(scores)  # Output (punteggi)

        # Divide i dati in set di addestramento e test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Standardizza i dati
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Costruzione del modello
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
            keras.layers.Dense(1)  # Output layer
        ])

        # Compila il modello
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Addestra il modello
        model.fit(X_train_scaled, y_train, epochs=50, batch_size=16, validation_data=(X_test_scaled, y_test))

        # Fai una predizione per tutti i giocatori
        all_players_scaled = scaler.transform(np.array(player_ids).reshape(-1, 1))
        predicted_scores = model.predict(all_players_scaled)

        # Calcola la differenza assoluta tra i punteggi reali e quelli previsti
        differences = np.abs(scores - predicted_scores.flatten())

        # Trova gli ID dei giocatori con la massima discrepanza
        improvement_candidate_ids = np.where(differences == np.max(differences))[0]

        for improvement_candidate_id in improvement_candidate_ids:
            improvement_candidate_name = player_names[improvement_candidate_id]
            improvement_candidate_score = scores[improvement_candidate_id]
            improvement_candidate_predicted_score = predicted_scores[improvement_candidate_id][0]
            print(f"Il miglior giocatore è il giocatore {improvement_candidate_name} con ID {improvement_candidate_id + 1}.")

        # Trova il giocatore con il punteggio previsto più alto
        best_player_id = np.argmax(predicted_scores)
        best_player_name = player_names[best_player_id]
        best_player_score = predicted_scores[best_player_id][0]

        # Visualizza un grafico dei punteggi previsti
        plt.scatter(player_ids, scores, label='Punteggi reali')
        plt.plot(player_ids, predicted_scores, color='red', label='Punteggi previsti')
        plt.xlabel('ID Giocatore')
        plt.ylabel('Punteggio')
        plt.title('Confronto tra Punteggi Reali e Punteggi Previsti')
        plt.legend()
        plt.show()

except Exception as e:
    logging.warning("Errore nell'estrazione dei dati dal database: " + str(e))
finally:
    # Chiudi la connessione al database alla fine
    mycursor.close()
    mydb.close()
