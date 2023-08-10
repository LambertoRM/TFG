# Made by Lamberto Ruiz Martínez
# GitHub: https://github.com/LambertoRM/

from flask import Flask, render_template, request, abort, redirect, url_for
from random import sample

from werkzeug.utils import secure_filename
import os
import shutil
import collections
from time import sleep

from recetas_chatgpt import chatGPT

import subprocess
import sys


app = Flask(__name__)
count = 0
archivo = "error"
lista_clas = []

@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html')

@app.route('/')
def index():
    return render_template('index.html')

def contador():
    global count
    count = count + 1
    numString = count

    return str(numString)

@app.route('/imagen', methods=['GET', 'POST'])
def imagen():

    if request.method == 'POST':
        file     = request.files['archivo']
        basepath = os.path.dirname (__file__) #ruta donde esta el archivo
        filename = secure_filename(file.filename) #nombre original del archivo

        #capturar extension del archivo
        extension      = os.path.splitext(filename)[1]

        #Eliminamos el contenido de la carpeta imagenes
        dir = './static//imagenes/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        if (extension == ".jpg") or (extension == ".jpeg") or (extension == ".png"):
            #newNombre      = "imagen" + extension
            newNombre  = "imagen" + contador() + extension

            upload_path = os.path.join (basepath, 'static/imagenes', newNombre)
            file.save(upload_path)
            global archivo
            archivo = newNombre
            
            #return procesar_imagen()
            return redirect(url_for('procesar_imagen'))
        
        else:
            return render_template('error_subir_imagen.html')
        
    return render_template('imagen.html')

def contar_clases(c):
    global lista_clas
    
    match c:
        case "0":	lista_clas.append("Manzana/s")
        case "1":	lista_clas.append("Espárrago/s")
        case "2":	lista_clas.append("Berenjena/s")
        case "3":	lista_clas.append("Bacon")
        case "4":	lista_clas.append("Plátano/s")
        case "5":	lista_clas.append("Bazlamá/s")
        case "6":	lista_clas.append("Carne/s")
        case "7":	lista_clas.append("Remolacha/s")
        case "8":	lista_clas.append("Arándanos")
        case "9":	lista_clas.append("Pan/es")
        case "10":	lista_clas.append("Broccoli/s")
        case "11":	lista_clas.append("Mantequilla/s")
        case "12":	lista_clas.append("Zanahoria/s")
        case "13":	lista_clas.append("Coliflor/es")
        case "14":	lista_clas.append("Queso/s")
        case "15":	lista_clas.append("Pollo/s")
        case "16":	lista_clas.append("Pechuga/s de pollo")
        case "17":	lista_clas.append("Chocolate/s")
        case "18":	lista_clas.append("Chips de chocolate")
        case "19":	lista_clas.append("Maíz")
        case "20":	lista_clas.append("Calabacines")
        case "21":	lista_clas.append("Crema/s")
        case "22":	lista_clas.append("Crema/s de queso")
        case "23":	lista_clas.append("Pepino/s")
        case "24":	lista_clas.append("Dates")
        case "25":	lista_clas.append("Huevos")
        case "26":	lista_clas.append("Harina/s")
        case "27":	lista_clas.append("Jengibre/s")
        case "28":	lista_clas.append("Queso/s de cabra")
        case "29":	lista_clas.append("Judías verdes")
        case "30":	lista_clas.append("Pimiento/s verde")
        case "31":	lista_clas.append("Chiles verdes")
        case "32":	lista_clas.append("Carne/s picada")
        case "33":	lista_clas.append("Jamón/es")
        case "34":	lista_clas.append("Nata/s")
        case "35":	lista_clas.append("Zumo/s")
        case "36":	lista_clas.append("Kiwi/s")
        case "37":	lista_clas.append("Limón/es")
        case "38":	lista_clas.append("Lechuga/s")
        case "39":	lista_clas.append("Lima/s")
        case "40":	lista_clas.append("Mango/s")
        case "41":	lista_clas.append("Carne/s")
        case "42":	lista_clas.append("Leche/s")
        case "43":	lista_clas.append("Menta/s")
        case "44":	lista_clas.append("Setas")
        case "45":	lista_clas.append("Oliva/s")
        case "46":	lista_clas.append("Cebolla/s")
        case "47":	lista_clas.append("Naranja/s")
        case "48":	lista_clas.append("Perejil")
        case "49":	lista_clas.append("Melocotón")
        case "50":	lista_clas.append("Guisantes")
        case "51":	lista_clas.append("Pepinillos")
        case "52":	lista_clas.append("Patata/s")
        case "53":	lista_clas.append("Rábano/s")
        case "54":	lista_clas.append("Pimiento/s rojo")
        case "55":	lista_clas.append("Col")
        case "56":	lista_clas.append("Uva/s")
        case "57":	lista_clas.append("Cebolla/s roja")
        case "58":	lista_clas.append("Salami/s")
        case "59":	lista_clas.append("Salsa/s")
        case "60":	lista_clas.append("Embutido/s")
        case "61":	lista_clas.append("Chalote/s")
        case "62":	lista_clas.append("Camarón")
        case "63":	lista_clas.append("Espinaca/s")
        case "64":	lista_clas.append("Cebolleta/s")
        case "65":	lista_clas.append("Fresa/s")
        case "66":	lista_clas.append("Azúcar")
        case "67":	lista_clas.append("Batata/s")
        case "68":	lista_clas.append("Maíz")
        case "69":	lista_clas.append("Tomate/s")
        case "70":	lista_clas.append("Tomate/s")
        case "71":	lista_clas.append("Botella/s de agua/s")
        case "72":	lista_clas.append("Pimiento/s amarillo")
        case "73":	lista_clas.append("Yoghurt/s")
        case "74":	lista_clas.append("Calabacín")

    # print(lista_clas)
    return 

