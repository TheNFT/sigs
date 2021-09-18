import numpy as np
from PIL import Image

count = 1
while count <= 10000:

    filecount = str(count)
    array = np.random.randint(low = 0, high = 255, size = (1, 1, 3))
    img = Image.fromarray(array.astype('uint8'))
    img.save('1.0/'+filecount+'.png')
    count += 1