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
        python3-matplotlib \
        cmake \
        black \
        yapf3 \
	git git-lfs gettext cmake \
	mtools \
    python3-dev \
        && \
    rm -rf /var/lib/apt/lists/*  \
    && apt-get clean



