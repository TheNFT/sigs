from PIL import Image,ImageFilter  

count = 1
while count <= 10000:

    filecount = str(count)  
    #Read image
    im = Image.open('1.1/'+filecount+'.png')
    #Display image  
    #im.show()
   
    from PIL import ImageEnhance  
    enh = ImageEnhance.Contrast(im)  
    enh.enhance(1.8).save('1.2/'+filecount+'.png')
    count += 1