import zipfile
from zipfile import ZipFile

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pytesseract
import cv2 as cv
import numpy as np
import math


def addTopMargin(contact_sheet, top_margin, font, pic_text1 ) :
    width, height = contact_sheet.size
    new_height = top_margin + height
    image2 = Image.new(contact_sheet.mode, (width, new_height), (255,255,255))
    image2.paste(contact_sheet, (0,top_margin))
    d = ImageDraw.Draw(image2)
    d.text((0,3), pic_text1, font=font, fill=(0,0,0,255))
    return image2

def compose_cs(file_name, search_word, cv_coef):
    total_list = []
    top_margin = 25
    pic_text2 = 'But there were no faces in that file!'
    font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 20)
    face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

    with ZipFile(file_name, 'r') as zip:
        for name in zip.namelist():
            zip.extract(name)
            image=Image.open(name)
            image=image.convert('RGB')
            text = pytesseract.image_to_string(image)

            if search_word in text :
                pic_text1 = 'Results found in file '+ name
                img = cv.imread(name)
                cv_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(cv_gray, cv_coef) #1.35
                crops = []
                if faces == () :
                    image3 = Image.new('RGB', (500, top_margin), (255,255,255))
                    d2 = ImageDraw.Draw(image3)
                    d2.text((0,0), pic_text2, font=font, fill=(0,0,0,255))
                    total_list.append(addTopMargin(image3, top_margin, font, pic_text1))
                else :
                    for x,y,w,h in faces:
                        crops.append(image.crop((x,y,x+w,y+h)))
                    max_img = crops[0]
                    j = 0
                    i = 0
                    for img in crops :
                        if img.width > max_img.width :
                            max_img = img
                            i = j
                        j += 1
                    crops.pop(i)
                    crops.insert(0, max_img)
                    #building contact sheet of images
                    matrix_height = math.ceil(len(crops)/5)
                    first_image=crops[0]
                    contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*5,first_image.height*matrix_height))
                    x=0
                    y=0
                    for img in crops:
                        # Lets paste the current image into the contact sheet
                        img = img.resize((first_image.width, first_image.height))
                        contact_sheet.paste(img, (x, y) )
                        # Now we update our X position. If it is going to be the width of the image, then we set it to 0
                        # and update Y as well to point to the next "line" of the contact sheet.
                        if x+first_image.width == contact_sheet.width:
                            x=0
                            y=y+first_image.height
                        else:
                            x=x+first_image.width
                    contact_sheet.thumbnail((500,500), Image.ANTIALIAS)
                    total_list.append(addTopMargin(contact_sheet, top_margin, font, pic_text1))

    total_height = 0
    for pic in total_list:
        total_height += pic.height

    first_image = total_list[0]
    final_image = PIL.Image.new(first_image.mode, (first_image.width,total_height))
    y=0
    for pic in total_list:
        final_image.paste(pic, (0,y))
        y += pic.height
    return final_image
print("=================== SMALL FILE =======================")
display(compose_cs("readonly/small_img.zip", 'Christopher', 1.35))
print("=================== LARGE FILE ==================================")
display(compose_cs("readonly/images.zip", 'Mark', 1.35))
