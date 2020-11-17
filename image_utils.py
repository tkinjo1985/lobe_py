import os
from io import BytesIO

import numpy as np
import requests
from PIL import Image


def preprocess_from_file(image_path):
    """
    予測に使用する画像をnumpy.ndarrayに変換する。

    parameter:
    image_path: 画像ファイル

    return:
    image: numpy.ndarray
    """
    if os.path.exists(image_path):
        image = image2numpy(image_path)
        return image
    else:
        print('画像が見つかりません。')


def preprocess_from_url(image_url):
    """
    予測にWBE上の画像を使う場合は、この関数を使い画像をnumpy.ndarrayに変換する。

    parameter:
    image_url: 画像のURL

    return:
    image: numpy.ndarray
    """
    res = requests.get(image_url)
    if res.status_code == 200 and res.headers['Content-Type'] == 'image/jpeg':
        image_bytes = BytesIO(res.content)
        image = image2numpy(image_bytes)
        return image
    else:
        print('画像が見つかりません。URLを確認してください。')


def image2numpy(image):
    """
    画像をnumpy形式に変換する。
    """
    image = Image.open(image)
    image = np.asarray(image, dtype=np.float32) / 255.0
    image = np.expand_dims(image, axis=0)
    return image
