from PIL import Image

count = 1
while count <= 10000:

    filecount = str(count)

    # Opening the primary image (used in background)
    img1 = Image.open(r"#000000.png")
      
    # Opening the secondary image (overlay image)
    img2 = Image.open(r"2.2/"+filecount+".png")
    img2 = img2.resize((3000,3000),Image.ANTIALIAS)
    # Pasting img2 image on top of img1 
    # starting at coordinates (0, 0)
    img1.paste(img2, (500,500), mask = img2)
      
    # Displaying the image
    img1.save("2.3/"+filecount+".png")
    count += 1