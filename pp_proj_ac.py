import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def show_frame(frame):
    frame.tkraise()


root = tk.Tk()

root.state('zoomed')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root)#logo
frame2 = tk.Frame(root)#register form
frame3 = tk.Frame(root)#Choose resto
frame7 = tk.Frame(root)#mcd menu
frame7 = tk.Frame(root)#kfc menu
frame7 = tk.Frame(root)#dunkin menu
frame7 = tk.Frame(root)#bill


for frame in (frame1, frame2, frame3, frame7, frame7, frame7, frame7):
    frame.grid(row=0, column=0, sticky='nsew')

# ==================Frame 1 code
# window title
root.title("FOOD HUNTER")
root.geometry("600x500")
root["highlightbackground"] = "#00f3b2"

# baground
bg_label_f1 = Label(frame1, bg="#310054")
bg_label_f1.pack(fill='both', expand=True)

# image
img = Image.open("/Users/samiradeepak/Desktop/food_hunter_RE.png")
logo_pic = ImageTk.PhotoImage(img)
logo_label = tk.Label(frame1, image=logo_pic)
logo_label.place(x=159, y=100)

# order button
button_order = tk.Button(frame1, text="Order", command=lambda: show_frame(frame2))
button_order.place(x=210, y=435)
button_order["width"] = 20
button_order["fg"] = "#310054"
button_order["highlightbackground"] = "#00f3b2"

# ==================Frame 2 code
# window title
root.geometry("600x500")

# baground
bg_label_f2 = tk.Label(frame2, bg="#310054")
bg_label_f2.pack(fill='both', expand=True)

# Registration Form Label
registration_form_label = tk.Label(frame2, text="Registration Form")
registration_form_label.place(x=180, y=60)

# dictionary attributes for label
registration_form_label["font"] = ("Calibri", 30)
registration_form_label["fg"] = "#00f3b2"
registration_form_label["bg"] = "#310054"

# Fullname Label
fullname_label = tk.Label(frame2, text="FULL NAME :")
fullname_label.place(x=70, y=130)
fullname_label["fg"] = "#00f3b2"
fullname_label["bg"] = "#310054"

# textbox - Entry text
fullname_entrytext = tk.Entry(frame2, borderwidth=3)
fullname_entrytext["fg"] = "#00f3b2"
fullname_entrytext["bg"] = "#310054"
fullname_entrytext.place(x=240, y=130)

# time(breakfast,lunch,dinner)
time_slot = tk.Label(frame2, text="TIME SLOT :")
time_slot["fg"] = "#00f3b2"
time_slot["bg"] = "#310054"
time_slot.place(x=70, y=210)

# creating optionmenu for time slots
list_of_slots = ["Breakfast : 8:00 a.m. - 11:00 a.m.", "Lunch : 1:00 p.m. - 3:00 p.m.",
                 "Dinner : 8:00 p.m. - 11:00 p.m."]
temp1 = StringVar()
slot_optionmenu = tk.OptionMenu(frame2, temp1, *list_of_slots)
slot_optionmenu.place(x=240, y=210)
slot_optionmenu["fg"] = "#00f3b2"
slot_optionmenu["bg"] = "#310054"
temp1.set("Select your time slot")

# location label
user_location = tk.Label(frame2, text="LOCATION :")
user_location["fg"] = "#00f3b2"
user_location["bg"] = "#310054"
user_location.place(x=70, y=280)

# creatting optionmenu for locations
list_of_states = ["Mumbai", "Delhi", "Bangalore", "Kolkata"]
temp = StringVar()
state_optionmenu = tk.OptionMenu(frame2, temp, *list_of_states)
state_optionmenu["fg"] = "#00f3b2"
state_optionmenu["bg"] = "#310054"
state_optionmenu.place(x=240, y=280)
temp.set("Select your state")

# number of people
num_ppl = tk.Label(frame2, text="NUMBER OF PEOPLE :")
num_ppl["fg"] = "#00f3b2"
num_ppl["bg"] = "#310054"
num_ppl.place(x=70, y=340)
num_spin = tk.Spinbox(frame2, from_=1, to=15, width=8)
num_spin["fg"] = "#00f3b2"
num_spin["bg"] = "#310054"
num_spin.place(x=240, y=340)

# Submit Button
button_submit = tk.Button(frame2, text="Submit", command=lambda: show_frame(frame3))
button_submit.place(x=180, y=380)
button_submit["width"] = 20
button_submit["fg"] = "#00f3b2"
button_submit["highlightbackground"] = "#310054"

# ==================Frame 3 code
root.geometry("800x900")
bg_label_f3 = tk.Label(frame3,bg = "#310054")
bg_label_f3.pack(fill='both', expand=True)

