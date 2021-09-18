from PIL import Image

count = 1
while count <= 10000:

    filecount = str(count)
    img = Image.open("2.3/"+filecount+'.png').convert('RGB')
    img = img.resize((1000,1000),Image.ANTIALIAS)
    img.save('2.4/'+filecount+'.jpeg')
    count += 1