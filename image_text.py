

from PIL import Image, ImageDraw, ImageFont

img = Image.open("images/pic.jpg")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 40)

text = "Boxing life"

image_width, image_height = img.size
x = image_width // 2
y = image_height // 2


text_color = (255,255,255)
draw.text((x,y), text,fill=text_color,font=font)
img.save("images/pic3.jpg")

