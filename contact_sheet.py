import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# add black margin at the bottom
bottom_margin = 50
width, height = image.size
new_height = height + bottom_margin
image2 = Image.new(image.mode, (width, new_height), (0,0,0))
image2.paste(image)

images=[]
koefs = [0.1, 0.5, 0.9]
channels = [0,1,2]
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 60)

# build a list of pictures
for chan in channels :
    for koef in koefs :
        tech_im = image2.copy()
        d = ImageDraw.Draw(tech_im)
        d.text((0,450), "channel {} intensity {}".format(chan, koef), font=font)
        c_list = list(tech_im.split())
        c_list[chan] = c_list[chan].point(lambda i : i* koef)
        result = Image.merge('RGB', (c_list[0], c_list[1], c_list[2]))
        images.append(result)


first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
