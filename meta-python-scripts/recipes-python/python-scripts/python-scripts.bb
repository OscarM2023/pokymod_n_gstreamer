SUMMARY = "Python scripts collection"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://python-scripts-1.0"

do_patch[noexec] = "1"
do_configure[noexec] = "1"
do_compile[noexec] = "1"

do_install() {
    install -d ${D}${bindir}
    
    echo "Contents of WORKDIR:"
    ls -la ${WORKDIR}/
    echo "Contents of python-scripts-1.0:"
    if [ -d "${WORKDIR}/python-scripts-1.0" ]; then
        ls -la ${WORKDIR}/python-scripts-1.0/
    else
        echo "python-scripts-1.0 directory does not exist!"
    fi
    echo "=================="
    
    # Install all .py files from the python-scripts-1.0 directory
    for pyfile in ${WORKDIR}/python-scripts-1.0/*.py; do
        echo "Processing file: $pyfile"
        if [ -f "$pyfile" ]; then
            echo "Installing: $pyfile to ${D}${bindir}/"
            install -m 0755 "$pyfile" ${D}${bindir}/
        else
            echo "File not found: $pyfile"
        fi
    done
    
    # Show final result
    echo "Final contents of ${D}${bindir}:"
    ls -la ${D}${bindir}/
}

# Include all files in bindir
FILES:${PN} = "/usr /usr/bin ${bindir}/*"

# Add runtime dependencies
RDEPENDS:${PN} = " \
    python3-core \
    python3-numpy \
    python3-pygobject \
    opencv \
    python3-opencv \
    gstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-libav \
"
