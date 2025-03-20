import cv2
from PIL import Image, ImageDraw, ImageFont, ImageOps

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

cv2.imwrite('photo.png', frame)

image = Image.open('photo.png')
draw = ImageDraw.Draw(image)

font_tittle = ImageFont.truetype("1font/1font-medium.ttf", 34) 
font_text = ImageFont.truetype("1font/1font-regular.ttf", 25)
font_date = ImageFont.truetype("date_font.ttf", 20)
#Приветсвие
draw.text((10, 10), f"Присет мы Рома и Дима!", fill=(255, 255, 255), font=font_tittle)
draw.text((10, 45), f"это наша фотокарточка", fill=(255, 255, 255), font=font_tittle)

#Текст
draw.text((image.width - 630, image.height - 60), f"День самоуправления", fill=(255, 255, 255), font=font_text)
draw.text((image.width - 630, image.height - 35), f"Информатика | Проще, чем кажется", fill=(255, 255, 255), font=font_text)

#Дата
draw.text((image.width - 140, image.height - 35), f"12.12.2024", fill=(255, 255, 255), font=font_date)

#Рамка
bordered_image = ImageOps.expand(image, border = 3, fill = (209, 205, 168))

#Лого
logo = Image.open('logo.png').resize((80, 80))
logo = logo.convert("RGBA")
bordered_image.paste(logo, (bordered_image.width - 90, 10), logo)

bordered_image.save('card.png')
bordered_image.show()
