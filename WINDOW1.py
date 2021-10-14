from tkinter import*
from PIL import Image,ImageTk
root = Tk()

#window title
root.title("FOOD HUNTER")
root.geometry("600x500")
root["bg"] = "#310054"

#image
load= Image.open("/Users/samiradeepak/Desktop/food_hunter_RE.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=159, y=100)

#order button
button_order = Button(root, text="Order")
button_order.place(x=210, y=435)
button_order["width"] = 20
button_order["fg"] = "#310054"

button_order["highlightbackground"] = "#00f3b2"
root.mainloop()