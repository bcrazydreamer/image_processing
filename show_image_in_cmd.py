'''
Language: Python3
'''

import sys
from PIL import Image

pixel_symbol = "██"

'''
Used to scale image size
'''
def scale_image(img, new_width):
    (width, height) = img.size
    ratio = height/float(width)
    new_height = int(ratio * new_width)
    return img.resize((new_width, new_height))

'''
Convert in grayscale/black_and_white
'''
def convert_in_grayscale(img):
    return img.convert('L')


'''
Color function will color the simulated pixel block 
'''
def color(c,clr):
    if(type(clr) is tuple):
        c1,c2,c3 = str(clr[0]),str(clr[1]),str(clr[2])
        color_pixel = c1 + ";" + c2 + ";" + c3
        c = "\u001B[38;2;"+color_pixel+"m" + c + "\u001B[39m"
    else:
        c = '\u0020';
        if clr != 0:
            c = pixel_symbol
    return c

'''
Creates the array of pixel according to width
'''
def genrate_pixel_array(image, width):
    img_pxl = list(image.getdata())
    pxl_arr = []
    for i in range(0, len(img_pxl), width):
        pxl_arr.append(img_pxl[i:i + width])
    return pxl_arr


'''
Pixel simulator
'''
def simulate_pixel(pixel_array,width):
    simulated_output = ""
    for row in pixel_array:
        row_simulated_output = ""
        for pixel_set in row:
            row_simulated_output += color(pixel_symbol,pixel_set)
        row_simulated_output += "\n"
        simulated_output += row_simulated_output
    return simulated_output


'''
Image simulator
'''
def simulate_image(image,width):
    pixel_array = genrate_pixel_array(image,width)
    simulated_image = simulate_pixel(pixel_array,width)
    return simulated_image

'''
Process image or start of image processing
'''
def process_image(image_filepath,width=100,style="color"):
    image = None
    try:
        image = Image.open(image_filepath)
        image = scale_image(image,width)
        if style == "grayscale":
            image = convert_in_grayscale(image)
    except Exception as e:
        print("file not exist")
        return

    return simulate_image(image,width)

if __name__=='__main__':
    name = "sample_image.jpeg"
    width = 100
    image_path = name
    image = process_image(image_path,width,"color")
    print(image)
