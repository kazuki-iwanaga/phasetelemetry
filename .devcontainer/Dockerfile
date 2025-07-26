FROM python:3.11-bullseye

WORKDIR /tmp

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash-completion \
        build-essential \
        git \
        curl \
        unzip \
        vim \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN echo "source /usr/share/bash-completion/bash_completion" >> /etc/bash.bashrc

COPY requirements.txt .
RUN python3.11 -m pip install -r requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python2.7 \
    && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python2.7 /usr/local/bin/python2.7 \
    && curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py \
    && python2.7 get-pip.py

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

USER $USERNAME
WORKDIR /workspace
