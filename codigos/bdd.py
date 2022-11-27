from psycopg2 import connect

conn = connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host='postgres'
       )
cursor = conn.cursor()

with open("output.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        word, docs = linea.split('\t',1)
        word = word.strip(':')
        query = "INSERT INTO buscador(palabra,documentos) VALUES ('"+word+"','"+docs+"');"
        cursor.execute(query)
        conn.commit()

cursor.close()
conn.close()