import os
from io import BytesIO

import numpy as np
import requests
from PIL import Image


def preprocess_from_file(image_path, input_width, input_height):
    """
    予測に使用する画像をmodelへの入力サイズに合わせてnumpy.ndarrayに変換します。

    parameter:
    image_path: 画像ファイル
    input_width: 幅
    input_height: 高さ　

    return:
    image: numpy.ndarray
    """
    if os.path.exists(image_path):
        image = image_resize(image_path, input_width, input_height)
        return image
    else:
        print('画像が見つかりません。')


def preprocess_from_url(image_url, input_width, input_height):
    """
    予測にWBE上の画像を使う場合は、この関数を使いmodelへの入力サイズに合わせてnumpy.ndarrayに変換します。

    parameter:
    image_url: 画像のURL
    input_width: 幅
    input_height: 高さ　

    return:
    image: numpy.ndarray
    """
    res = requests.get(image_url)
    if res.status_code == 200 and res.headers['Content-Type'] == 'image/jpeg':
        image_bytes = BytesIO(res.content)
        image = image_resize(image_bytes, input_width, input_height)
        return image
    else:
        print('画像が見つかりません。URLを確認してください。')


def image_resize(image, input_width, input_height):
    image = Image.open(image)
    image = image.resize((input_width, input_height))
    image = np.asarray(image, dtype=np.float32) / 255.0
    image = np.expand_dims(image, axis=0)
    return image
