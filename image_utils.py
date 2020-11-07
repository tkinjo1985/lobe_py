from io import BytesIO

import numpy as np
import requests
from PIL import Image


def preprocess_from_file(image_path, input_width, input_height, input_channel):
    """
    予測に使用する画像をmodelへの入力サイズに合わせてnumpy.ndarrayに変換します。

    parameter:
    image_path: 画像ファイル
    input_width: 幅
    input_height: 高さ　
    input_channel: チャネル

    return:
    image: numpy.ndarray
    """
    try:
        image = Image.open(image_path)
        image = image.resize((input_width, input_height))
        image = np.array(image, dtype=np.float32) / 255.0
        image = image.reshape([1, input_width, input_height, input_channel])
        return image
    except FileNotFoundError as err:
        print('画像がみつかりません。画像の保存先と名前を確認してください。')
        print(err)


def preprocess_from_url(image_url, input_width, input_height, input_channel):
    """
    予測にWBE上の画像を使う場合は、この関数を使いmodelへの入力サイズに合わせてnumpy.ndarrayに変換します。

    parameter:
    image_url: 画像のURL
    input_width: 幅
    input_height: 高さ　
    input_channel: チャネル

    return:
    image: numpy.ndarray
    """
    res = requests.get(image_url)
    if res.status_code == 200 and res.headers['Content-Type'] == 'image/jpeg':
        image = BytesIO(res.content)
        image = Image.open(image)
        image = image.resize((input_width, input_height))
        image = np.array(image, dtype=np.float32) / 255.0
        image = image.reshape((1, input_width, input_height, input_channel))
        return image
    else:
        print('画像が見つかりません。URLを確認してください。')
