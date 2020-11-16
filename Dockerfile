FROM tensorflow/tensorflow:latest-jupyter

RUN apt-get update && apt-get install -y \
    sudo \
    git

WORKDIR /work

# pipを最新のアップデート
RUN pip install --upgrade pip

CMD [ "bash -c source /etc/bash.bashrc" ]
