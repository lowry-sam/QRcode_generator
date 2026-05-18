import qrcode 
from colors import colors
import re
from colorama import Fore, Back, Style
import os
from PIL import Image

color_list = colors.keys()

from gui import QRCode
text=QRCode.file_name
file_name=QRCode.file_name
color=QRCode.chosen_color

def my_function (text, file_name, color):
    qr = qrcode.QRCode(
        version = 1, 
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 20, 
        border = 2,
    )
    qr.add_data(text)
    qr.make(fit = True)

    if(color==""):
        while True:
            color = input("What color do you want it to be? ")
            color = color.lower()
            color = re.sub(r'\d+','',color)
            color = ''.join([char for char in color if char.isalnum()])
            color_split = color.split(" ")
            
            try: 
                img = qr.make_image(fill_color=color, back_color='white')
                break;
                    
            except ValueError:
                potential_colors = []
                
                for element in color_list:
                    for split_element in color_split:
                        if split_element in element:
                            potential_colors.append(element)
                
                if (len(potential_colors) > 0): 
                    print("That is not a proper color. But here is a list of similar colors:")
                    for first, second, third in zip(
                        potential_colors[::3], potential_colors[1::3], potential_colors[2::3]
                    ): 
                        column = ""
                        column = column + '- ' + first + '\t'
                        if len(first) <  6: column = column + '\t\t'
                        elif (len(first) < 14): column = column + '\t'
                        column = column + '- ' + second + '\t'
                        if len(second) <  6: column = column + '\t\t'
                        elif (len(second) < 14): column = column + '\t'
                        column = column + '- ' + third
                        print (column)
                else: print("There were no colors that are similar, please try another.")
    else:
        img = qr.make_image(fill_color=color, back_color='white')
                
    os.makedirs("generated_codes", exist_ok=True)        
    img.save(os.path.join("generated_codes", file_name))
    img.show()

if not(QRCode.file_name == "" or QRCode.website == ""):
    my_function(text,file_name,color)
#website = input("Please entire your URL: ")
#file_name = input("What do you want the QR code to be called? ") + ".png"

#my_function(website, file_name, "")
#functionB()
#my_function(websites, name, "")
#print("QR code saved under " + file_name)