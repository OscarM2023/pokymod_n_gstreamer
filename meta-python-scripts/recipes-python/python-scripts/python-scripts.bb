SUMMARY = "Colección de scripts Python utilizados en el proyecto."
DESCRIPTION = "Scripts para probar el funcionamiento de pyton en el sistema."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://boxdetector.py \
           file://edgedetect.py \
           file://hello_python.py"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}

    install -m 0755 ${WORKDIR}/boxdetector.py ${D}${bindir}/
    install -m 0755 ${WORKDIR}/edgedetect.py ${D}${bindir}/
    install -m 0755 ${WORKDIR}/hello_python.py ${D}${bindir}/
}

# Runtime dependencies
RDEPENDS:${PN} = "python3-core"

FILES:${PN} = "${bindir}/*"
