# Autore: Gnavi Alex

# Azienda: Max Cambi

# data: 23/01/2024

# Nome progetto: Golden Golf Tuor

import mysql.connector
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import logging
import boto3
# Configurazione del modulo di logging
logging.basicConfig(filename='MWdb.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Connessione al database mysql
try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="golfclub",
    database="golfclub"  # Specifico il database da utilizzare
    )

    mycursor = mydb.cursor()
    logging.info(mycursor)
except mysql.connector.Error as err:
   logging.error(f"error: {err}")
except Exception as e:
    print("error generics"+str(e))
    logging.warning(e)
  



while True:
    # opzioni disponibili
    print("Menu:")
    print("1. Select")
    print("2. Insert")
    print("3. Delete")
    print("4. Modified points")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    # mostro i dati
    logging.info(f"option: {choice}")
    if choice == "1":
        mycursor.execute("SELECT * FROM partecipanti")
      
        myresult = mycursor.fetchall()
        if not myresult:
            print("No data available.")
        else:
            try:
            #utilizzo la libreria table per vedere i record  in tabella
                table = PrettyTable()
                table.field_names = ["ID", "nome","cognome","regione_provenienza","circolo_provenienza","categoria","ultimo_torneo_partecipato","punti_classifica_principale","punti_classifica_parziale"]
                for row in myresult:
                    table.add_row(row)

                print(table)
            except Exception  as e:
                logging.error(e)
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
            partial_point=input("insert partial point: ")

            sql = "INSERT INTO partecipanti (nome,cognome,regione_provenienza,circolo_provenienza,categoria,ultimo_torneo_partecipato,punti_classifica_principale,punti_classifica_parziale) VALUES (%s, %s, %s, %s,%s,%s,%s,%s);"
            val = (name,surname,region,circle,categories,tournament,points,partial_point)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            logging.info( "record inserted.")
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
            logging.info( "record(s) deleted.")
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

                sql_update = "UPDATE partecipanti SET punti_classifica_principale = %s WHERE cognome = %s"
                val_update = (new_points, surname_to_update)

                mycursor.execute(sql_update, val_update)
                mydb.commit()

                print( "record(s) updated.")
            elif update_choice == "Circle":
                surname_to_update=input("Enter the surname to update circle:")
                new_circle_update=input("enter the new circle: ")
                sql_update = "UPDATE partecipanti SET circolo_provenienza = %s WHERE cognome = %s"
                val_update = (new_circle_update, surname_to_update)

                mycursor.execute(sql_update, val_update)
                mydb.commit()
                print(mycursor.rowcount, "record(s) updated.")
                logging.info( "record(s) updated.")
            else:
             print("Invalid choice. Please select a valid option.")
        except Exception as e:
           logging.warning("error" + str(e))
    # chiudo il programma
    elif choice == "5":
        print("Exiting the program.")
        break
    # operazione invalida
    # ad esempio se inserisco 6 questo è l'output
    else:
        print("Invalid choice. Please select a valid option.")
        logging.error(f"{choice} Invalid choice. Please select a valid option. ")

