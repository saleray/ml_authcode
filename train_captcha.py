
from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random


digits =[i for i in  '0123456789']
alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]

CHAR_SET=digits+alphabet

def random_captcha_text(char_set=CHAR_SET,captcha_size=6):
    captcha_text=[]
    for i in range(captcha_size):
        c=random.choice(char_set)
        captcha_text.append(c)
    return captcha_text
def gen_captcha_text_and_image():
    image=ImageCaptcha()
    captcha_text=random_captcha_text()
    captcha_text=''.join(captcha_text)
    #print(captcha_text)
    captcha = image.generate(captcha_text)
    #image.write(captcha_text,captcha_text+'.png')
    captcha_image = np.array(Image.open(captcha))
    return captcha_text, captcha_image


#for _ in range(10):
    #gen_captcha_text_and_image()


