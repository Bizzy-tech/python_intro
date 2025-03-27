from PIL import Image

img = Image.open("images/pic.jpg")
img2 = img.convert("L")

img2.save("images/pic2.jpg")
