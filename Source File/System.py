from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
# import cv2
# import numpy as np


AllowedClr = []
def ColorSelection():
    clrSwin=Toplevel(window)
    clrSwin.geometry("400x160")

    global AllowedClr
    def send_colorData():
        AllowedClr=[]
        if redP.get()==1:
            AllowedClr.append('red')
        if blueP.get()==1:
            AllowedClr.append('blue')

        # print(f'Selected Colors: {for i in range(0,len(AllowedClr))}')
        print("Selected Color/Colors ->")
        for i in range(0,len(AllowedClr)):print(AllowedClr[i])
        clrSwin.destroy()



    redP = IntVar()
    blueP=IntVar()

    Caption=Label(clrSwin,text='\nPick Color/Colors which you want to detect:', fg='white', font=('cursive',15)).pack()
    RedBox = Checkbutton(clrSwin, text='Red', variable=redP, onvalue=1, offvalue=0)
    RedBox.place(x=44,y=50)
    BlueBox = Checkbutton(clrSwin, text='Blue', variable=blueP, onvalue=1, offvalue=0)
    BlueBox.place(x=42, y=80)


    button = Button(clrSwin, text='submit', command=send_colorData)
    button.place(x=150,y=110)
    clrSwin.mainloop()

def prev():
    pass

# Tkinter Window
window = Tk()
window.geometry("500x750")


window.title("Automatic Pick and Place Object using Robotic arm and OpenCV")
window.config(bg="#d0efff")

Soft_Heading = Label(window, text='\nAutomatic Pick and Place Object\nUsing Robotic Arm and OpenCV', font=('Cursive', 25), bg="#d0efff", fg="black").pack()
soft_details = Label(window, text='Object Sorting Based On Color', bg="#d0efff", fg="black").pack()
barline = Label(window, text="-------------------------------------------------------------------------------",bg="#d0efff",fg="black").pack()
# #
# # stp_1_Details = Label(window, text='[ Upload the Certificate Template ]', font=('Cursive', 12), bg="#d0efff").pack()
# #

cover_pic= Image.open('/Users/akhanda/Downloads/IMG_20221224_040138.jpg')
resized_Pic= cover_pic.resize((480,400))
Updated_cover_pic= ImageTk.PhotoImage(resized_Pic)

coverPhoto_label= Label(window, image=Updated_cover_pic).pack()


Object_Selection_btn = Button(window, text="Color Selection", width=23, height=2, bg="#59788E", fg="black", command=ColorSelection).place(x=8,y=550)
Manual_controlling_btn = Button(window, text="Manual Pick and Place", width=22, height=2, bg="#59788E", fg="black", command=prev).place(x=254,y=550)
Auto_controlling_btn = Button(window, text="Automatic Pick and Place", width=23, height=2, bg="#59788E", fg="black", command=prev).place(x=8,y=600)
Additional_features_btn = Button(window, text="Additional Features", width=22, height=2, bg="#59788E", fg="black", command=prev).place(x=254,y=600)
heading_barline = Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=645)
course_label= Label(window, text="  Course No || ECE 3200      ",fg='black', bg="#59788E").place(x=8, y=665)
course_name_label= Label(window, text="  Course Name || Electronics Project Design/Dev.",fg='black', bg="#59788E").place(x=190, y=665)
Lowerbarline = Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=685)
copyright=Label(window,text="Copyright: Nashit [1809002] & Rajmin [1809031]",fg='black',bg="#d0efff").place(x=80, y=705)
# print(red.get())
window.mainloop()
