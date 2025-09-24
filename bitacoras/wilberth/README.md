# Bitácora — Wilberth Gutiérrez Montero

## 02 de septiembre de 2025
**Lo hecho:** Arranqué el proyecto revisando qué es Yocto y cómo encajan sus piezas. Preparé la computadora de trabajo, descargué el árbol de código y dejé lista la carpeta de compilación. También repasé la documentación básica de OpenCV y GStreamer para entender qué necesitaremos más adelante.  
**Problemas:** Ajustar los directorios de descargas y de caché tomó un rato, más que nunca había usado la VM de Azure.

---

## 08 de septiembre de 2025
**Lo hecho:** Nos reunimos para repartir tareas. A mí me tocó levantar una primera imagen de prueba con Python. Investigué cómo personalizar la imagen y confirmé que, para usar GStreamer desde Python, lo más práctico sería trabajar con PyGObject.  
**Problemas:** Al principio confundí qué va en “características de la imagen” y qué corresponde a “características de la distribución”, y eso me generó dudas sobre dónde activar cosas como *ssh* o *systemd*.

---

## 10 de septiembre de 2025
**Lo hecho:** Creé mi propia capa de trabajo y armé una imagen base con Python para la rama **walnascar** de Yocto. La idea fue dejar un cimiento mínimo y estable antes de meter multimedia.  
**Problemas:** La compilación falló porque pedí “python3” de forma genérica; aprendí que hay que llamar a los componentes concretos de Python. Además, ajusté la referencia de licencia en una receta que inicialmente puse de forma imprecisa.

---

## 13 de septiembre de 2025
**Lo hecho:** Empecé a sumar GStreamer y OpenCV a la imagen. La intención fue tener lo necesario para correr pruebas de video y luego consumirlo desde Python.  
**Problemas:** Me pegué por detalles de escritura al agregar paquetes (espacios, sufijos) y por dependencias que no estaban del todo declaradas. También descubrí que, si no se incluye el soporte de introspección, Python no encuentra los módulos de GStreamer.

---

## 14 de septiembre de 2025
**Lo hecho:** Conseguí que la imagen con multimedia compilara de forma consistente. Validé con un *pipeline* simple de GStreamer y con una importación de prueba desde Python.  
**Problemas:** Tuve dudas con algunos complementos de GStreamer por el tema de licencias y, en un par de ocasiones, la caché de compilación quedó en un estado raro y tuve que recompilar en limpio.

---

## 15 de septiembre de 2025
**Lo hecho:** Preparé el camino para usar *systemd* como sistema de arranque, pensando en poder instalar nuestra aplicación como servicio. Dejé una unidad de ejemplo para que el proceso inicie solo.  
**Problemas:** La primera vez el servicio no levantó porque hacía falta instalar correctamente el archivo de unidad y declararlo para que se habilitara en la imagen.

---

## 17 de septiembre de 2025
**Lo hecho:** Generé la imagen en formato para máquina virtual y probé en VirtualBox. Verifiqué consola, usuarios y que la base arrancara.  
**Problemas:** El primer disco virtual no arrancó por corrupción del archivo; liberé espacio, regeneré la imagen y validé antes con QEMU. Con eso, VirtualBox funcionó bien.

---

## 18 de septiembre de 2025
**Lo hecho:** Personalicé el nombre del equipo (hostname) y agregué un usuario de desarrollo con los grupos necesarios. También dejé documentado cómo mantener estos cambios desde recetas y no solo desde la configuración temporal.  
**Problemas:** La compilación se cayó con un error al crear usuarios porque me faltó incluir la parte que habilita ese mecanismo en la imagen. Además, el .gitignore bloqueaba subir mi capa y los *conf* de la *build*, y tuve que reordenarlo.

---

## 19 de septiembre de 2025
**Lo hecho:** Activé *ssh* para poder copiar archivos y trabajar de forma remota. Añadí algunos recursos (imágenes y otros) a una carpeta fija dentro del sistema y dejé la aplicación de Python instalada con un servicio para que inicie al arrancar.  
**Problemas:** Al principio no pude entrar por *ssh* con llaves; ajusté la copia de claves durante la creación del sistema de archivos. También acomodé las rutas para que la app de Python encuentre sus recursos sin trucos.

---

## 20 de septiembre de 2025
**Lo hecho:** Validé el uso de GStreamer desde Python con PyGObject en la rama **walnascar**, confirmando que la importación y la inicialización se hacen sin errores.  
**Problemas:** En un intento de prueba la importación falló porque faltaba un paquete de introspección; lo agregué a la imagen y volvió a funcionar.

---

## 22 de septiembre de 2025
**Lo hecho**: Realicé la ronda final de pruebas en Oracle VirtualBox con la imagen generada en Yocto. Verifiqué arranque, el procesado de imagenes con aplicaciones y el uso de ssh.
**Problemas**: No hubo problemas.

---

## 23 de septiembre de 2025

**Lo hecho**: Actualicé el tutorial junto con mis compañeros. Reestructuramos el README para que siguiera la metodología que indicaba el instructivo y la rúbrica.
**Problemas**: Conflictos menores con git por modificar el mismo archivo README.md.
