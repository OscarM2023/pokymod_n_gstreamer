SUMMARY = "Aplicacion de deteccion de bordes en Python"
LICENSE = "CLOSED"                 # Sin redistribución del código fuente

# Asegura que BitBake busque primero en ${LAYERDIR}/files
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

# Empaquetamos el script y la unidad de systemd desde la capa
SRC_URI = " \
    file://myapp.py \
    file://myapp.service \
"

# Evita que Yocto espere un árbol de fuentes "S" distinto
S = "${WORKDIR}"

inherit systemd

# Activa y habilita el servicio en runtime
SYSTEMD_SERVICE:${PN} = "myapp.service"
SYSTEMD_AUTO_ENABLE:${PN} = "enable"

# Dependencias en tiempo de ejecución.
RDEPENDS:${PN} = " \
    python3-core \
    python3-numpy \
    python3-opencv \
    gstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
"

do_install() {
    # Binarios y unidades
    install -d ${D}${bindir}
    install -d ${D}${systemd_unitdir}/system

    # Instala el script (ejecutable) y la unidad systemd (solo lectura)
    install -m 0755 ${WORKDIR}/myapp.py \
        ${D}${bindir}/myapp.py

    install -m 0644 ${WORKDIR}/myapp.service \
        ${D}${systemd_unitdir}/system/myapp.service
}

# Declara qué archivos van en el paquete principal
FILES:${PN} += " \
    ${bindir}/myapp.py \
    ${systemd_unitdir}/system/myapp.service \
"
