import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Sign Language Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open("img6.jpg")
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Sign Language Recognisation",font=("Curlz MT", 35, 'bold'),
                    background="#0000A0", fg="white", width=65, height=1)
label_l1.place(x=0, y=30)


def voice():
    from subprocess import call
    call(["python","main1.py"])

def text():
    from subprocess import call
    call(["python","main2.py"])

def log():
    from subprocess import call
    call(["python","fun_util.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Text Recognize", command=voice, width=18, height=1,font=('Curlz MT', 20, ' bold '), bg="#0000A0", fg="white")
button1.place(x=130, y=200)

button2 = tk.Button(root, text="Gesture Recognisation",command=log,width=18, height=1,font=('Curlz MT', 20, ' bold '), bg="#0000A0", fg="white")
button2.place(x=130, y=300)

button1 = tk.Button(root, text="Voice Recognize", command=text, width=18, height=1,font=('Curlz MT', 20, ' bold '), bg="#0000A0", fg="white")
button1.place(x=130, y=400)

button3 = tk.Button(root, text="Exit", command=window, width=18, height=1,font=('Curlz MT', 20, ' bold '), bg="red", fg="white")
button3.place(x=130, y=500)


root.mainloop()