#restaurants title label
resto_label =  tk.Label(frame3,text = "CHOOSE THE RESTAURANTS")
resto_label["fg"] = "#00f3b2"
resto_label["bg"] = "#310054"
resto_label["font"] = ("Calibri", 30,"underline")
resto_label.place(x = 100,y = 40 )

#image mcd logo
mcd_logo = tk.PhotoImage(file ="/Users/samiradeepak/Desktop/mcd_logo (1).png")
mcd_logo_label = tk.Label(frame3, image = mcd_logo)
mcd_logo_label["highlightbackground"] = "#310054"
mcd_logo_label.place(x=100, y=100)

#mcd
mcd_label =  tk.Label(frame3,text = "Mcdonalds : ")
mcd_label["fg"] = "#00f3b2"
mcd_label["bg"] = "#310054"
mcd_label["font"] = ("Calibri", 14)
mcd_label.place(x = 230,y = 100)


#finish reservation button mcd
finish_button_mcd = tk.Button(frame3, text = "Finish Reservation", command=lambda:show_frame(frame7))
finish_button_mcd["fg"] = "#00f3b2"
finish_button_mcd["highlightbackground"] = "#310054"
finish_button_mcd["font"] = ("Calibri", 15)
finish_button_mcd.place(x = 230,y = 150)

#continue to order button mcd
continue_to_order_mcd = tk.Button(frame3, text = "Continue to order", command=lambda:show_frame(frame7))
continue_to_order_mcd["fg"] = "#00f3b2"
continue_to_order_mcd["highlightbackground"] = "#310054"
continue_to_order_mcd["font"] = ("Calibri", 15)
continue_to_order_mcd.place(x = 390,y = 150)

#image starbucks
star_logo = tk.PhotoImage(file ="/Users/samiradeepak/Desktop/starbucks_logo.png")
star_logo_label = tk.Label(frame3, image = star_logo)
star_logo_label["highlightbackground"] = "#310054"
star_logo_label.place(x=100, y=250)

#starbucks
star_label =  tk.Label(frame3,text = "Starbucks : ")
star_label["fg"] = "#00f3b2"
star_label["bg"] = "#310054"
star_label["font"] = ("Calibri", 14)
star_label.place(x = 220,y = 250 )


#finish reservation button starbuks
finish_button_star = tk.Button(frame3, text = "Finish Reservation", command=lambda:show_frame(frame7))
finish_button_star["fg"] = "#00f3b2"
finish_button_star["highlightbackground"] = "#310054"
finish_button_star["font"] = ("Calibri", 15)
finish_button_star.place(x = 220,y = 300)

#continue to order button starbucks
continue_to_order_star = tk.Button(frame3, text = "Continue to order", command=lambda:show_frame(frame7))
continue_to_order_star["fg"] = "#00f3b2"
continue_to_order_star["highlightbackground"] = "#310054"
continue_to_order_star["font"] = ("Calibri", 15)
continue_to_order_star.place(x = 390,y = 300)

#image dunkin
dunkin_logo = tk.PhotoImage(file ="/Users/samiradeepak/Desktop/dunkin_logo (2).png")
dunkin_logo_label = tk.Label(frame3, image = dunkin_logo)
dunkin_logo_label["highlightbackground"] = "#310054"
dunkin_logo_label.place(x=40, y=380)


#dunkin
dunkin_label =  tk.Label(frame3,text = "Dunkin'Donuts : ")
dunkin_label["fg"] = "#00f3b2"
dunkin_label["bg"] = "#310054"
dunkin_label["font"] = ("Calibri", 14)
dunkin_label.place(x = 220,y = 380 )


#finish reservation button dunkin
finish_button_dunkin = tk.Button(frame3, text = "Finish Reservation", command=lambda:show_frame(frame7))
finish_button_dunkin["fg"] = "#00f3b2"
finish_button_dunkin["highlightbackground"] = "#310054"
finish_button_dunkin["font"] = ("Calibri", 15)
finish_button_dunkin.place(x = 220,y = 430)

#continue to order button dunkin
continue_to_order_dunkin = tk.Button(frame3,text = "Continue to order",command=lambda:show_frame(frame7))
continue_to_order_dunkin["fg"] = "#00f3b2"
continue_to_order_dunkin["highlightbackground"] = "#310054"
continue_to_order_dunkin["font"] = ("Calibri", 15)
continue_to_order_dunkin.place(x = 390,y = 430)

# ==================Frame 4 code(MENU OF RESTO)

