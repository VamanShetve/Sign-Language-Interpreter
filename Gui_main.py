# import tkinter as tk
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.configure(background="white")
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
# root.title("hello")

# image2 = Image.open("1.jpg")
# image2 = image2.resize((w, h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)

# label = tk.Label(
#     root,
#     text="Sign language Detection System",
#     font=("Calibri", 45),
#     bg="purple",
#     width=55,
#     height=1,
# )
# label.place(x=0, y=0)


# def shift():
#     x1, y1, x2, y2 = canvas.bbox("marquee")
#     if x2 < 0 or y1 < 0:  # reset the coordinates
#         x1 = canvas.winfo_width()
#         y1 = canvas.winfo_height() // 2
#         canvas.coords("marquee", x1, y1)
#     else:
#         canvas.move("marquee", -2, 0)
#     canvas.after(1000 // fps, shift)


# canvas = tk.Canvas(root, bg="black")
# canvas.pack()
# canvas.place(x=0, y=0)
# text_var = "Sign language Detection System"
# text = canvas.create_text(
#     0,
#     -2000,
#     text=text_var,
#     font=("Raleway", 25, "bold"),
#     fill="white",
#     tags=("marquee",),
#     anchor="w",
# )
# x1, y1, x2, y2 = canvas.bbox("marquee")
# width = 1600
# height = 80
# canvas["width"] = width
# canvas["height"] = height
# fps = 40  # Change the fps to make the animation faster/slower
# shift()  # Function Calling


# def log():
#     from subprocess import call

#     call(["python", "login.py"])


# btn = tk.Button(
#     root,
#     text="Login",
#     command=log,
#     font=("Arial", 15),
#     width=7,
#     bg="light gray",  # fg="white",
# )
# btn.place(x=1080, y=400)


# def reg():
#     from subprocess import call

#     call(["python", "registration.py"])


# btn = tk.Button(
#     root,
#     text="Register",
#     command=reg,
#     font=("Arial", 15),
#     width=7,
#     bg="light gray",
#     # fg="white",
# )
# btn.place(x=1220, y=400)


# register1 = tk.Label(root, text="Kindly register here....", font=("Cambria", 10)).place(
#     x=1230, y=350
# )


# root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

root = tk.Tk()
root.configure(background="white")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("hello")

image2 = Image.open("1.jpg")
image2 = image2 = image2.resize((w, h), resample=ImageFilter.LANCZOS)  # Use LANCZOS resampling method
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

label = tk.Label(
    root,
    text="Sign language Detection System",
    font=("Calibri", 45),
    bg="purple",
    width=55,
    height=1,
)
label.place(x=0, y=0)


def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if x2 < 0 or y1 < 0:  # reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, shift)


canvas = tk.Canvas(root, bg="black")
canvas.pack()
canvas.place(x=0, y=0)
text_var = "Sign language Detection System"
text = canvas.create_text(
    0,
    -2000,
    text=text_var,
    font=("Raleway", 25, "bold"),
    fill="white",
    tags=("marquee",),
    anchor="w",
)
x1, y1, x2, y2 = canvas.bbox("marquee")
width = 1600
height = 80
canvas["width"] = width
canvas["height"] = height
fps = 40  # Change the fps to make the animation faster/slower
shift()  # Function Calling


def log():
    from subprocess import call

    call(["python", "login.py"])


btn = tk.Button(
    root,
    text="Login",
    command=log,
    font=("Arial", 15),
    width=7,
    bg="light gray",  # fg="white",
)
btn.place(x=1080, y=400)


def reg():
    from subprocess import call

    call(["python", "registration.py"])


btn = tk.Button(
    root,
    text="Register",
    command=reg,
    font=("Arial", 15),
    width=7,
    bg="light gray",
    # fg="white",
)
btn.place(x=1220, y=400)


register1 = tk.Label(root, text="Kindly register here....", font=("Cambria", 10)).place(
    x=1230, y=350
)

root.mainloop()
