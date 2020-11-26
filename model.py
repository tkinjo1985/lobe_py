import tensorflow as tf


class ImageModel:
    def __init__(self, model_path):
        """
        modelを読み込みます。

        paramter:
        model_paht: modelの保存パス
        """
        try:
            self.model = tf.saved_model.load(model_path)
            self.infer = self.model.signatures['serving_default']
        except Exception as err:
            print('modelが見つかりません。modelの保存先と名前を確認してください。')
            print(err)

    def predict(self, image):
        """
        与えられた画像から正解ラベルを予測します。

        Parameter:
        image: 予測したい画像(numpy.ndarray)

        Return:
        predict: 予測結果
        """
        try:
            predict = self.infer(tf.constant(image))['Prediction'][0]
            return predict.numpy().decode()
        except ValueError as e:
            print(e)
