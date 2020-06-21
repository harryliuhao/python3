# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:31:37 2020

@author: Hao
"""

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
training='readonly/haarcascade_frontalface_default.xml'

zf=zipfile.ZipFile('readonly/small_img.zip','r')
zf.extractall('training')
zf.close()

zf=zipfile.ZipFile('readonly/images.zip','r')
zf.extractall('images')
zf.close()


def create_contact_sheet(images,thumbnail_size):    
    first_image=images[0]
    col_num=5
    row_num=math.ceil(len(images)/col_num)
    contact_sheet=PIL.Image.new(first_image.mode, (thumbnail_size*col_num,thumbnail_size*row_num))
    x=0
    y=0
    
    for img in images:

        contact_sheet.paste(img, (x, y) )
        if x+thumbnail_size == contact_sheet.width:
            x=0
            y=y+thumbnail_size
        else:
            x=x+thumbnail_size
    
    # resize and display the contact sheet
    #contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
    display(contact_sheet)
    
def create_faces(img):
    # loading the face detection classifier
    face_cascade = cv.CascadeClassifier(training)
    faces = (face_cascade.detectMultiScale(np.array(img),scaleFactor,minNeighbors)).tolist()

    face_lst=[]    
    for face in faces:
        rec=[face[0],face[1],face[0]+face[2],face[1]+face[3]]
        img_crop=img.crop(rec)
        img_crop.thumbnail((thumbnail_size,thumbnail_size))
        face_lst.append(img_crop)
    return face_lst

def search_face(folder,word):
    training_lst=os.listdir(folder)
    dict_f={folder+'/'+fname:pytesseract.image_to_string(folder+'/'+fname) for fname in training_lst }
    
    for f,t in dict_f.items():
        if word in t:
            print('Results found in file',f)
            img=Image.open(f)
            face_lst=create_faces(img)
            if len(face_lst)>0:
                create_contact_sheet(face_lst,thumbnail_size)
            else:
                print('But there were no faces in that file!')
                
search_face('training','Christopher')
search_face('images','Mark')