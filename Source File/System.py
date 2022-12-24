import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
# import cv2
# import numpy as np

AllowedcolorList=[]

def ColorSelection():
    global AllowedcolorList
    clrSwin=tk.Tk()
    clrSwin.geometry("400x400")
    clrSwin.title("Color Selection")
    clrSwin.config(bg="#d0efff")


    def FinalColorList():
        global AllowedcolorList
        AllowedcolorList= {'Red':Red.get(), 'Green':Green.get(), 'Blue': Blue.get(), "Yellow":Yellow.get()}
        print(AllowedcolorList)

    Red = tk.StringVar()
    Green= tk.StringVar()
    Blue=tk.StringVar()
    Yellow=tk.StringVar()



    ttk.Checkbutton(clrSwin,
                    text='Red Color',
                    variable=Red, onvalue='1',offvalue='0').pack()
    ttk.Checkbutton(clrSwin,
                    text='Blue Color',
                    variable=Blue).pack()
    ttk.Checkbutton(clrSwin,
                    text='Green Color',
                    variable=Green).pack()
    ttk.Checkbutton(clrSwin,
                    text='Yellow Color',
                    variable=Yellow).pack()

    doneButton= tk.Button(clrSwin, text='Done', command=FinalColorList).pack()
    clrSwin.mainloop()


def prev():
    pass

# Tkinter Window
window = tk.Tk()
window.geometry("500x750")

window.title("Automatic Pick and Place Object using Robotic arm and OpenCV")
window.config(bg="#d0efff")

Soft_Heading = tk.Label(window, text='\nAutomatic Pick and Place Object\nUsing Robotic Arm and OpenCV', font=('Cursive', 25), bg="#d0efff", fg="black").pack()
soft_details = tk.Label(window, text='Object Sorting Based On Color', bg="#d0efff", fg="black").pack()
barline = tk.Label(window, text="-------------------------------------------------------------------------------",bg="#d0efff",fg="black").pack()
# #
# # stp_1_Details = Label(window, text='[ Upload the Certificate Template ]', font=('Cursive', 12), bg="#d0efff").pack()
# #

cover_pic= Image.open('/Users/akhanda/Downloads/IMG_20221224_040138.jpg')
resized_Pic= cover_pic.resize((480,400), Image.ANTIALIAS)
Updated_cover_pic= ImageTk.PhotoImage(resized_Pic)

coverPhoto_label= tk.Label(window, image=Updated_cover_pic).pack()


Object_Selection_btn = tk.Button(window, text="Color Selection", width=23, height=2, bg="#59788E", fg="black", command=ColorSelection).place(x=8,y=550)
Manual_controlling_btn = tk.Button(window, text="Manual Pick and Place", width=22, height=2, bg="#59788E", fg="black", command=prev).place(x=254,y=550)
Auto_controlling_btn = tk.Button(window, text="Automatic Pick and Place", width=23, height=2, bg="#59788E", fg="black", command=prev).place(x=8,y=600)
Additional_features_btn = tk.Button(window, text="Additional Features", width=22, height=2, bg="#59788E", fg="black", command=prev).place(x=254,y=600)
barline = tk.Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=645)
course_label= tk.Label(window, text="  Course No || ECE 3200      ",fg='black', bg="#59788E").place(x=8, y=665)
course_name_label= tk.Label(window, text="  Course Name || Electronics Project Design/Dev.",fg='black', bg="#59788E").place(x=190, y=665)
barline = tk.Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=685)
copyright=tk.Label(window,text="Copyright: Nashit [1809002] & Rajmin [1809031]",fg='black',bg="#d0efff").place(x=80, y=705)

window.mainloop()
