import os
from PIL import Image, ImageDraw
import PIL
import pytesseract
import cv2 as cv
import math
import numpy as np
import zipfile

scaleFactor=1.25
minNeighbors=5
thumbnail_size=120

training='C:\\Users\Hao\\Documents\\github\\python3\\haarcascade_frontalface_default.xml'
test='C:\\Users\Hao\\Documents\\github\\python3\\small_img.zip'
#training='readonly/haarcascade_frontalface_default.xml'
os.chdir('C:\\Users\Hao\\Documents\\github\\python3\\')
os.getcwd()

img_path='C:\\Users\Hao\\Documents\\github\\python3\\test1.png'

def create_contact_sheet(images,thumbnail_size):    
    first_image=images[0]
    col_num=5
    row_num=math.ceil(len(images)/col_num)
    contact_sheet=PIL.Image.new(first_image.mode, (thumbnail_size*col_num,thumbnail_size*row_num))
    x=0
    y=0
    
    for img in images:
        # Lets paste the current image into the contact sheet
        contact_sheet.paste(img, (x, y) )
        # Now we update our X position. If it is going to be the width of the image, then we set it to 0
        # and update Y as well to point to the next "line" of the contact sheet.
        if x+thumbnail_size == contact_sheet.width:
            x=0
            y=y+thumbnail_size
        else:
            x=x+thumbnail_size
    
    # resize and display the contact sheet
    #contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
    display(contact_sheet)
    
def create_faces(img):
    face_cascade = cv.CascadeClassifier(training)
    faces = (face_cascade.detectMultiScale(np.array(img),scaleFactor,minNeighbors)).tolist()

    face_lst=[]    
    for face in faces:
        rec=[face[0],face[1],face[0]+face[2],face[1]+face[3]]
        img_crop=img.crop(rec)
        img_crop.thumbnail((thumbnail_size,thumbnail_size))
        face_lst.append(img_crop)
    return face_lst

#image=Image.open('/home/hao/Pictures/test.png')
image=Image.open(img_path)
t=pytesseract.image_to_string(image)

# loading the face detection classifier


img=cv.imread(img_path)
"""
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
pil_img=Image.fromarray(gray,mode="L")
drawing=ImageDraw.Draw(pil_img)
"""

face_lst=create_faces(img)
create_contact_sheet(face_lst,thumbnail_size)


folder='test'
training_lst=os.listdir(folder)

dict_f={folder+'/'+fname:pytesseract.image_to_string(folder+'/'+fname) for fname in training_lst }


word='Christopher'

for f,t in dict_f.items():
        print('Results found in file',f)
        #img=cv.imread(f)
        img=Image.open(f)
        display(img)
        face_lst=create_faces(img)
        create_contact_sheet(face_lst,thumbnail_size)
