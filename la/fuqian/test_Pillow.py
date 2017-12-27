from PIL import Image

im = Image.open("fileTest/gile.jpeg")
w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
im.save('fileTest/thumbnail.jpeg', 'jpeg')