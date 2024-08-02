#pip install pillow

from PIL import Image

def resizing(size1,size2):
    image = Image.open('image location name') #here is not location

    print(f"current size:{image.size}")

    rezied = image.resize((size1,size2))

    rezied.save('location to save the image')

size1 = int(input('enter size 1'))
size2 = int(input('enter size 2'))


resizing(size1,size2)