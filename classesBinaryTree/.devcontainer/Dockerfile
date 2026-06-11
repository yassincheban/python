FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-22.04
ENV DEBIAN_FRONTEND=noninteractive
                
RUN apt-get update && apt-get install -y --no-install-recommends\
        mc \
        vim \
        git \
        zip \
        wget \
        python3-pycodestyle \
        python3-pip \
        python3-pillow \
        cmake \
        black \
        yapf3 \
	git git-lfs gettext cmake \
	mtools \
    python3-dev \
        && \
    rm -rf /var/lib/apt/lists/*  \
    && apt-get clean



RUN pip3 install \
    Adafruit_Blinka \
    Adafruit-Blinka-Displayio \
    adafruit-circuitpython-display-text \
    adafruit-circuitpython-st7789 \
    adafruit-circuitpython-neopixel \
    adafruit_circuitpython_logging \
    adafruit_circuitpython_asyncio

RUN git clone https://github.com/sebastianohl/Blinka_Pytest_Board.git && \
    pip3 install --upgrade ./Blinka_Pytest_Board   && \
    rm -Rf Blinka_Pytest_Board
    
RUN git clone https://github.com/sebastianohl/Adafruit_Blinka.git && \
    pip3 install --upgrade ./Adafruit_Blinka && \
    rm -Rf Adafruit_Blinka

RUN git clone https://github.com/sebastianohl/Adafruit_Python_PlatformDetect.git && \
    cp -R ./Adafruit_Python_PlatformDetect/adafruit_platformdetect /usr/local/lib/python3.10/dist-packages && \
    rm -Rf Adafruit_Python_PlatformDetect

ENV BLINKA_PYTEST="PYTEST"


