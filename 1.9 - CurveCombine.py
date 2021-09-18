try:
    from PIL import Image
except ImportError:
    import Image

count = 1
while count <= 10000:

    filecount = str(count)
    
    img = Image.new("RGBA", (4000, 4000))
    overlay = Image.open("1.8/"+filecount+".png").convert('RGBA')
    background = Image.open("1.7/"+filecount+".png")
    
    overlay.paste(background, (0,0), background)
    overlay.save("1.9/"+filecount+".png")
    count += 1
