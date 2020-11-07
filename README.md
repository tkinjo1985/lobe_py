マイクロソフトからリリースされた機械学習のトレーニングツール「Lobe」 で学習したmodelをPythonから利用するためのサンプルコードです。
Qiitaにアップした記事をご確認ください。

[マイクロソフトが公開した機械学習モデルの訓練を容易にできる「Lobe」を試してみた。](https://qiita.com/tkinjo1/items/5cfe561b8765add0b7d0)

[Lobeで学習したモデルをPythonで利用する方法](https://qiita.com/tkinjo1/items/bbcb77fb0f4b8fe79a81)

## 使い方
```lobe_example.py
from model import ImageModel
import image_utils

# 1, modelのインスタンス生成。引数はmodelの保存パス。
model = ImageModel('sample_model')

# 2, modelの入力サイズを取得。引数はsignatureファイル。
input_width, input_height, input_channel = model.get_input_shape('sample_model/signature.json')

# 3, 予測したい画像を用意する。引数には画像ファイルもしくはURLと2で取得したmodelへの入力サイズを指定する。
# 画像ファイルを使用する場合
image = image_utils.preprocess_from_file('sample_image/cat/cat.105.jpg', input_width=input_width, input_height=input_height, input_channel=input_channel)

# URLを使用する場合
image = image_utils.preprocess_from_url('画像URL', input_width, input_height, input_channel)

# 4, 予測する。
predict_label = model.predict(image)
print(predict_label)
```

## TensorFlow Servingと組み合わせてREST APIにする。

[Lobeで学習したモデルとTensorFlow Servingを使ってREST APIを作る。](https://qiita.com/tkinjo1/items/4fd9f0202aa8e3949845)

[lobe_tensorflowserving](https://github.com/tkinjo1985/lobe_tensorflowserving)
