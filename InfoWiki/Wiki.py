import wikipedia as wiki #Importamos la libreria wikipedia

wiki.set_lang("es") #Cambiar el idioma de la busqueda a español

def replaceChars(text): #Funcion para reemplazar caracteres especiales
    char_to_replace = ['.', ',', '(', ')', '!', '?', '¿', '¡', "'", '"', '[', ']', '=', '<', '>', '»', '«', '°', '-', ':', ';']
    for char in char_to_replace:
        text = text.replace(char, ' ')
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')
    text = text.replace('ñ', 'n')
    return text

def getData(busqueda):  #Funcion para obtener los datos de la busqueda
    data = []
    title = busqueda.title
    title = replaceChars(title)
    content = busqueda.content.lower()
    content = replaceChars(content)
    data = [title, content]
    return data

#---------------Busqueda de contenido----------------

busquedas = ["Copa Mundial de Fútbol de 2022","Copa Mundial de Fútbol de 2018","Copa Mundial de Fútbol de 2014","Copa Mundial de Fútbol de 2010","Copa Mundial de Fútbol de 2006","Lionel Messi","Cristiano Ronaldo","Alexis Sanchez","Neymar","Paulo Dybala"]
nombres = ["Qatar","Rusia","Brasil","Sudafrica","Alemania","Messi","Ronaldo","Sanchez","Neymar","Dybala"]
i = 0

for x in busquedas:
    busqueda = wiki.page(x) #Buscamos la pagina
    data = getData(busqueda) #Obtenemos el titulo y el contenido de la pagina
    with open('./'+nombres[i]+'.txt', 'w', encoding='utf-8') as f:
        i += 1
        f.write("WikiTitle: " + data[0] + "\n") #Escribimos el titulo
        f.write(data[1]) #Escribimos el contenido
        f.write("\n")
        f.write("\n")
        f.close()