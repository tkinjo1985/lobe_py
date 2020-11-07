# ベースイメージ名:タグ名
FROM ubuntu:latest

# パッケージアップデートと必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim \
    git \
    python3-dev \
    python3-pip

# workdirを/optへ変更
WORKDIR /opt

# anacondaのインストールスクリプトのダウンロードとスクリプト実行
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh && \
    sh Anaconda3-2020.07-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    rm -rf Anaconda3-2020.07-Linux-x86_64.sh

# anaconda3へのPATHを追加
ENV PATH=/opt/anaconda3/bin:$PATH

# pipのインストール
RUN pip install --upgrade pip
RUN pip install tensorflow-cpu

# workdirを/へ変更
WORKDIR /work
