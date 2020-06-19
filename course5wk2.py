from PIL import Image
import pytesseract
print('hello')
image=Image.open('/home/hao/Pictures/test.png')
display(image)
dir(pytesseract)
help(Image.Image.resize)
import inspect
src=inspect.getsource(pytesseract.image_to_string)
print(src)
pytesseract.image_to_string??
t=pytesseract.image_to_string(image)
