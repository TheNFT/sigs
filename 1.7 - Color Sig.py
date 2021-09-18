try:
    import uuid
    from PIL import Image
except ImportError:
    import Image

count = 1
while count <= 10000:

    filecount = str(count)
    filename = str(uuid.uuid4().hex)    
    overlay = Image.open("1.5/"+filecount+".png")
    background = Image.open("1.6/"+filecount+".png")

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    img = Image.new("RGBA", (4000, 4000), (0,0,0,0))
    
    img.paste(overlay, background)
    img.save("1.7/"+filecount+".png")
    count += 1
