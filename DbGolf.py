# Autore: Gnavi Alex

# Azienda: Max Cambi

# data: 23/01/2024

# metodologia di lavoro: Design pattern

# Nome progetto: Golden Golf Tutor

import mysql.connector
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import logging

# Configurazione del modulo di logging
logging.basicConfig(filename='MWdb.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="golfclub",
    database="golfclub"  # Specifico il database da utilizzare
    )

    mycursor = mydb.cursor()
    logging.info(mycursor)
except Exception as e:
    print("error connection")
    logging.warning(e)
    
    
while True:
    # opzioni disponibili
    print("Menu:")
    print("1. Select")
    print("2. Insert")
    print("3. Delete")
    print("4. Modified points")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    # mostro i dati
    logging.info(f"option: {choice}")
    if choice == "1":
        mycursor.execute("SELECT * FROM partecipanti")
      
        myresult = mycursor.fetchall()
        if not myresult:
            print("No data available.")
        else:
            #utilizzo la libreria table per vedere i record  in tabella
            table = PrettyTable()
            table.field_names = ["ID", "nome","cognome","regione_provenienza","circolo_provenienza","categoria","ultimo_torneo_partecipato","punti"]
            for row in myresult:
                table.add_row(row)

            print(table)
    # inserisco i dati
    elif choice == "2":
      
        try:
            name=input("insert the name: ")
            surname=input("insert the surname: ")
            region=input("insert the region: ")
            circle=input("insert the from circle: ")
            categories=input("insert the categories: ")
            tournament=input("enter last tournament: ")
            points=input("insert the point: ")

            sql = "INSERT INTO partecipanti (nome,cognome,regione_provenienza,circolo_provenienza,categoria,ultimo_torneo_partecipato,punti) VALUES (%s, %s, %s, %s,%s,%s,%s);"
            val = (name,surname,region,circle,categories,tournament,points)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            logging.warning("error"+str( e))
    # elimino i dati
    elif choice == "3":
        try:
            id_to_delete = input("Enter the ID to delete: ")
            sql_delete = "DELETE FROM partecipanti WHERE ID = %s"
            val_delete = (id_to_delete,)
            mycursor.execute(sql_delete, val_delete)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted.")
        except Exception as e:
            logging.warning("error" + str(e))
    # aggiorno i punteggi
    elif choice == "4":
        try:
            print("Update Record Menu:")
            print(" Update Points")
            print(" Update Circle")
            

            update_choice = input("Enter your choice : ")

            if update_choice == "Update Points":
                surname_to_update = input("Enter the surname to update points: ")
                new_points = input("Enter the new points: ")

                sql_update = "UPDATE partecipanti SET punti = %s WHERE cognome = %s"
                val_update = (new_points, surname_to_update)

                mycursor.execute(sql_update, val_update)
                mydb.commit()

                print(mycursor.rowcount, "record(s) updated.")
            elif update_choice == "Circle":
                surname_to_update=input("Enter the surname to update circle:")
                new_circle_update=input("enter the new circle: ")
                sql_update = "UPDATE partecipanti SET circolo_provenienza = %s WHERE cognome = %s"
                val_update = (new_circle_update, surname_to_update)

                mycursor.execute(sql_update, val_update)
                mydb.commit()
                print(mycursor.rowcount, "record(s) updated.")
            else:
             print("Invalid choice. Please select a valid option.")
        except Exception as e:
           logging.warning("error" + str(e))
    # chiudo i programmi
    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
        logging.error(f"{choice} Invalid choice. Please select a valid option. ")