@app.route('/resultados', methods=['GET', 'POST'])
def read_archivo():
    global archivo
    global lista_clas
    lista_clas = []
    name = os.path.splitext(archivo)[0]
    rutaImagen = "./static/yolov5/runs/detect/" + archivo + "/" + archivo

    file = open("./static/yolov5/runs/detect/" + archivo + "/labels/" + name + ".txt", "r")
    for linea in file:
        clase = linea[:linea.index(' ')]
        contar_clases(clase)
    file.close()

    #lista = procesar_lista()
    
    #ingredientes = contar_clases()
    #print(lista_clas)

    c = collections.Counter(lista_clas)
    
    return render_template('resultados.html', ing = c, imagen = rutaImagen)

@app.route('/imagen-procesando', methods=['GET', 'POST'])
def procesar_imagen():
    global archivo
    pesos = 'best_150m.pt'
    
    #Eliminamos el contenido de la carpeta detect
    dir = './static/yolov5/runs/detect/'
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        shutil.rmtree(path)

    #shutil.rmtree("./static/yolov5/runs/detect/")
    print('python ./static/yolov5/detect.py --source ./static/imagenes/' + archivo + ' --weights ./static/w/' + pesos + ' --conf 0.15 --save-txt --name ' + archivo)
    os.system('python ./static/yolov5/detect.py --source ./static/imagenes/' + archivo + ' --weights ./static/w/' + pesos + ' --conf 0.15 --save-txt --name ' + archivo)
        
    # Leer archivo generado
    sleep(3)
    #read_archivo()
    return redirect(url_for('read_archivo'))
    
@app.route('/5-posibles-recetas', methods=['GET', 'POST'])
def openai_recetas_5():
    c = collections.Counter(lista_clas)
    num_recetas = "5"

    chat = chatGPT(c, "", num_recetas)
    respuesta = chat.pregunta()
    #lista_rec = respuesta.split(' ')
    #print(respuesta)
    return render_template('recetas.html', ing = c, recet = respuesta, elem = num_recetas)

@app.route('/10-posibles-recetas', methods=['GET', 'POST'])
def openai_recetas_10():
    c = collections.Counter(lista_clas)
    num_recetas = "10"

    chat = chatGPT(c, "", num_recetas)
    respuesta = chat.pregunta()
    #lista_rec = respuesta.split(' ')
    #print(respuesta)
    return render_template('recetas.html', ing = c, recet = respuesta, elem = num_recetas)

@app.route('/20-posibles-recetas', methods=['GET', 'POST'])
def openai_recetas_20():
    c = collections.Counter(lista_clas)
    num_recetas = "20"

    chat = chatGPT(c, "", num_recetas)
    respuesta = chat.pregunta()
    #lista_rec = respuesta.split(' ')
    #print(respuesta)
    return render_template('recetas.html', ing = c, recet = respuesta, elem = num_recetas)

@app.route('/modificar-recetas', methods=['GET', 'POST'])
def modificar_recetas():
    c = collections.Counter(lista_clas)
    num_recetas = "10"

    chat = chatGPT(c, "", num_recetas)
    respuesta = chat.pregunta_diferente()
    #lista_rec = respuesta.split(' ')
    #print(respuesta)
    return render_template('recetas.html', ing = c, recet = respuesta, elem = num_recetas)

