from email.mime import image
import tkinter as tk

root = tk.Tk()
root.geometry("900x450+500+200")
root.title("Aprendiendo Tkinter")
root.iconbitmap("GUI\images\codemy.ico")

#Images
my_img1 = tk.PhotoImage(file="GUI/images/aspen.png")
#my_img2 = tk.PhotoImage(file="GUI/images/aspenhospital.jpg")
my_img3 = tk.PhotoImage(file="GUI/images/me1.png")
my_img4 = tk.PhotoImage(file="GUI/images/me2.png")
my_img5 = tk.PhotoImage(file="GUI/images/me3.png")

image_list = [my_img1, my_img3, my_img4, my_img5]


canvas = tk.Canvas(root, width=700, height=400)
canvas.create_image(250, 200, image=my_img1)
canvas.grid(row=0, column=0)

#Buttons
button_quit = tk.Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=0)





root.mainloop()