from pyfirmata import Arduino, SERVO, util
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import imutils
board= Arduino('/dev/cu.usbmodem1101')
import time
import cv2
import numpy as np



grip = board.get_pin('d:9:s')
link2 = board.get_pin('d:11:s')
link1 = board.get_pin('d:10:s')
base = board.get_pin('d:12:s')

grip.write(90)
link1.write(40)
link2.write(70)
base.write(90)

global allColorsList

def ColorSelection():
    clrSwin=Toplevel(window)
    clrSwin.geometry("400x160")
    clrSwin.title("Box's Color Picking")


    global allColorsList

    # allColorsList=[]
    def send_colorData():
        global allColorsList
        allColorsList = []
        # allColorsList = []
        # allColorsList=[
        if redP.get()==1:
            allColorsList.append('red')
        if blueP.get()==1:
            allColorsList.append('blue')


        # print(f'Selected Colors: {for i in range(0,len(AllowedClr))}')
        print("Selected Color/Colors ->")
        for i in range(0,len(allColorsList)):print(allColorsList[i])
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
    try:
        global allColorsList
        if len(allColorsList)>0:

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

                for angle in range(100, 121, 1):
                    grip.write(50)
                    link2.write(angle)
                    link1.write(58)
                    base.write(89)
                    time.sleep(0.1)

            def pick_Obj_red(sleep):
                for angle in range(55, 71, 1):
                    grip.write(angle)
                    link2.write(120)
                    link1.write(58)
                    base.write(90)
                    time.sleep(sleep)

            def pick_Obj_blue(sleep):
                for angle in range(55, 78, 1):
                    grip.write(angle)
                    link2.write(120)
                    link1.write(58)
                    base.write(90)
                    time.sleep(sleep)

            def place_Obj_red(sleep):
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
            def place_Obj_blue(sleep):
                for angle in range(124, 71, -1):
                    grip.write(77)
                    link2.write(angle)
                    link1.write(58)
                    base.write(90)
                    time.sleep(sleep)

                for angle in range(90, 56, 1):
                    grip.write(77)
                    link2.write(70)
                    link1.write(58)
                    base.write(angle)
                    time.sleep(sleep)

                for angle in range(70, 101, 1):
                    grip.write(77)
                    link2.write(angle)
                    link1.write(58)
                    base.write(55)
                    time.sleep(sleep)

                for angle in range(58, 46, -1):
                    grip.write(77)
                    link2.write(100)
                    link1.write(angle)
                    base.write(55)
                    time.sleep(sleep)

                for angle in range(100, 126, 1):
                    grip.write(77)
                    link2.write(angle)
                    link1.write(43)
                    base.write(55)
                    time.sleep(sleep)

                for angle in range(68, 55, -1):
                    grip.write(angle)
                    link2.write(125)
                    link1.write(45)
                    base.write(55)
                    time.sleep(0.1)

            def move_bake_red(sleep):
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

            def move_bake_blue(sleep):
                for angle in range(125, 100, -1):
                    grip.write(55)
                    link2.write(angle)
                    link1.write(45)
                    base.write(55)
                    time.sleep(sleep)



                grip.write(90)
                time.sleep(0.5)
                link2.write(70)
                time.sleep(0.5)
                link1.write(40)
                time.sleep(0.5)
                base.write(90)
                time.sleep(0.1)
            def start_():
                cap = cv2.VideoCapture(0)
                cap.set(3, 640)
                cap.set(4, 480)

                while True:
                    _, frame = cap.read()
                    frame=cv2.resize(frame,(400,500))
                    hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                    lower_red = np.array([0, 50, 120])
                    higher_red = np.array([10, 255, 255])

                    lower_blue = np.array([90, 60, 0])
                    higher_blue = np.array([121, 255, 255])

                    mask1 = cv2.inRange(hsvimg, lower_red, higher_red)
                    mask2 = cv2.inRange(hsvimg, lower_blue, higher_blue)

                    conts1 = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    conts1 = imutils.grab_contours(conts1)
                    conts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    conts2 = imutils.grab_contours(conts2)
                    done = 0
                    ObjectColor = ""
                    if 'red' in allColorsList:

                        for c in conts1:
                            area1 = cv2.contourArea(c)
                            if area1 > 5000:
                                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                                M = cv2.moments(c)

                                cx = int(M["m10"] / M["m00"])
                                cy = int(M["m01"] / M["m00"])

                                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                                ObjectColor = "Red"
                                cv2.putText(frame, "red", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)

                                print("Red box is found")
                                move_to_obj(0.08)
                                pick_Obj_red(0.01)
                                place_Obj_red(0.01)
                                move_bake_red(0.01)

                            else:
                                print("Red Box not exist")


                    if 'blue' in allColorsList:
                        for c in conts2:

                            area1 = cv2.contourArea(c)
                            if area1 > 5000:
                                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                                M = cv2.moments(c)

                                cx = int(M["m10"] / M["m00"])
                                cy = int(M["m01"] / M["m00"])

                                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                                ObjectColor = "Blue"
                                cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255),
                                            3)

                                print("Blue Box Detected")
                                move_to_obj(0.08)
                                pick_Obj_blue(0.1)
                                place_Obj_blue(0.01)
                                move_bake_blue(0.01)
                                done=1
                            else:
                                print("Blue Box not exist")


                    # print(ObjectColor)
                    cv2.imshow("result", frame)
                    # k = cv2.waitKey(1)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        camWin.destroy()
                        break

                cap.release()

            def stop_():
                camWin.destroy()

            camWin=Tk()
            camWin.geometry("400x100")
            camWin.title("Automatic Pick and Place")

            startBtn=Button(camWin,text="Start", command=start_, height=2,width=5).place(x=50,y=30)
            stopbtn = Button(camWin, text="Cancel", command=stop_, height=2, width=5).place(x=250, y=30)

            camWin.mainloop()


    except:
        messagebox.showerror("Error","Color is not Selected")
        print("Color is not Selected")
def exit_():
    window.destroy()

# Tkinter Window
window = Tk()
window.geometry("500x750")
window.resizable(width=False,height=False)




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
exitButton = Button(window, text="Exit", width=22, height=2, bg="#59788E", fg="black", command=exit_).place(x=254,y=600)
heading_barline = Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=645)
course_label= Label(window, text="  Course No || ECE 3200      ",fg='black', bg="#59788E").place(x=8, y=665)
course_name_label= Label(window, text="  Course Name || Electronics Project Design/Dev.",fg='black', bg="#59788E").place(x=190, y=665)
Lowerbarline = Label(window,text="-------------------------------------------------------------------------------",bg="#d0efff", fg="black").place(x=8,y=685)
copyright=Label(window,text="Copyright: Nashit [1809002] & Rajmin [1809031]",fg='black',bg="#d0efff").place(x=80, y=705)
# print(red.get())
window.mainloop()