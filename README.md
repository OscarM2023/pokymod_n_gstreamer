# Sistema detector de Cajas (Contornos)

> En este repositorio se realiza el desarrollo de un sistema operativo custom utilizando la herramienta de **Yocto Project**. Se utiliza **Gstreamer** con su sistema de pipelines para poder obtener componentes multimedia, además se utiliza **OpenCV** para realizar el procesamiento de las imagenes.



##  Desarrolladores
El sistema fue desarrollado por:

- Nagel Eduardo Mejía Segura
- Oscar Gonzalez Cambronero
- Wilberth Gutierrez Montero

## Tabla de Contenidos


1. [Caracteristicas del Host](#caracteristicas-del-computador-host)
2. [Herramientas de Desarrollo](herramientas-de-desarrollo-y-requisitos)
    - [Yocto-Project](yocto-project)
    - [Gstreamer](gstreamer)
    - [OpenCV](yocto-project)
    - [Virtual-Box](virtual-box)
3. [Estructura del proyecto](estructura-básica-del-proyecto)

## Caracteristicas del Computador Host

- **Fabricante**:
- **Modelo**:
- **Sistema Operativo y Arquitectura**:
- **CPU y Nucleos**:
- **Capacidad RAM**:
- **Almacenamiento**:

## Herramientas de Desarrollo y Requisitos

### Yocto Project
Herramienta para customizar y generar imagenes de Linux.

**Requiere**:
  - 90 GB de disco duro libre minimo
  - 32 GB de RAM (Mejor perfomance en construcción)
  - Distribución de Linux
  - Dependencias:
      - Git 1.8.3.1
      - tar 1.28
      - Python 3.9.0
      - gcc 10.1
      - GNU make 4.0

### Gstreamer
Herramienta para generar pipelines de flujo multimedia

**Requiere**:
  - Distribución Linux (mejor compatibilidad)
  - Python o C++ (inclusión en códigos)

### OpenCV
Herramienta para visión por computadora, permite procesar imagenes.

### Virtual Box
Programa de Virtualización

**Requiere**:
  - Arquitectura de 64 bits
  - Recomendación asignar 4 GB de RAM
  - Minimo asignar 3 nucleos
  - Soporte de Virtualización (BIOS-UEFI)

## Estructura básica del proyecto

```
├── meta-python-scripts
│   ├── conf
│   │   └── layer.conf
│   └── recipes-python
│       └── python-scripts
│            ├── files
│            │   └── python-scripts-1.0
│            │       ├── boxdetector.py
│            │       ├── edgedetect.py
│            │       ├── hello_python.py
│            │       ├── inputs
│            │       │   └── box_test.mp4
│            │       ├── main.py
│            │       └── src
│            │           ├── detector.py
│            └── python-scripts.bb
└── build
    └── conf/
        ├── bblayers.conf
        └── local.conf

```
