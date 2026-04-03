import tkinter as tk #import Tkinter for GUI
import qrcode # import qr library to generate QR code 
from PIL import Image,ImageTk #import Pillow to display image 
from tkinter import colorchooser #import colorchooser for seleting QR color
import os


#TODO : default Qr color
qr_color="black"


def color_chooser():
    global qr_color
    color=colorchooser.askcolor()[1]
    if color:
        qr_color = color
       


def generate_Qr():
    qr_data=inputboxValue.get()
    if qr_data =="":
        print ("please enter some data")
        return

        
    
    filename = filename_entry.get()
    if filename == "":
        filename = "qr_code"

    #create folder
    if not os.path.exists("image"):
        os.makedirs("image")
    
    #ceate filename
    count = 0
    new_filename = filename

    while os.path.exists(f"image/{new_filename}.png"):
        count += 1
        new_filename = f"{filename}_{count}"

   
    #qr code size
    qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color= qr_color, back_color="white")
    
    img.save(f"image/{new_filename}.png")
    print("Qr code is generated successfully")
    qr_image=Image.open(f"image/{new_filename}.png")
    qr_image = qr_image.resize((250,250))
    qr_photo= ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

#TODO : main gui

root=tk.Tk()
root.configure(bg="#7DAACB")
root.title("Qr Generator") 
root.geometry("600x1000")
title_Label =tk.Label(root,text="QR GENERATOR APP",borderwidth=18,fg="black",font="ariel 25 bold",)
title_Label.pack(padx=12,pady=12)
inputbox =tk.Label(root, text="Enter text or URL",font="lucida 15 bold",fg="black")

inputbox.pack (padx=10,pady=10)

inputboxValue =tk.StringVar()
inputboxEntry =tk.Entry(root, textvariable=inputboxValue,font="lucida 16 ",width=25)
inputboxEntry.pack(padx=11,pady=11)

filename_label =tk.Label(root,text="Enter a file Name: ",font="lucida 15 bold",fg="black")
filename_label.pack(pady=8)

filename_entry = tk.Entry(root, width = 25,font="lucida 16")
filename_entry.pack(pady=11,padx=11)

tk.Button(root,text="Select color",command=color_chooser,height=1,width=12).pack(padx=7,pady=7) 
tk.Button(root,text="Generate QR",command=generate_Qr,height=2,font="lucida 15",fg= "black",width=26).pack(padx=10,pady=10)

# empty_label=tk.Label(root,text="",bg="#C44A3A")
# empty_label.pack(pady=10)


qr_label=tk.Label(root,bg="#7DAACB")
qr_label.pack()

root.mainloop()
