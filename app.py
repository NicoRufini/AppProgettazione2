import psycopg2

# Dettagli di conessione
host = "localhost" # O l'indirizzo IP del tuo server DB
port = "5432" # La porta di default di PostgreSQL
dbname = "Accademia"
user = "postgres"
password = "postgres"

# Connesione al database
try:
    connection = psycopg2.connect (
        host = host,
        port = port,
        dbname = dbname,
        user = user,
        password = password
    )
    print("Connesione al database avvenuta col sucesso")
except Exception as e:
    print(f"Errore durante la connesione del database: {e}")
'''
cursor = connection.cursor()

# Esegui una query
cursor.execute("SELECT * FROM persona")

# Recupera i risultati
rows = cursor.fetchall()

for row in rows:
    print(row)

print("\n")

#Seconda tabella
cursor1 = connection.cursor()
# Esegui una query
cursor1.execute("SELECT * FROM progetto")

# Recupera i risultati
rows = cursor1.fetchall()

for row in rows:
    print(row)
'''

while True:
    #Per far ritornare una tabella all'interno di Accademia
    tabelle_Accademia = ["assenza", "attivitanonprogettuale", "attivitaprogetto", "persona", "progetto", "wp"]
    tabella_input = input("Inserisci il nome di una tabella: ").lower()

    if tabella_input in tabelle_Accademia:
        cursor = connection.cursor()

        # Esegui una query
        cursor.execute(f"SELECT * FROM {tabella_input}")

        # Recupera i risultati
        rows = cursor.fetchall()

        rows_number = 0

        for row in rows:
            print(row)
            rows_number += 1

        print("Rows:", rows_number)
    else:
        print("La tabella che hai inserito non è presente all'interno del database")


