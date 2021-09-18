try:
    from PIL import Image, ImageOps
except ImportError:
    import Image

count = 1
while count <= 10000:
    filecount = str(count)
    im = Image.open('1.0/'+filecount+'.png').convert('RGB')
    im_invert = ImageOps.invert(im)
    im_invert.save('1.1/'+filecount+'.png')
    count += 1