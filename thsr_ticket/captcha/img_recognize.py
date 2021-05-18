from keras.models import load_model
from PIL import Image
from thsr_ticket.captcha.utils import preprocessing
import numpy as np
import cv2

class Recognize:
    def __init__(self) -> None:
        self.WIDTH = 140
        self.HEIGHT = 48
        self.allowedChars = '234579ACFHKMNPQRTYZ'
        self.model = load_model("thsr_ticket/captcha/thsrc_cnn_model.hdf5")

    def predict(self, img):
        img = img.resize((self.WIDTH, self.HEIGHT), Image.ANTIALIAS)
        img = img.convert('RGB')
        img_path = 'thsr_ticket/captcha/images/'
        img.save(img_path+'captcha.jpg', "JPEG")

        preprocessing(img_path+'captcha.jpg', img_path+'preprocessing.jpg')
        train_data = np.stack([np.array(cv2.imread(img_path+'preprocessing.jpg'))/255.0])
        prediction = self.model.predict(train_data)

        predict_captcha = ''
        for predict in prediction:
            value = np.argmax(predict[0])
            predict_captcha += self.allowedChars[value]

        return predict_captcha