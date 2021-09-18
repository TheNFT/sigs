from PIL import Image

count = 1
while count <= 10000:

    filecount = str(count)
    img = Image.open("1.0/"+filecount+'.png')
    pixels = img.load() 
    width, height = img.size

    for y in range(height):      # this row
        for x in range(width):   # and this row was exchanged
         r, g, b = pixels[x, y]
        
        # in case your image has an alpha channel
        # r, g, b, a = pixels[x, y]

    with open("2.1/"+filecount+".txt", "a") as text_file:
        print(x, y, f"#{r:02x}{g:02x}{b:02x}", file=text_file)
    count += 1
