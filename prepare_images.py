from PIL import Image

im = Image.open("empanadas.jpg")

size = 64, 64

out = im.convert("L").resize((64,64))
out.thumbnail(size, Image.ANTIALIAS)

with open("processed.jpg", 'w') as f:
    out.save(f)