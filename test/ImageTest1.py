'''
Created on Feb 2, 2015

@author: sikarwv
'''
from PIL import Image

pil_im = Image.OPEN('20140930_115332.jpg')
print(pil_im.format, pil_im.size) 