import mysql.connector
import matplotlib.pyplot as plt

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="golfclub",
        database="golfclub"
    )
    mycursor = mydb.cursor()
except Exception as e:
    print("Error connecting to the database:", e)
    exit()

try:
    mycursor.execute("SELECT nome, cognome, punti_classifica_principale FROM partecipanti")
    player_data = mycursor.fetchall()
except Exception as e:
    print("Error fetching player data:", e)
    exit()

if not player_data:
    print("No player data available.")
    exit()

# Converti i punteggi da VARCHAR a interi
converted_player_data = [(name, surname, int(points) if points.isdigit() else 0) for name, surname, points in player_data]

# Calcolo della media dei punteggi
scores = [score[2] for score in converted_player_data]
average_score = sum(scores) / len(scores) if scores else 0
print("Media dei punteggi:", average_score)

# Ordinamento dei giocatori in base ai punteggi
sorted_players = sorted(converted_player_data, key=lambda x: x[2], reverse=True)

# Visualizzazione dei migliori giocatori
print("\nTop 5 giocatori:")
for i, (name, surname, points) in enumerate(sorted_players[:5]):
    print(f"{i + 1}. {name} {surname}: {points} punti")

# Creazione di un grafico a barre per visualizzare i punteggi dei giocatori
names = [f"{name} {surname}" for name, surname, _ in sorted_players[:10]]
scores = [points for _, _, points in sorted_players[:10]]

# Specifica i colori per i primi e i secondi in classifica
colors = ['red' if i == 0 else 'yellow' if i == 1 else 'blue' for i in range(len(names))]

plt.bar(names, scores, color=colors)
plt.xlabel('Giocatori')
plt.ylabel('Punteggi')
plt.title('Punteggi dei giocatori')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

mydb.close()
