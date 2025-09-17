SUMMARY = "Minimal + myapp (python + gstreamer + opencv)"
LICENSE = "MIT"

inherit core-image

IMAGE_FEATURES += "ssh-server-openssh"

# Paquetes base que necesitas en runtime + tu app
IMAGE_INSTALL:append = " \
    python3-core \
    python3-numpy \
    python3-opencv \
    gstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    myapp \
"

