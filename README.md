<h1 align="center">
  <br>
  Aplicaciones para Neveras Inteligentes basadas en Deep Learning
  <br>
</h1>


<h4 align="center">
  Trabajo de Final de Grado del grado de Ingeniería Informática hecho por Lamberto Ruiz Martínez en la Universidad de Alicante. La duración del proyecto ha sido de 8 o 9 meses aprox. y el código no es ni limpio ni muy claro pero funciona. Tiene muchas posibles mejoras y por ello lo quiero publicar en GitHub y ver qué puede hacer la comunidad con esta idea.
</h4>

## Índice
1. [Introducción del proyecto](##Introducción-del-proyecto)
2. [Desarrollo del proyecto](##Desarrollo-del-proyecto)
3. [Comandos y demás ayudas](##Comandos-y-demás-ayudas)
4. [Posibles mejoras](##Posibles-mejoras)

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
* Para el funcionamiento en Linux, recomiendo encarecidamente instalar <a href="https://www.anaconda.com/download#downloads">Anaconda</a> para el uso de entornos de ejecución y poder ejecutar la aplicación web en uno de ellos con las instalaciones y librerías necesarias. 

* Importante instalar todos los requerimientos de YOLOv5 que hay en su repositorio para que la apliación funcione correctamente. La versión que hay en este repositorio de YOLOv5 está ya entrenada y faltan muchísimos modelos de entrenamiento y ficheros importantes. Por tanto, si vas a emplear este mecanismo para la detección de los alimentos, primero descargalo <a href="https://github.com/ultralytics/yolov5">aquí</a>:
  <p align="center">pip install -r requirements</p>
  
* También debes tener instalado Flask y la librería de OpenAI para la API de ChatGPT:
  <p align="center">
  sudo apt-get install python3-flask
  <br>
  pip install openai</p>
  
* Una vez creado el entorno de ejecución y todas las librerías han sido instaladas, podemos ejecutar la app:
  <p align="center">
  export FLASK_APP=app.py && flask run</p>
  
* Ahora entramos a nuestro navegador y ponemos la siguiente URL: http://127.0.0.1:5000/. Ya podemos ver la primera versión de este proyecto que como decía, lo dejo para que la comunidad pueda hacer progresos y mejoras :D.
<br>
* <b>IMPORTANTE</b>: Para que la parte de ChatGPT funcione, es necesario que tengas una API desde la web de OpenAI. En el módulo "recetas_chatgpt.py" es importante poner tu API KEY entre comillas dobles para que esto funcione.

## Posibles mejoras
A continuación listo una serie de posibles mejoras que se podrían realizar:
<ol>
<li>Mejorar la propia aplicación web de forma visual y añadiendo más funcionalidades y
contenido, como que el usuario pueda modificar manualmente los alimentos eliminando,
cambiando o añadiendo.</li>
<li>Mejorar el reconocimiento de imágenes probando otros modelos y comparándolos con
los resultados obtenidos.</li>
<li>Cambiando la forma de extraer las recetas utilizando por ejemplo un dataset de recetas
u otra tecnología.</li></ol>
