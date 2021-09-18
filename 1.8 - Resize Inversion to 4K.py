import numpy as np
from PIL import Image

count = 1
while count <= 10000:

    filecount = str(count)
    basewidth = 4000
    img = Image.open('1.1/'+filecount+'.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('1.8/'+filecount+'.png')
    count += 1