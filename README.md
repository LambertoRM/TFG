<h1 align="center">
  <br>
  TFG del Grado de Ingeniería Informática
  <br>
</h1>


<h4 align="center">
  Trabajo de Final de Grado del grado de Ingeniería Informática hecho por Lamberto Ruiz Martínez. La duración del proyecto ha sido de 8 o 9 meses aprox. y el código no es ni limpio ni muy claro pero funciona. Tiene muchas posibles mejoras y por ello lo quiero publicar en GitHub y ver qué puede hacer la comunidad con esta idea.
</h4>

## Introducción del proyecto
Este proyecto consiste, mediante el reconocimiento de alimentos dentro de una nevera, en obtener recetas que podríamos realizar con los alimentos detectados previamente.<br>
Para ello se han empleado las siguientes tecnologías:
* <a href="https://www.python.org/">Python</a>.
* <a href="https://github.com/ultralytics/yolov5">YOLOv5</a>.
* Datasets de entrenamiento de la red de <a href="https://roboflow.com/">Roboflow</a>.
* <a href="https://openai.com/">API de Chat GPT 3.5-turbo</a>.
* <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask</a>.
* Otras tecnologías.

## Desarrollo del proyecto
A continuación muestro un gráfico de cuál sería la lógica del proyecto a gran escala con algunas las tecnologías más importantes representadas:
<br>
![https://github.com/LambertoRM/TFG/blob/main/img%20readme/Estructura_TFG.png](https://raw.githubusercontent.com/LambertoRM/TFG/main/img%20readme/Estructura_TFG.png)

## Comandos y demás ayudas
Para el funcionamiento en Linux, recomiendo encarecidamente instalar <a href="https://www.anaconda.com/download#downloads">Anaconda</a> para el uso de entornos de ejecución y poder ejecutar la aplicación web en uno de ellos. 

Importante instalar todos los requerimientos de YOLOv5 que hay en su web para que la apliación funcione correctamente:
<br>
pip install -r requirements
<br>
También debes tener instalado Flask y la librería de OpenAI para la API de ChatGPT:
<br>
sudo apt-get install python3-flask
<br>
pip install openai
<br>
Una vez creado el entorno de ejecución y todas las librerías han sido instaladas, podemos ejecutar la app:
<br>
export FLASK_APP=app.py && flask run
<br>
Ahora entramos a nuestro navegador y ponemos la siguiente URL: http://127.0.0.1:5000/. Ya podemos ver la primera versión de este proyecto que como decía, lo dejo para que la comunidad pueda hacer progresos y mejoras :D.

<b>IMPORTANTE</b>: Para que la parte de ChatGPT funcione, es necesario que tengas una API desde la web de OpenAI. En el módulo "recetas_chatgpt.py" es importante poner tu API KEY entre comillas dobles para que esto funcione.
