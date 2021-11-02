from tkinter import *
from tkinter import messagebox
from PIL import Image
import random
from PIL import Image




# tkinter name instance
root = Tk()

#setting the windows size
root.geometry("1000x300")
root.configure(bg='gray')




def get_file():
    global my_image

    filename = input("Please give it a file name")
    my_image = Image.open(filename)

get_file()



def My_image():

    rows = my_image.size[0]
    cols = my_image.size[1]
    print("Image info")
    print(rows, " by ", cols)
    px = my_image.load()
    px[9, 9] = (0, 0, 0)

    # px[0,9] = (0, 0, 0)
    # px[0,0] = (0, 0, 0)
    # px[9,0] = (0, 0, 0)
    for i in range(0, rows):
        start = random.randint(3, rows)
        end = random.randint(6, cols)
        nub = random.randint(1, 2)

        if i % 9 == 0:
            start = 0
        else:
            start = i

        for j in range(start, cols, nub):
            #red = random.randint(200, 255)
            #green = random.randint(1, 255)
            #blue = random.randint(1, 255)
            red_str = red_slider.get()
            red = int(red_str)
            green_str = green_slider.get()
            green = int(green_str)
            blue_str = blue_slider.get()
            blue = int(blue_str)
            px[i, j] = (red, green, blue)

    my_image.show()


#button
Glitch_it = Button(root, text='Glitch it', command=My_image)
Glitch_it.grid(row=2, column=3)


red_slider = Scale(root, from_= 0, to=255,  orient=VERTICAL)
red_slider.grid(row=2, column=7)

blue_slider = Scale(root, from_= 0, to=255, orient=VERTICAL)
blue_slider.grid(row=2, column=8)

green_slider = Scale(root, from_= 0, to=255, orient=VERTICAL)
green_slider.grid(row=2, column=9)

print(green_slider.get())

root.mainloop()






