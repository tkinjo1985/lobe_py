# tensorflow公式イメージ(jupyter入り)を使用
FROM tensorflow/tensorflow:latest-jupyter

# tzdataのインストールで止まってしまう事象を回避するため
ENV DEBIAN_FRONTEND=noninteractive

# パッケージ一覧更新と必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    libopencv-dev \
    opencv-data

# 作業用ディレクトリを作成
WORKDIR /work

# pipを最新のアップデート
RUN pip install --upgrade pip

# 必要なPythonのパッケージをインストール
COPY requirements.txt /work
RUN pip install -r requirements.txt
