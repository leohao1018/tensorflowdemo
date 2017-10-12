# coding:utf-8

import requests
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random, time, os
from io import BytesIO


class gen_captcha:
    def __init__(self):
        # 训练数据文件夹
        self.root_dir = "E:/08_pythonFile/tensorflowdemo/gaoyuan_captcha/train-data/"
        self.train_count = 350
        self.all_captcha_texts = self.get_captcha_texts()

        # 验证码中的字符, 就不用汉字了
        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u',
                         'v', 'w', 'x', 'y', 'z']
        self.ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U',
                         'V', 'W', 'X', 'Y', 'Z']

    # 验证码一般都无视大小写；验证码长度4个字符
    def random_captcha_text(self):
        char_set = self.number + self.alphabet + self.ALPHABET
        captcha_size = 4

        captcha_text = []
        for i in range(captcha_size):
            c = random.choice(char_set)
            captcha_text.append(c)
        return captcha_text

    # 生成字符对应的验证码
    def gen_captcha_text_and_image(self):
        image = ImageCaptcha()

        captcha_text = self.random_captcha_text()
        captcha_text = ''.join(captcha_text)

        captcha = image.generate(captcha_text)

        captcha_image = Image.open(captcha)
        captcha_image = np.array(captcha_image)
        return captcha_text, captcha_image

    def get_gaoyuan_image(self):
        response = requests \
            .get(
            "http://shixin.court.gov.cn/captchaNew.do?captchaId=4e7d5cb48d2f477b9fbb900b881bc100&random=0.9224144561849414")

        image_content = response.content

        f = BytesIO()
        f.write(image_content)
        captcha_image = Image.open(f)
        captcha_image = captcha_image.resize((160, 60), Image.ANTIALIAS)
        captcha_image = np.array(captcha_image)
        return captcha_image

    def get_captcha_texts(self):
        filename = self.root_dir + "captcha.txt"
        file_object = open(filename, 'r')
        lines = []
        try:
            list_of_all_the_lines = file_object.readlines()
            for line in list_of_all_the_lines:
                lines.append(line.replace('\n', ''))
        finally:
            file_object.close()

        return lines

    # 高院验证码训练图片
    def get_gaoyuan_image_by_exist(self):
        rd = random.randrange(1, self.train_count + 1)
        captcha_text = self.all_captcha_texts[rd - 1]
        filename = self.root_dir + str(rd) + ".jpg"

        file_object = open(filename, 'rb')
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()

        image_content = all_the_text

        f = BytesIO()
        f.write(image_content)
        captcha_image = Image.open(f)
        captcha_image = captcha_image.resize((160, 60), Image.ANTIALIAS)
        captcha_image = np.array(captcha_image)
        return captcha_text, captcha_image

    def save_file(self, file_name, data):
        path = "images" + "/"
        file = open(path + file_name, "wb")
        file.write(data)
        file.flush()
        file.close()

    def get_special_image(self):
        captcha_text = ''
        filename = 'E:/tmp/captchaNew.jpg'

        file_object = open(filename, 'rb')
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()

        image_content = all_the_text

        f = BytesIO()
        f.write(image_content)
        captcha_image = Image.open(f)
        captcha_image = captcha_image.resize((160, 60), Image.ANTIALIAS)
        captcha_image = np.array(captcha_image)
        return captcha_text, captcha_image

# if __name__ == '__main__':
#     while (1):
#         captcha_text, image = get_gaoyuan_image_by_exist()
#         print('begin ', time.ctime(), type(image))
#         f = plt.figure()
#         ax = f.add_subplot(111)
#         ax.text(0.1, 0.9, captcha_text, ha='center', va='center', transform=ax.transAxes)
#         plt.imshow(image)
#
#         plt.show()
#         print('end ', time.ctime())
