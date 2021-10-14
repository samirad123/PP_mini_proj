from tkinter import*
root = Tk()

root.title("RESTAURANTS")
root.geometry("600x500")
root["bg"] = "#310054"


#restaurants title label
resto_label =  Label(root,text = "CHOOSE THE RESTAURANTS")
resto_label["fg"] = "#00f3b2"
resto_label["bg"] = "#310054"
resto_label["font"] = ("Calibri", 30,"underline")
resto_label.place(x = 100,y = 40 )

#mcd radiobutton
var = IntVar()
mcd_radiobutton = Radiobutton(root, text="Mcdonalds", value=1, variable = var ,bg="#310054",fg = "#00f3b2")
mcd_radiobutton["font"] = ("Calibri", 20)
mcd_radiobutton.place(x=250,y=100)

#kfc radiobutton
kfc_radiobutton = Radiobutton(root, text="KFC", value=2,  variable = var ,bg="#310054",fg = "#00f3b2")
kfc_radiobutton["font"] = ("Calibri", 20)
kfc_radiobutton.place(x=250,y=150)

#Subway radiobutton
subway_radiobutton = Radiobutton(root, text="Subway", value=3,  variable = var ,bg="#310054",fg = "#00f3b2")
subway_radiobutton["font"] = ("Calibri", 20)
subway_radiobutton.place(x=250,y=200)

#Starbucks radiobutton
starbucks_radiobutton = Radiobutton(root, text="Starbucks", value=4,  variable = var ,bg="#310054",fg = "#00f3b2")
starbucks_radiobutton["font"] = ("Calibri", 20)
starbucks_radiobutton.place(x=250,y=250)

#dunkin radiobutton
dunkin_radiobutton = Radiobutton(root, text="Dunkin'Donuts", value=5,  variable = var ,bg="#310054",fg = "#00f3b2")
dunkin_radiobutton["font"] = ("Calibri", 20)
dunkin_radiobutton.place(x=250,y=250)

#Burger King radiobutton
bking_radiobutton = Radiobutton(root, text="Burger King", value=6,  variable = var ,bg="#310054",fg = "#00f3b2")
bking_radiobutton["font"] = ("Calibri", 20)
bking_radiobutton.place(x=250,y=300)


#finish reservation button
finish_button = Button(root,text = "Finish Reservation")
finish_button["fg"] = "#00f3b2"
finish_button["highlightbackground"] = "#310054"
finish_button["font"] = ("Calibri", 20)
finish_button.place(x = 130,y = 380)

#continue to order button
continue_to_order = Button(root,text = "Continue to order")
continue_to_order["fg"] = "#00f3b2"
continue_to_order["highlightbackground"] = "#310054"
continue_to_order["font"] = ("Calibri", 20)
continue_to_order.place(x = 320,y = 380)














root.mainloop()