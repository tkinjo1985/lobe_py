マイクロソフトからリリースされた機械学習のトレーニングツール「Lobe」 で学習したmodelをPythonから利用するためのサンプルコードです。
Qiitaにアップした記事をご確認ください。

[マイクロソフトが公開した機械学習モデルの訓練を容易にできる「Lobe」を試してみた。](https://qiita.com/tkinjo1/items/5cfe561b8765add0b7d0)

[Lobeで学習したモデルをPythonで利用する方法](https://qiita.com/tkinjo1/items/bbcb77fb0f4b8fe79a81)

## 使い方
```
# Dockerを使用する場合は下記のコマンドを実行し出力されたURLにアクセスする。
$ docker-compose up --build

-----出力サンプル---------
web_1  | [I 00:49:58.539 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
web_1  | [C 00:49:58.545 NotebookApp] 
web_1  |     
web_1  |     To access the notebook, open this file in a browser:
web_1  |         file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
web_1  |     Or copy and paste one of these URLs:
web_1  |         http://4dfef021f377:8888/?token=0e67269931c2b948693729cdef7e132849c8932da4d09251
web_1  |      or http://127.0.0.1:8888/?token=0e67269931c2b948693729cdef7e132849c8932da4d09251
```
```lobe_example.py
from model import ImageModel
from image_utils import preprocess_from_file, preprocess_from_url

# 1, modelのインスタンス生成。引数はmodelの保存パス。
model = ImageModel('sample_model')

# 2, modelの入力サイズを取得。引数はsignatureファイル。 
input_shape = model.get_input_shape('sample_model/signature.json')

# 3, 予測したい画像を用意する。引数には[画像ファイルもしくはURL]と[2で取得したmodelへの入力サイズ]を指定する。
# 画像ファイルを使用する場合
image = preprocess_from_file('sample_image/cat/cat.105.jpg', input_width=input_shape[0], input_height=input_shape[1])

# *input_shapeを引数にすることで展開されてそれぞれの要素が個別の引数として渡されるのでおなじ結果を得ることができる。
image = preprocess_from_file('sample_image/cat/cat.105.jpg', *input_shape))

# URLを使用する場合
image = preprocess_from_url('画像URL', *input_shape)

# 4, 予測する。
predict_label = model.predict(image)
print(predict_label)
```

## TensorFlow Servingと組み合わせてREST APIにする。

[Lobeで学習したモデルとTensorFlow Servingを使ってREST APIを作る。](https://qiita.com/tkinjo1/items/4fd9f0202aa8e3949845)

[lobe_tensorflowserving](https://github.com/tkinjo1985/lobe_tensorflowserving)
