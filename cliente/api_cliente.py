from flask import Flask, render_template, request
from psycopg2 import connect
import wikipedia

wikipedia.set_lang("es")
app = Flask(__name__)

conn = connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host='localhost'
       )
cursor = conn.cursor()

def orden(lista):
    return int(lista[1])
    
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/Busqueda', methods=['POST']) 
def NuevaVenta():
    if request.method == 'POST':
        resultados = []
        palabra = request.form['palabra']
        query = "SELECT documentos FROM buscador WHERE palabra = '"+palabra+"';"
        cursor.execute(query)
        paginas = cursor.fetchall()
        if paginas != []:
            paginas = paginas[0][0].split(') (')
            paginas[0] = paginas[0].replace('(','')
            paginas[-1] = paginas[-1].replace(')','')
            for x in paginas:
                x = x.split(',')
                x[1] = x[1].replace(' ','')
                resultados.append(x)
            resultados.sort(key=orden, reverse=True)

        for x in range(len(resultados)):
            page = wikipedia.page(resultados[x][0])
            resultados[x].append(page.url)
            resultados[x].append(page.title)

        return render_template('index.html', paginas=resultados)
        
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug = True)