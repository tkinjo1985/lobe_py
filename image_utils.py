import os
from io import BytesIO

import requests
from PIL import Image
import tensorflow as tf


def preprocess_from_file(image_path):
    """
    予測に使用する画像をnumpy.ndarrayに変換する。

    parameter:
        image_path str: 変換する画像ファイル

    return:
        numpy.ndarray: モデルへの入力形式に変換された画像データ
    """
    if os.path.exists(image_path):
        file_extension = os.path.splitext(os.path.basename(image_path))[-1]
        if file_extension == '.jpg' or file_extension == '.jpeg' or file_extension == '.png':
            image = _convert_image(image_path)
            return image
        else:
            print('画像ではありません。')
    else:
        print('ファイルが見つかりません。')


def preprocess_from_url(image_url):
    """
    予測にWBE上の画像を使う場合は、この関数を使い画像をnumpy.ndarrayに変換する。

    parameter:
        image_url str: 画像のURL

    return:
        numpy.ndarray: モデルへの入力形式に変換された画像データ
    """
    res = requests.get(image_url)
    content_type = res.headers['Content-Type']
    if res.status_code == 200 and 'jpeg' in content_type or 'png' in content_type:
        try:
            image_bytes = BytesIO(res.content)
        except Exception as err:
            print(err)
        else:
            try:
                image = Image.open(image_bytes).convert('RGB')
            except Exception as err:
                print(err)
            else:
                image = image.resize(size=(224, 224))
                image = _image2tensor(image)
                return image
    else:
        print('画像が見つかりません。URLを確認してください。')


def _convert_image(image_file):
    try:
        image = tf.keras.preprocessing.image.load_img(
            image_file, color_mode='rgb', target_size=(224, 224))
    except Exception as err:
        print(err)
    else:
        image = _image2tensor(image)
        return image


def _image2tensor(image):
    image = tf.keras.preprocessing.image.img_to_array(image) / 255.0
    image = tf.convert_to_tensor(image)
    image = tf.expand_dims(image, axis=0)
    return image
