# Bitacora Nagel Eduardo Mejía Segura

## 31 de Agosto de 2025

- Se realizó una investigación inicial, así como la instalación de GStreamer y OpenCV.
- Siguiendo los tutoriales para ambas herramientas, se verificó el correcto funcionamiento inicial por medio de programas simples de Python.

Referencias: 
- https://docs.opencv.org/4.x/d3/d96/tutorial_basic_geometric_drawing.html 
- https://gstreamer.freedesktop.org/

## 15 de setiembre de 2025

- Se realizaron pruebas en opencv para poder realizar la detección de las cajas, primero se realizó por cuenta propia un código que utilizaba detector de bordes Canny, y seguidamente se utilizaba opencv para obtener los contornos.

Problemas Encontrados: No lograba detectar la mayoría de cajas, al revisar la imagen generada tras la detección de bordes, había mucho ruido esto provocaba que algunas cajas no se detectaran como tal ya que no concordaba con la forma del poligono buscado.

## 16 de setiembre de 2025

- Se investigó sobre formas de hacer la detección de cajas, se implementó un diseño de un repositorio coreano el cual resultó ser más robusto, de igual forma se seguirá investigando formas alternativas.

Problemas: Si bien el detector es robusto, aveces detecta poligonos "cuadrados" como cajas.

Referencias: https://github.com/KEG012/Project_openCV_Box_Detector

## 19 de setiembre de 2025

- Se organizó de mejor forma los códigos de python generando un programa principal (main.py), que utiliza los códigos de python del nuevo directorio de fuentes (src) para la detección de cajas (detector.py), el procesamiento del video (video_processor.py) y un código para implementar configuraciones generales (config.py).

Problemas: **ERROR** el programa de python no está funcionando por medio del pipeline de gstreamer, con opencv puro sí lo logra.

## 20 de setiembre de 2025

- Se descartaron los programas en src de config.py y videodetector.py ya que la funcionalidad de Gstreamer con python no está habilitada por defecto, se optó por la funcionalidad directa de Gstreamer con python utilizando appsink para obtener el frame y realizar las operaciones necesarias con opencv.

Deberes: Modificar los archivos de la receta para que acepte el nuevo programa completo.

## 21 de setiembre de 2025 (mañana)

- Se realizó la modificación de la receta para poder ejecutar el programa completo. Se realizaron pruebas en QEMU las cuales generaron resultados esperados logrando observar un pipeline de gstreamer de testeo de video por medio de ssh.

Problemas: Se me ha hecho imposible probar la imagen en VirtualBox, se me han generado errores en la configuración del propio programa, haciendo los pasos que recomienda el propio VirtualBox (ejecutar /sbin/vboxconfig) sigue provocando el mismo error.

## 21 de setiembre de 2025 (tarde)

- Se realizó una reunion con los integrantes, uno de los integrantes logró correr la aplicación en una maquina virtual, y logró visualizar el video procesado en vivo por medio de compartir recursos con ssh.

Deberes: Se debe completar el tutorial del programa.

## 23 de setiembre de 2025

- Se realizaron las partes de diagramas, generación y sintesis de la imagen, descripción de los toolkits. Se realizo una explicación de lo más importante sobre la receta generada, así como layers utilizadas, y configuraciones locales para el buen funcionamiento del programa.