root.geometry("600x500")
bg_label_f4 = tk.Label(frame7, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

menu_label = tk.Label(frame7, text="MENU")
menu_label["fg"] = "#00f3b2"
menu_label["bg"] = "#310054"
menu_label["font"] = ("Calibri", 30, "underline")
menu_label.place(x=480, y=20)


def resto_selection():
    rest_value = var.get()
    print(rest_value)
    if rest_value == 1:
        lbl1 = tk.Label(frame7, text="BURGERS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl1.place(x=20, y=80)
        lbl5 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl5.place(x=280, y=80)
        lbl6 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl6.place(x=800, y=80)
        mcd1 = tk.Label(frame7, text="McSpicy Chicken", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd1.place(x=50, y=120)
        price_lbl1 = Label(frame7, text="Rs.170", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl1.place(x=315, y=120)
        mcd_label = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label.place(x=440, y=120)
        sb1 = Spinbox(frame7, from_=0, to=100, width=3)
        sb1.place(x=470, y=120)
        mcd2 = tk.Label(frame7, text="McSpicy Paneer", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd2.place(x=50, y=160)
        price_lbl2 = Label(frame7, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl2.place(x=315, y=160)
        mcd_label2 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label2.place(x=440, y=160)
        sb2 = Spinbox(frame7, from_=0, to=100, width=3)
        sb2.place(x=470, y=160)
        mcd3 = tk.Label(frame7, text="McVeggie", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd3.place(x=50, y=200)
        price_lbl3 = Label(frame7, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl3.place(x=315, y=200)
        mcd_label3 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label3.place(x=440, y=200)
        sb3 = Spinbox(frame7, from_=0, to=100, width=3)
        sb3.place(x=470, y=200)
        mcd4 = tk.Label(frame7, text="Mexican McAloo Tikki", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd4.place(x=50, y=240)
        price_lbl4 = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl4.place(x=315, y=240)
        mcd_label4 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label4.place(x=440, y=240)
        sb4 = Spinbox(frame7, from_=0, to=100, width=3)
        sb4.place(x=470, y=240)
        mcd5 = tk.Label(frame7, text="McAloo", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd5.place(x=50, y=280)
        price_lbl5 = Label(frame7, text="Rs.50", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl5.place(x=315, y=280)
        mcd_label5 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label5.place(x=440, y=280)
        sb5 = Spinbox(frame7, from_=0, to=100, width=3)
        sb5.place(x=470, y=280)
        mcd6 = tk.Label(frame7, text="Chicken Kebab Burger", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd6.place(x=50, y=320)
        price_lbl6 = Label(frame7, text="Rs.180", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl6.place(x=315, y=320)
        mcd_label6 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label6.place(x=440, y=320)
        sb6 = Spinbox(frame7, from_=0, to=100, width=3)
        sb6.place(x=470, y=320)
        lbl2 = tk.Label(frame7, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl2.place(x=20, y=380)
        mcd7 = tk.Label(frame7, text="Thums Up", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd7.place(x=50, y=420)
        price_lbl7 = Label(frame7, text="Rs.85", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl7.place(x=315, y=420)
        mcd_label7 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label7.place(x=440, y=420)
        sb7 = Spinbox(frame7, from_=0, to=100, width=3)
        sb7.place(x=470, y=420)
        mcd8 = tk.Label(frame7, text="Coke", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd8.place(x=50, y=460)
        price_lbl8 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl8.place(x=315, y=460)
        mcd_label8 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label8.place(x=440, y=460)
        sb8 = Spinbox(frame7, from_=0, to=100, width=3)
        sb8.place(x=470, y=460)
        mcd9 = tk.Label(frame7, text="Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd9.place(x=50, y=500)
        price_lbl9 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl9.place(x=315, y=500)
        mcd_label9 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label9.place(x=440, y=500)
        sb9 = Spinbox(frame7, from_=0, to=100, width=3)
        sb9.place(x=470, y=500)
        lbl3 = tk.Label(frame7, text="DESSERTS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl3.place(x=20, y=560)
        mcd10 = tk.Label(frame7, text="McSwirl", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd10.place(x=50, y=600)
        price_lbl10 = Label(frame7, text="Rs.30", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl10.place(x=315, y=600)
        mcd_label10 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label10.place(x=440, y=600)
        sb10 = Spinbox(frame7, from_=0, to=100, width=3)
        sb10.place(x=470, y=600)
        mcd11 = tk.Label(frame7, text="McFlurry", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd11.place(x=50, y=640)
        price_lbl11 = Label(frame7, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl11.place(x=315, y=640)
        mcd_label11 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label11.place(x=440, y=640)
        sb11 = Spinbox(frame7, from_=0, to=100, width=3)
        sb11.place(x=470, y=640)
        mcd12 = tk.Label(frame7, text="Soft Serve", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd12.place(x=50, y=680)
        price_lbl12 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl12.place(x=315, y=680)
        mcd_label12 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label12.place(x=440, y=680)
        sb12 = Spinbox(frame7, from_=0, to=100, width=3)
        sb12.place(x=470, y=680)
        lbl4 = tk.Label(frame7, text="FRIES & SIDES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl4.place(x=620, y=80)
        mcd13 = tk.Label(frame7, text="Regular Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd13.place(x=650, y=120)
        price_lbl13 = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl13.place(x=850, y=120)
        mcd_label13 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label13.place(x=960, y=120)
        sb13 = Spinbox(frame7, from_=0, to=100, width=3)
        sb13.place(x=990, y=120)
        mcd14 = tk.Label(frame7, text="Medium Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd14.place(x=650, y=160)
        price_lbl14 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl14.place(x=850, y=160)
        mcd_label14 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label14.place(x=960, y=160)
        sb14 = Spinbox(frame7, from_=0, to=100, width=3)
        sb14.place(x=990, y=160)
        mcd15 = tk.Label(frame7, text="Large Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd15.place(x=650, y=200)
        price_lbl15 = Label(frame7, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl15.place(x=850, y=200)
        mcd_label15 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label15.place(x=960, y=200)
        sb15 = Spinbox(frame7, from_=0, to=100, width=3)
        sb15.place(x=990, y=200)
        mcd16 = tk.Label(frame7, text="Masala Wedeges", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd16.place(x=650, y=240)
        price_lbl16 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl16.place(x=850, y=240)
        mcd_label16 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label16.place(x=960, y=240)
        sb16 = Spinbox(frame7, from_=0, to=100, width=3)
        sb16.place(x=990, y=240)
        mcd17 = tk.Label(frame7, text="Chicken Strips", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd17.place(x=650, y=280)
        price_lbl17 = Label(frame7, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl17.place(x=850, y=280)
        mcd_label17 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label17.place(x=960, y=280)
        sb17 = Spinbox(frame7, from_=0, to=100, width=3)
        sb17.place(x=990, y=280)
        mcd18 = tk.Label(frame7, text="McWings", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd18.place(x=650, y=320)
        price_lbl18 = Label(frame7, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl18.place(x=850, y=320)
        mcd_label18 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label18.place(x=960, y=320)
        sb18 = Spinbox(frame7, from_=0, to=100, width=3)
        sb18.place(x=990, y=320)

    elif rest_value == 2:
        lbl1 = tk.Label(frame7, text="CHICKEN:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl1.place(x=20, y=80)
        lbl5 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl5.place(x=280, y=80)
        lbl6 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl6.place(x=800, y=80)
        mcd1 = tk.Label(frame7, text="Big 8", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd1.place(x=50, y=120)
        price_lbl1 = Label(frame7, text="Rs.620", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl1.place(x=315, y=120)
        mcd_label = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label.place(x=440, y=120)
        sb1 = Spinbox(frame7, from_=0, to=100, width=3)
        sb1.place(x=470, y=120)
        mcd2 = tk.Label(frame7, text="Big 12", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd2.place(x=50, y=160)
        price_lbl2 = Label(frame7, text="Rs.730", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl2.place(x=315, y=160)
        mcd_label2 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label2.place(x=440, y=160)
        sb2 = Spinbox(frame7, from_=0, to=100, width=3)
        sb2.place(x=470, y=160)
        mcd3 = tk.Label(frame7, text="Bucket for 2", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd3.place(x=50, y=200)
        price_lbl3 = Label(frame7, text="Rs.600", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl3.place(x=315, y=200)
        mcd_label3 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label3.place(x=440, y=200)
        sb3 = Spinbox(frame7, from_=0, to=100, width=3)
        sb3.place(x=470, y=200)
        mcd4 = tk.Label(frame7, text="Ultimate Savings Bucket", bg="#310054", fg="#00f3b2",
                        font=['Calibri', 15, 'bold'])
        mcd4.place(x=50, y=240)
        price_lbl4 = Label(frame7, text="Rs.700", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl4.place(x=315, y=240)
        mcd_label4 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label4.place(x=440, y=240)
        sb4 = Spinbox(frame7, from_=0, to=100, width=3)
        sb4.place(x=470, y=240)
        lbl2 = tk.Label(frame7, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl2.place(x=20, y=300)
        mcd5 = tk.Label(frame7, text="Red Bull Energy Drink", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd5.place(x=50, y=340)
        price_lbl5 = Label(frame7, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl5.place(x=315, y=340)
        mcd_label5 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label5.place(x=440, y=340)
        sb5 = Spinbox(frame7, from_=0, to=100, width=3)
        sb5.place(x=470, y=340)
        mcd6 = tk.Label(frame7, text="Pepsi Can", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd6.place(x=50, y=380)
        price_lbl6 = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl6.place(x=315, y=380)
        mcd_label6 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label6.place(x=440, y=380)
        sb6 = Spinbox(frame7, from_=0, to=100, width=3)
        sb6.place(x=470, y=380)
        mcd7 = tk.Label(frame7, text="Miranda Can", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd7.place(x=50, y=420)
        price_lbl7 = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl7.place(x=315, y=420)
        mcd_label7 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label7.place(x=440, y=420)
        sb7 = Spinbox(frame7, from_=0, to=100, width=3)
        sb7.place(x=470, y=420)
        lbl3 = tk.Label(frame7, text="BURGERS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl3.place(x=20, y=480)
        mcd8 = tk.Label(frame7, text="Veg Zinger Burger", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd8.place(x=50, y=520)
        price_lbl8 = Label(frame7, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl8.place(x=315, y=520)
        mcd_label8 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label8.place(x=440, y=520)
        sb8 = Spinbox(frame7, from_=0, to=100, width=3)
        sb8.place(x=470, y=520)
        mcd9 = tk.Label(frame7, text="Classic Zinger Burger\n(With Cheese)", bg="#310054", fg="#00f3b2",
                        font=['Calibri', 15, 'bold'])
        mcd9.place(x=50, y=560)
        price_lbl9 = Label(frame7, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl9.place(x=315, y=560)
        mcd_label9 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label9.place(x=440, y=560)
        sb9 = Spinbox(frame7, from_=0, to=100, width=3)
        sb9.place(x=470, y=560)
        mcd10 = tk.Label(frame7, text="Tandoori Zinger Burger\n(with Cheese)", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd10.place(x=50, y=630)
        price_lbl10 = Label(frame7, text="Rs.200", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl10.place(x=315, y=630)
        mcd_label10 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label10.place(x=440, y=630)
        sb10 = Spinbox(frame7, from_=0, to=100, width=3)
        sb10.place(x=470, y=630)
        mcd11 = tk.Label(frame7, text="2 Double Down Burgers", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd11.place(x=50, y=690)
        price_lbl11 = Label(frame7, text="Rs.500", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl11.place(x=315, y=690)
        mcd_label11 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label11.place(x=440, y=690)
        sb11 = Spinbox(frame7, from_=0, to=100, width=3)
        sb11.place(x=470, y=690)
        lbl4 = tk.Label(frame7, text="SNACKS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl4.place(x=620, y=80)
        mcd12 = tk.Label(frame7, text="2 pc Veg Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd12.place(x=650, y=120)
        price_lbl12 = Label(frame7, text="Rs.140", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl12.place(x=850, y=120)
        mcd_label12 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label12.place(x=960, y=120)
        sb12 = Spinbox(frame7, from_=0, to=100, width=3)
        sb12.place(x=990, y=120)
        mcd13 = tk.Label(frame7, text="Medium Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd13.place(x=650, y=160)
        price_lbl13 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl13.place(x=850, y=160)
        mcd_label13 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label13.place(x=960, y=160)
        sb13 = Spinbox(frame7, from_=0, to=100, width=3)
        sb13.place(x=990, y=160)
        mcd14 = tk.Label(frame7, text="Large Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd14.place(x=650, y=200)
        price_lbl14 = Label(frame7, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl14.place(x=850, y=200)
        mcd_label14 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label14.place(x=960, y=200)
        sb14 = Spinbox(frame7, from_=0, to=100, width=3)
        sb14.place(x=990, y=200)
        mcd15 = tk.Label(frame7, text="Smokey Red Chicken\n(2 pc)", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd15.place(x=650, y=240)
        price_lbl15 = Label(frame7, text="Rs.220", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl15.place(x=850, y=240)
        mcd_label15 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label15.place(x=960, y=240)
        sb15 = Spinbox(frame7, from_=0, to=100, width=3)
        sb15.place(x=990, y=240)
        mcd16 = tk.Label(frame7, text="Mingles Bucket", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd16.place(x=650, y=290)
        price_lbl16 = Label(frame7, text="Rs.310", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl16.place(x=850, y=290)
        mcd_label16 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label16.place(x=960, y=290)
        sb16 = Spinbox(frame7, from_=0, to=100, width=3)
        sb16.place(x=990, y=290)
        mcd17 = tk.Label(frame7, text="Medium Popcorn", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd17.place(x=650, y=330)
        price_lbl17 = Label(frame7, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl17.place(x=850, y=330)
        mcd_label17 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label17.place(x=960, y=330)
        sb17 = Spinbox(frame7, from_=0, to=100, width=3)
        sb17.place(x=990, y=330)

    elif rest_value == 3:
        lbl1 = tk.Label(frame7, text="SIGNATURE WRAPS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl1.place(x=20, y=80)
        lbl5 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl5.place(x=280, y=80)
        lbl6 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl6.place(x=800, y=80)
        mcd1 = tk.Label(frame7, text="Aloo Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd1.place(x=50, y=120)
        price_lbl1 = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl1.place(x=315, y=120)
        mcd_label = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label.place(x=440, y=120)
        sb1 = Spinbox(frame7, from_=0, to=100, width=3)
        sb1.place(x=470, y=120)
        mcd2 = tk.Label(frame7, text="Chicken Teriyaki", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd2.place(x=50, y=160)
        price_lbl2 = Label(frame7, text="Rs.260", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl2.place(x=315, y=160)
        mcd_label2 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label2.place(x=440, y=160)
        sb2 = Spinbox(frame7, from_=0, to=100, width=3)
        sb2.place(x=470, y=160)
        mcd3 = tk.Label(frame7, text="Corn and Peas", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd3.place(x=50, y=200)
        price_lbl3 = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl3.place(x=315, y=200)
        mcd_label3 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label3.place(x=440, y=200)
        sb3 = Spinbox(frame7, from_=0, to=100, width=3)
        sb3.place(x=470, y=200)
        mcd4 = tk.Label(frame7, text="Peri Peri Chicken", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd4.place(x=50, y=240)
        price_lbl4 = Label(frame7, text="Rs.250", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl4.place(x=315, y=240)
        mcd_label4 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label4.place(x=440, y=240)
        sb4 = Spinbox(frame7, from_=0, to=100, width=3)
        sb4.place(x=470, y=240)
        mcd5 = tk.Label(frame7, text="Mexican Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd5.place(x=50, y=280)
        price_lbl5 = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl5.place(x=315, y=280)
        mcd_label5 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label5.place(x=440, y=280)
        sb5 = Spinbox(frame7, from_=0, to=100, width=3)
        sb5.place(x=470, y=280)
        mcd6 = tk.Label(frame7, text="Paneer Tikka", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd6.place(x=50, y=320)
        price_lbl6 = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl6.place(x=315, y=320)
        mcd_label6 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label6.place(x=440, y=320)
        sb6 = Spinbox(frame7, from_=0, to=100, width=3)
        sb6.place(x=470, y=320)
        lbl2 = tk.Label(frame7, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl2.place(x=20, y=380)
        mcd7 = tk.Label(frame7, text="Mountain Dew", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd7.place(x=50, y=420)
        price_lbl7 = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl7.place(x=315, y=420)
        mcd_label7 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label7.place(x=440, y=420)
        sb7 = Spinbox(frame7, from_=0, to=100, width=3)
        sb7.place(x=470, y=420)
        mcd8 = tk.Label(frame7, text="Orange Juice", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd8.place(x=50, y=460)
        price_lbl8 = Label(frame7, text="Rs.70", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl8.place(x=315, y=460)
        mcd_label8 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label8.place(x=440, y=460)
        sb8 = Spinbox(frame7, from_=0, to=100, width=3)
        sb8.place(x=470, y=460)
        mcd9 = tk.Label(frame7, text="Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd9.place(x=50, y=500)
        price_lbl9 = Label(frame7, text="Rs.50", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl9.place(x=315, y=500)
        mcd_label9 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label9.place(x=440, y=500)
        sb9 = Spinbox(frame7, from_=0, to=100, width=3)
        sb9.place(x=470, y=500)
        lbl3 = tk.Label(frame7, text="DESSERTS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl3.place(x=20, y=560)
        mcd10 = tk.Label(frame7, text="Rich Chocolate Truffle", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd10.place(x=50, y=600)
        price_lbl10 = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl10.place(x=315, y=600)
        mcd_label10 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label10.place(x=440, y=600)
        sb10 = Spinbox(frame7, from_=0, to=100, width=3)
        sb10.place(x=470, y=600)
        mcd11 = tk.Label(frame7, text="Single Chocolate Cookie", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd11.place(x=50, y=640)
        price_lbl11 = Label(frame7, text="Rs.30", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl11.place(x=315, y=640)
        mcd_label11 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label11.place(x=440, y=640)
        sb11 = Spinbox(frame7, from_=0, to=100, width=3)
        sb11.place(x=470, y=640)
        mcd12 = tk.Label(frame7, text="Double Chocolate Cookie", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd12.place(x=50, y=680)
        price_lbl12 = Label(frame7, text="Rs.40", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl12.place(x=315, y=680)
        mcd_label12 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label12.place(x=440, y=680)
        sb12 = Spinbox(frame7, from_=0, to=100, width=3)
        sb12.place(x=470, y=680)
        lbl4 = tk.Label(frame7, text="SIDES & EXTRAS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl4.place(x=620, y=80)
        mcd13 = tk.Label(frame7, text="Lays Chips (Classic)", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd13.place(x=650, y=120)
        price_lbl13 = Label(frame7, text="Rs.25", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl13.place(x=850, y=120)
        mcd_label13 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label13.place(x=960, y=120)
        sb13 = Spinbox(frame7, from_=0, to=100, width=3)
        sb13.place(x=990, y=120)

        mcd14 = tk.Label(frame7, text="Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd14.place(x=650, y=160)
        price_lbl14 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl14.place(x=850, y=160)
        mcd_label14 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label14.place(x=960, y=160)
        sb14 = Spinbox(frame7, from_=0, to=100, width=3)
        sb14.place(x=990, y=160)

        mcd15 = tk.Label(frame7, text="Hash Browns", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd15.place(x=650, y=200)
        price_lbl15 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl15.place(x=850, y=200)
        mcd_label15 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label15.place(x=960, y=200)
        sb15 = Spinbox(frame7, from_=0, to=100, width=3)
        sb15.place(x=990, y=200)

        mcd16 = tk.Label(frame7, text="Chorizo Flatbread Pizza", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd16.place(x=600, y=240)
        price_lbl16 = Label(frame7, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl16.place(x=850, y=240)
        mcd_label16 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label16.place(x=960, y=240)
        sb16 = Spinbox(frame7, from_=0, to=100, width=3)
        sb16.place(x=990, y=240)

    elif rest_value == 4:
        lbl1 = tk.Label(frame7, text="DOUGHNUTS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl1.place(x=20, y=80)
        lbl5 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl5.place(x=280, y=80)
        lbl6 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl6.place(x=800, y=80)
        mcd1 = tk.Label(frame7, text="Rainbow Pop", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd1.place(x=50, y=120)
        price_lbl1 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl1.place(x=315, y=120)
        mcd_label = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label.place(x=440, y=120)
        sb1 = Spinbox(frame7, from_=0, to=100, width=3)
        sb1.place(x=470, y=120)
        mcd2 = tk.Label(frame7, text="Choco Pop", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd2.place(x=50, y=160)
        price_lbl2 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl2.place(x=315, y=160)
        mcd_label2 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label2.place(x=440, y=160)
        sb2 = Spinbox(frame7, from_=0, to=100, width=3)
        sb2.place(x=470, y=160)
        mcd3 = tk.Label(frame7, text="Boston Crème", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd3.place(x=50, y=200)
        price_lbl3 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl3.place(x=315, y=200)
        mcd_label3 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label3.place(x=440, y=200)
        sb3 = Spinbox(frame7, from_=0, to=100, width=3)
        sb3.place(x=470, y=200)
        mcd4 = tk.Label(frame7, text="Choco Overdose", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd4.place(x=50, y=240)
        price_lbl4 = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl4.place(x=315, y=240)
        mcd_label4 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label4.place(x=440, y=240)
        sb4 = Spinbox(frame7, from_=0, to=100, width=3)
        sb4.place(x=470, y=240)
        mcd5 = tk.Label(frame7, text="Peanut Butter Island", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd5.place(x=50, y=280)
        price_lbl5 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl5.place(x=315, y=280)
        mcd_label5 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label5.place(x=440, y=280)
        sb5 = Spinbox(frame7, from_=0, to=100, width=3)
        sb5.place(x=470, y=280)
        mcd6 = tk.Label(frame7, text="White Choco & Strawberry\nEclair", bg="#310054", fg="#00f3b2",
                        font=['Calibri', 15, 'bold'])
        mcd6.place(x=50, y=320)
        price_lbl6 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl6.place(x=315, y=320)
        mcd_label6 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label6.place(x=440, y=320)
        sb6 = Spinbox(frame7, from_=0, to=100, width=3)
        sb6.place(x=470, y=320)
        mcd7 = tk.Label(frame7, text="Chocotella", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd7.place(x=50, y=370)
        price_lbl7 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl7.place(x=315, y=370)
        mcd_label7 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label7.place(x=440, y=370)
        sb7 = Spinbox(frame7, from_=0, to=100, width=3)
        sb7.place(x=470, y=370)
        mcd8 = tk.Label(frame7, text="Choco Berry Bomb", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd8.place(x=50, y=410)
        price_lbl8 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl8.place(x=315, y=410)
        mcd_label8 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label8.place(x=440, y=410)
        sb8 = Spinbox(frame7, from_=0, to=100, width=3)
        sb8.place(x=470, y=410)

        lbl2 = tk.Label(frame7, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl2.place(x=20, y=460)

        mcd9 = tk.Label(frame7, text="Caremal Dunkaccino", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd9.place(x=50, y=500)
        price_lbl9 = Label(frame7, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl9.place(x=315, y=500)
        mcd_label9 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label9.place(x=440, y=500)
        sb9 = Spinbox(frame7, from_=0, to=100, width=3)
        sb9.place(x=470, y=500)
        mcd10 = tk.Label(frame7, text="Virgin Mojito", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd10.place(x=50, y=540)
        price_lbl10 = Label(frame7, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl10.place(x=315, y=540)
        mcd_label10 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label10.place(x=440, y=540)
        sb10 = Spinbox(frame7, from_=0, to=100, width=3)
        sb10.place(x=470, y=540)
        mcd11 = tk.Label(frame7, text="Fruit Berry", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd11.place(x=50, y=580)
        price_lbl11 = Label(frame7, text="Rs.210", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl11.place(x=315, y=580)
        mcd_label11 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label11.place(x=440, y=580)
        sb11 = Spinbox(frame7, from_=0, to=100, width=3)
        sb11.place(x=470, y=580)
        mcd12 = tk.Label(frame7, text="Caremal Iced Coffee", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd12.place(x=50, y=620)
        price_lbl12 = Label(frame7, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl12.place(x=315, y=620)
        mcd_label12 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label12.place(x=440, y=620)
        sb12 = Spinbox(frame7, from_=0, to=100, width=3)
        sb12.place(x=470, y=620)

        mcd13 = tk.Label(frame7, text="Peach Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd13.place(x=50, y=660)
        price_lbl13 = Label(frame7, text="Rs.170", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl13.place(x=315, y=660)
        mcd_label13 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label13.place(x=440, y=660)
        sb13 = Spinbox(frame7, from_=0, to=100, width=3)
        sb13.place(x=470, y=660)

        mcd14 = tk.Label(frame7, text="Choco Hazelnut Dunkaccino", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
        mcd14.place(x=50, y=700)
        price_lbl14 = Label(frame7, text="Rs.180", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl14.place(x=315, y=700)
        mcd_label14 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label14.place(x=440, y=700)
        sb14 = Spinbox(frame7, from_=0, to=100, width=3)
        sb14.place(x=470, y=700)

        mcd15 = tk.Label(frame7, text="Fresh Ginger Chai", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd15.place(x=50, y=740)
        price_lbl15 = Label(frame7, text="Rs.200", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl15.place(x=315, y=740)
        mcd_label15 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label15.place(x=440, y=740)
        sb15 = Spinbox(frame7, from_=0, to=100, width=3)
        sb15.place(x=470, y=740)

        lbl4 = tk.Label(frame7, text="SIDES & EXTRAS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
        lbl4.place(x=620, y=80)

        mcd16 = tk.Label(frame7, text="Potato Wedges", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd16.place(x=630, y=130)
        price_lbl16 = Label(frame7, text="Rs.80", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl16.place(x=850, y=130)
        mcd_label16 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label16.place(x=960, y=130)
        sb16 = Spinbox(frame7, from_=0, to=100, width=3)
        sb16.place(x=990, y=130)

        mcd17 = tk.Label(frame7, text="Veg Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd17.place(x=630, y=170)
        price_lbl17 = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl17.place(x=850, y=170)
        mcd_label17 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label17.place(x=960, y=170)
        sb17 = Spinbox(frame7, from_=0, to=100, width=3)
        sb17.place(x=990, y=170)

        mcd18 = tk.Label(frame7, text="Chicken Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        mcd18.place(x=630, y=210)
        price_lbl18 = Label(frame7, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
        price_lbl18.place(x=850, y=210)
        mcd_label18 = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
        mcd_label18.place(x=960, y=210)
        sb18 = Spinbox(frame7, from_=0, to=100, width=3)
        sb18.place(x=990, y=210)

    else:
        messagebox.showerror("Choose Restaurant", "Please Choose a Restaurant from above")


billing_button = Button(frame7, text="Continue to Billing", font=["Times New Roman", 18, "bold"])
billing_button.place(x=1000, y=700)

# ==================Frame 5 code(BILL)

bg_label_f5 = Label(frame7, bg="#310054")
bg_label_f5.pack(fill='both', expand=True)

bill_label = tk.Label(frame7, text="BILL")
bill_label["fg"] = "#00f3b2"
bill_label["bg"] = "#310054"
bill_label["font"] = ("Calibri", 30, "underline")
bill_label.place(x=100, y=40)

# ==================Frame 6 code(RESERVATION CONFIRMATION)

bg_label_f6 = Label(frame7, bg="#310054")
bg_label_f6.pack(fill='both', expand=True)

confirm_label = tk.Label(frame7, text="RESERVATION CONFIRMATION")
confirm_label["fg"] = "#00f3b2"
confirm_label["bg"] = "#310054"
confirm_label["font"] = ("Calibri", 30, "underline")
confirm_label.place(x=100, y=40)

show_frame(frame1)

root.mainloop()
