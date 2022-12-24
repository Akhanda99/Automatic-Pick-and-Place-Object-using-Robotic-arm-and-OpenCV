
from pyfirmata import Arduino, SERVO, util
from tkinter import *
from PIL import Image, ImageTk
board= Arduino('/dev/cu.usbmodem1101')
import time
import cv2
import numpy as np


AllowedClr = []

grip = board.get_pin('d:9:s')
link2 = board.get_pin('d:11:s')
link1 = board.get_pin('d:10:s')
base = board.get_pin('d:12:s')

grip.write(90)
link1.write(40)
link2.write(70)
base.write(90)



def ColorSelection():
    clrSwin=Toplevel(window)
    clrSwin.geometry("400x160")
    clrSwin.title("Box's Color Picking")

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

    Caption=Label(clrSwin,text='\nPick Box Color/Colors which have to detect:', fg='black', font=('cursive',15)).pack()
    RedBox = Checkbutton(clrSwin, text='Red', variable=redP, onvalue=1, offvalue=0)
    RedBox.place(x=44,y=50)
    BlueBox = Checkbutton(clrSwin, text='Blue', variable=blueP, onvalue=1, offvalue=0)
    BlueBox.place(x=42, y=80)


    button = Button(clrSwin, text='submit', command=send_colorData)
    button.place(x=150,y=110)
    clrSwin.mainloop()

def manual_pp():

    iter8 = util.Iterator(board)
    iter8.start()
    def gripper_move(a):
        # board.digital[pin].write(a)
        grip.write(a)

    def joint1_move(a):
        # board.digital[pin].write(a)
        link1.write(a)

    def joint2_move(a):
        # board.digital[pin].write(a)
        link2.write(a)

    def base_move(a):
        # board.digital[pin].write(a)
        base.write(a)

    def resetVal():
        gripper_scale.set(90)
        time.sleep(0.015)
        joint1_scale.set(40)
        time.sleep(0.015)
        joint2_scale.set(70)
        time.sleep(0.015)
        Base_scale.set(90)


    manControlWin = Tk()
    manControlWin.geometry('430x360')
    manControlWin.title("Manual Picking and Placing")
    CaptionLabel=Label(manControlWin,text="\nManual Pick and Place: ",font=('cursive',20),fg='black').pack()
    barline = Label(manControlWin, text="------------------------------------------------------------------",
                    fg="black").pack()

    gripper_scale = Scale(manControlWin, command=gripper_move, from_=90, to=55, orient=HORIZONTAL, length=400, label='\nGripper: ')
    gripper_scale.set(90)
    gripper_scale.pack(anchor=CENTER)
    joint1_scale = Scale(manControlWin, command=joint1_move, from_=20, to=180, orient=HORIZONTAL, length=400, label='\nJoint1: ')
    joint1_scale.set(40)
    joint1_scale.pack(anchor=CENTER)
    joint2_scale = Scale(manControlWin, command=joint2_move, from_=20, to=180, orient=HORIZONTAL, length=400, label='\nJoint2: ')
    joint2_scale.set(70)
    joint2_scale.pack(anchor=CENTER)
    Base_scale = Scale(manControlWin, command=base_move, from_=20, to=180, orient=HORIZONTAL, length=400, label='\nBase: ')
    Base_scale.set(90)
    Base_scale.pack(anchor=CENTER)

    ResetButton=Button(manControlWin,text="Reset", command=resetVal).place(x=180,y=320)
    manControlWin.mainloop()



def auto_pp():

    def move_to_obj(sleep):
        for angle in range(70, 101, 1):
            grip.write(90)
            link2.write(angle)
            link1.write(40)
            base.write(89)
            time.sleep(sleep)

        for angle in range(40, 59, 1):
            grip.write(90)
            link2.write(100)
            link1.write(angle)
            base.write(89)
            time.sleep(sleep)

        for angle in range(90, 50, -1):
            grip.write(angle)
            link2.write(100)
            link1.write(58)
            base.write(89)
            time.sleep(sleep)

        for angle in range(100, 125, 1):
            grip.write(50)
            link2.write(angle)
            link1.write(58)
            base.write(89)
            time.sleep(0.1)

    def pick_Obj(sleep):
        for angle in range(55, 71, 1):
            grip.write(angle)
            link2.write(124)
            link1.write(58)
            base.write(90)
            time.sleep(sleep)

    def place_Obj(sleep):
        for angle in range(124, 71, -1):
            grip.write(70)
            link2.write(angle)
            link1.write(58)
            base.write(90)
            time.sleep(sleep)

        for angle in range(90, 125, 1):
            grip.write(70)
            link2.write(70)
            link1.write(58)
            base.write(angle)
            time.sleep(sleep)

        for angle in range(70, 101, 1):
            grip.write(70)
            link2.write(angle)
            link1.write(58)
            base.write(125)
            time.sleep(sleep)

        for angle in range(58, 46, -1):
            grip.write(70)
            link2.write(100)
            link1.write(angle)
            base.write(125)
            time.sleep(sleep)

        for angle in range(100, 126, 1):
            grip.write(70)
            link2.write(angle)
            link1.write(43)
            base.write(125)
            time.sleep(sleep)

        for angle in range(68, 55, -1):
            grip.write(angle)
            link2.write(125)
            link1.write(45)
            base.write(125)
            time.sleep(0.1)

    def move_bake(sleep):
        for angle in range(125, 100, -1):
            grip.write(55)
            link2.write(angle)
            link1.write(45)
            base.write(125)
            time.sleep(sleep)


        grip.write(90)
        time.sleep(0.5)
        link2.write(70)
        time.sleep(0.5)
        link1.write(40)
        time.sleep(0.5)
        base.write(90)
        time.sleep(0.1)

    move_to_obj(0.08)
    pick_Obj(0.01)
    place_Obj(0.01)
    move_bake(0.01)


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


Object_Clr_Selection_btn = Button(window, text="Box Color Selection", width=23, height=2, bg="#59788E", fg="black", command=ColorSelection).place(x=8,y=550)
Manual_controlling_btn = Button(window, text="Manual Pick and Place", width=22, height=2, bg="#59788E", fg="black", command=manual_pp).place(x=254,y=550)
Auto_controlling_btn = Button(window, text="Automatic Pick and Place", width=23, height=2, bg="#59788E", fg="black", command=auto_pp).place(x=8,y=600)
Additional_features_btn = Button(window, text="Additional Features", width=22, height=2, bg="#59788E", fg="black", command=prev).place(x=254,y=600)
heading_barline = Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=645)
course_label= Label(window, text="  Course No || ECE 3200      ",fg='black', bg="#59788E").place(x=8, y=665)
course_name_label= Label(window, text="  Course Name || Electronics Project Design/Dev.",fg='black', bg="#59788E").place(x=190, y=665)
Lowerbarline = Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=685)
copyright=Label(window,text="Copyright: Nashit [1809002] & Rajmin [1809031]",fg='black',bg="#d0efff").place(x=80, y=705)
# print(red.get())
window.mainloop()
