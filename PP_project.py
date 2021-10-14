import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import smtplib


def show_frame(frame):
    frame.tkraise()


root = tk.Tk()

root.state('zoomed')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root)  # logo
frame2 = tk.Frame(root)  # register form
frame3 = tk.Frame(root)  # Choose resto
frame4 = tk.Frame(root)  # mcd menu
frame5 = tk.Frame(root)  # kfc menu
frame6 = tk.Frame(root)  # dunkin menu
frame7 = tk.Frame(root)  # subway
frame8 = tk.Frame(root)  # bill
frame9 = tk.Frame(root)  # reservation

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9):
    frame.grid(row=0, column=0, sticky='nsew')

# ==================Frame 1 code
# window title
root.title("FOOD HUNTER")
root.geometry("800x900")
root["highlightbackground"] = "#00f3b2"

# baground
bg_label_f1 = Label(frame1, bg="#310054")
bg_label_f1.pack(fill='both', expand=True)

# image
logo_pic = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/food_hunter_RE.png"))
logo_label = tk.Label(frame1, image=logo_pic)
logo_label["highlightbackground"] = "#310054"
logo_label.place(x=490, y=120)

# order button
button_order = tk.Button(frame1, text="Order", command=lambda: show_frame(frame2))
button_order.place(x=550, y=435)
button_order["width"] = 20
button_order["fg"] = "#00f3b2"
button_order["highlightbackground"] = "#310054"

# ==================Frame 2 code
# window title
root.geometry("600x500")

# baground
bg_label_f2 = tk.Label(frame2, bg="#310054")
bg_label_f2.pack(fill='both', expand=True)

# Registration Form Label
registration_form_label = tk.Label(frame2, text="REGISTRATION FORM")
registration_form_label.place(x=450, y=60)
# dictionary attributes for label
registration_form_label["font"] = ("Al Bayan", 30, "underline","bold")
registration_form_label["fg"] = "#ffa500"
registration_form_label["bg"] = "#310054"

fullname = ""
timeslot = ""
num_of_ppl = ""
email_id = ""


def reg_form_submit():
    error = False
    global fullname
    fullname = fullname_entrytext.get()
    if fullname == "":
        messagebox.showerror("Empty Name Box", "Enter Your Name")
        error = True
        show_frame(frame2)
    var_name.set(f"Name :     {fullname}")
    global timeslot
    timeslot = temp1.get()
    if timeslot == "Select your time slot":
        error = True
        messagebox.showerror("Time Slot Not Chosen", "Select a Time Slot")
    var_time.set(f"Timeslot :     {timeslot}")
    global num_of_ppl
    num_of_ppl = num_spin.get()
    var_num_ppl.set(f"Number of people :     {num_of_ppl}")
    global city
    city = temp.get()
    if city == "Select your city":
        messagebox.showerror("City Not Chosen", "Select a Time Slot")
        error = True
    global email_id
    email_id = email_entrytext.get()
    if email_id == "":
        messagebox.showerror("Empty Email ID Box", "Enter Your Email ID")
        error = True
        show_frame(frame2)
    if error == False:
        show_frame(frame3)
    else:
        show_frame(frame2)


# Fullname Label
fullname_label = tk.Label(frame2, text="FULL NAME :")
fullname_label.place(x=430, y=130)
fullname_label["font"] = ("Calibri",15,"bold")
fullname_label["fg"] = "#00f3b2"
fullname_label["bg"] = "#310054"
# textbox - Entry text
fullname_entrytext = tk.Entry(frame2,borderwidth=3,width = 27)
fullname_entrytext["fg"] = "#00f3b2"
fullname_entrytext["bg"] = "#310054"
fullname_entrytext.place(x=570, y=130)

# time(breakfast,lunch,dinner)
time_slot = tk.Label(frame2, text="TIME SLOT :")
time_slot["font"] = ("Calibri",15,"bold")
time_slot["fg"] = "#00f3b2"
time_slot["bg"] = "#310054"
time_slot.place(x=430, y=210)
# creating optionmenu for time slots
list_of_slots = ["Breakfast : 8:00 a.m. - 11:00 a.m.", "Lunch : 1:00 p.m. - 3:00 p.m.",
                 "Dinner : 8:00 p.m. - 11:00 p.m."]
temp1 = StringVar()
slot_optionmenu = tk.OptionMenu(frame2, temp1, *list_of_slots)
slot_optionmenu.place(x=570, y=210)
slot_optionmenu.config(width=25)
slot_optionmenu["fg"] = "#00f3b2"
slot_optionmenu["bg"] = "#310054"
temp1.set("Select your time slot")

# location label
user_location = tk.Label(frame2, text="LOCATION :")
user_location["font"] = ("Calibri",15,"bold")
user_location["fg"] = "#00f3b2"
user_location["bg"] = "#310054"
user_location.place(x=430, y=280)
# creatting optionmenu for locations
list_of_states = ["Mumbai", "Delhi", "Bangalore", "Kolkata"]
temp = StringVar()
state_optionmenu = tk.OptionMenu(frame2, temp, *list_of_states)
state_optionmenu.config(width=25)
state_optionmenu["fg"] = "#00f3b2"
state_optionmenu["bg"] = "#310054"
state_optionmenu.place(x=570, y=280)
temp.set("Select your city")

# number of people
num_ppl = tk.Label(frame2, text="NUMBER OF PEOPLE :")
num_ppl["font"] = ("Calibri",15,"bold")
num_ppl["fg"] = "#00f3b2"
num_ppl["bg"] = "#310054"
num_ppl.place(x=365, y=340)
num_spin = tk.Spinbox(frame2, from_=1, to=15, width=8)
num_spin.config(width=10)
num_spin["fg"] = "#00f3b2"
num_spin["bg"] = "#310054"
num_spin.place(x=600, y=340)

# Email ID Label
email_label = tk.Label(frame2, text="EMAIL ID :")
email_label["font"] = ("Calibri",15,"bold")
email_label.place(x=430, y=400)
email_label["fg"] = "#00f3b2"
email_label["bg"] = "#310054"
# textbox - Entry text
email_entrytext = tk.Entry(frame2, borderwidth=3,width = 27)
email_entrytext["fg"] = "#00f3b2"
email_entrytext["bg"] = "#310054"
email_entrytext.place(x=570, y=400)

# Submit Button
button_submit = tk.Button(frame2, text="Submit", command=reg_form_submit)
button_submit.place(x=630, y=480)
button_submit["width"] = 20
button_submit["fg"] = "#00f3b2"
button_submit["highlightbackground"] = "#310054"

# Back Button
button_back = tk.Button(frame2, text="Back", command=lambda: show_frame(frame1))
button_back.place(x=430, y=480)
button_back["width"] = 20
button_back["fg"] = "#00f3b2"
button_back["highlightbackground"] = "#310054"

# ==================Frame 3 code

root.geometry("800x900")
bg_label_f3 = tk.Label(frame3, bg="#310054")
bg_label_f3.pack(fill='both', expand=True)

# restaurants title label
resto_label = tk.Label(frame3, text="CHOOSE THE RESTAURANT")
resto_label["fg"] = "#ffa500"
resto_label["bg"] = "#310054"
resto_label["font"] = ("Al Bayan", 30, "underline","bold")
resto_label.place(x= 450, y=40)

# image mcd logo
mcd_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/mcd_logo (1).png"))
mcd_logo_label = tk.Label(frame3, image=mcd_logo)
mcd_logo_label["highlightbackground"] = "#310054"
mcd_logo_label.place(x=130, y=150)

# mcd
mcd_label = tk.Label(frame3, text="McDonalds : ")
mcd_label["fg"] = "#00f3b2"
mcd_label["bg"] = "#310054"
mcd_label["font"] = ("Calibri", 14)
mcd_label.place(x=260, y=150)

# finish reservation button mcd
finish_button_mcd = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_mcd["fg"] = "#00f3b2"
finish_button_mcd["highlightbackground"] = "#310054"
finish_button_mcd["font"] = ("Calibri", 15)
finish_button_mcd.place(x=260, y=200)

# continue to order button mcd
continue_to_order_mcd = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame4))
continue_to_order_mcd["fg"] = "#00f3b2"
continue_to_order_mcd["highlightbackground"] = "#310054"
continue_to_order_mcd["font"] = ("Calibri", 15)
continue_to_order_mcd.place(x=410, y=200)

# image kfc
kfc_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/kfc logo img (1).png"))
kfc_logo_label = tk.Label(frame3, image=kfc_logo)
kfc_logo_label["highlightbackground"] = "#310054"
kfc_logo_label.place(x=110, y=380)

# kfc
kfc_label = tk.Label(frame3, text="KFC : ")
kfc_label["fg"] = "#00f3b2"
kfc_label["bg"] = "#310054"
kfc_label["font"] = ("Calibri", 14)
kfc_label.place(x=250, y=380)

# finish reservation button kfc
finish_button_kfc = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_kfc["fg"] = "#00f3b2"
finish_button_kfc["highlightbackground"] = "#310054"
finish_button_kfc["font"] = ("Calibri", 15)
finish_button_kfc.place(x=250, y=430)

# continue to order button kfc
continue_to_order_kfc = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame5))
continue_to_order_kfc["fg"] = "#00f3b2"
continue_to_order_kfc["highlightbackground"] = "#310054"
continue_to_order_kfc["font"] = ("Calibri", 15)
continue_to_order_kfc.place(x=400, y=430)

# image dunkin
dunkin_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/dunkin_logo (2).png"))
dunkin_logo_label = tk.Label(frame3, image=dunkin_logo)
dunkin_logo_label["highlightbackground"] = "#310054"
dunkin_logo_label.place(x=610, y=150)

# dunkin
dunkin_label = tk.Label(frame3, text="Dunkin' Donuts : ")
dunkin_label["fg"] = "#00f3b2"
dunkin_label["bg"] = "#310054"
dunkin_label["font"] = ("Calibri", 14)
dunkin_label.place(x=790, y=150)

# finish reservation button dunkin
finish_button_dunkin = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_dunkin["fg"] = "#00f3b2"
finish_button_dunkin["highlightbackground"] = "#310054"
finish_button_dunkin["font"] = ("Calibri", 15)
finish_button_dunkin.place(x=790, y=200)

# continue to order button dunkin
continue_to_order_dunkin = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame6))
continue_to_order_dunkin["fg"] = "#00f3b2"
continue_to_order_dunkin["highlightbackground"] = "#310054"
continue_to_order_dunkin["font"] = ("Calibri", 15)
continue_to_order_dunkin.place(x=940, y=200)

# image subway
subway_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/subway_logo (1).png"))
subway_logo_label = tk.Label(frame3, image=subway_logo)
subway_logo_label["highlightbackground"] = "#310054"
subway_logo_label.place(x=610, y=380)

# subway
subway_label = tk.Label(frame3, text="Subway : ")
subway_label["fg"] = "#00f3b2"
subway_label["bg"] = "#310054"
subway_label["font"] = ("Calibri", 14)
subway_label.place(x = 790, y=380)

# finish reservation button subway
finish_button_subway = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_subway["fg"] = "#00f3b2"
finish_button_subway["highlightbackground"] = "#310054"
finish_button_subway["font"] = ("Calibri", 15)
finish_button_subway.place(x=790, y=430)

# continue to order button subway
continue_to_order_subway = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame7))
continue_to_order_subway["fg"] = "#00f3b2"
continue_to_order_subway["highlightbackground"] = "#310054"
continue_to_order_subway["font"] = ("Calibri", 15)
continue_to_order_subway.place(x=940, y=430)

button_back_f2 = tk.Button(frame3, text="Back", command=lambda: show_frame(frame2))
button_back_f2.place(x=100, y=550)
button_back_f2["width"] = 20
button_back_f2["fg"] = "#00f3b2"
button_back_f2["highlightbackground"] = "#310054"

# ==================Frame 4 code(MENU OF RESTO - MCD)
root.geometry("600x500")
bg_label_f4 = tk.Label(frame4, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

global chosen_item_name
chosen_item_name = []
global chosen_item_qty
chosen_item_qty = []
global chosen_item_price
chosen_item_price = []

city = ""


def mcd_get_order():
    show_frame(frame8)
    global city
    city = temp.get()
    var_restaurant.set(f"Restaurant :     McDonald's, {city}")
    mcd_all_items = []  # Adding all items in the list as a tuple in the form (item name, quantity, price)
    mcd_all_items.append(("McSpicy Chicken", int(var_mcspicy_chicken.get()), 170))
    mcd_all_items.append(("McSpicy Paneer", int(var_mcspicy_paneer.get()), 160))
    mcd_all_items.append(("McVeggie", int(var_mcveggie.get()), 110))
    mcd_all_items.append(("Mexican McAloo Tikki", int(var_mex_mcaloo.get()), 60))
    mcd_all_items.append(("McAloo Tikki", int(var_mcaloo.get()), 50))
    mcd_all_items.append(("Chicken Kebab Burger", int(var_chicken_kebab.get()), 180))
    mcd_all_items.append(("Thums Up", int(var_thums_up.get()), 85))
    mcd_all_items.append(("Coke", int(var_coke.get()), 90))
    mcd_all_items.append(("Iced Tea", int(var_iced_tea.get()), 100))
    mcd_all_items.append(("Regular Fries", int(var_reg_fries.get()), 60))
    mcd_all_items.append(("Medium Fries", int(var_med_fries.get()), 100))
    mcd_all_items.append(("Large Fries", int(var_large_fries.get()), 120))
    mcd_all_items.append(("Masala Wedges", int(var_masala_wedges.get()), 100))
    mcd_all_items.append(("Chicken Strips", int(var_chicken_strips.get()), 120))
    mcd_all_items.append(("McFlurry", int(var_mcflurry.get()), 110))
    mcd_all_items.append(("Soft Serve", int(var_soft_serve.get()), 90))

    # Adding the items the user has selected in this list
    chosen_item_amt = []
    for (name, qty, price) in mcd_all_items:
        if qty > 0:
            chosen_item_name.append(name)
            chosen_item_qty.append(qty)
            chosen_item_price.append(price)
            chosen_item_amt.append(qty * price)
    print(f"{chosen_item_name}\n{chosen_item_qty}\n{chosen_item_price}\n{chosen_item_amt}")

    # Storing all the item names in a string
    name_str = ""
    for x in chosen_item_name:
        name_str += f"{x}\n"
    var_item_name.set(name_str)

    # Storing all the item quantities in a string
    qty_str = ""
    for x in chosen_item_qty:
        qty_str += f"{x}\n"
    var_item_quantity.set(qty_str)

    # Storing all the item amounts in a string
    amt_str = ""
    for x in chosen_item_amt:
        amt_str += f"{x}\n"
    var_item_amt.set(amt_str)
    # Finding and storing the total amount without GST
    amt_wo_gst = 0
    for x in chosen_item_amt:
        amt_wo_gst += x
    var_total_amt_wo_gst.set(f"Sub Total :\t\t{amt_wo_gst}")
    print(amt_wo_gst)

    # Calculating GST
    gst = ((6 / 100) * amt_wo_gst)
    var_gst_amt.set(f"GST :\t\t{gst:.2f}\t(6%)")

    # Finding Total Amount
    amt_w_gst = amt_wo_gst + gst
    var_total_amt_w_gst.set(f"Final Amount :\t{amt_w_gst:.2f}")

    txtfile = open("reservation details.txt", "w")
    txtfile.write(
        f"Hey {fullname}\nBooking has been confirmed, here are the details :\nName : {fullname}\nRestaurant : McDonald's, {city}\nTimeslot : {timeslot}\nNumber of People : {num_of_ppl}\nTotal Amount : {amt_w_gst} Rs.\n\n")
    txtfile.close()


mcd_label = tk.Label(frame4, text="MENU - MCDONALDS")
mcd_label["fg"] = "#ffa500"
mcd_label["bg"] = "#310054"
mcd_label["font"] = ("Al Bayan", 30, "underline","bold")
mcd_label.place(x=500, y=10)

mcd_burgers = tk.Label(frame4, text="BURGERS:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
mcd_burgers.place(x=20, y=80)

mcd_price_1 = tk.Label(frame4, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
mcd_price_1.place(x=280, y=80)

mcd_price_2 = tk.Label(frame4, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
mcd_price_2.place(x=800, y=80)

mcspicy_chicken = tk.Label(frame4, text="McSpicy Chicken", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcspicy_chicken.place(x=50, y=120)

price_mcspicy_chicken = Label(frame4, text="Rs.170", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcspicy_chicken.place(x=315, y=120)

qty_mcspicy_chicken = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcspicy_chicken.place(x=440, y=120)

var_mcspicy_chicken = IntVar(value=0)
sb_mcspicy_chicken = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcspicy_chicken)
sb_mcspicy_chicken.place(x=470, y=120)

mcspicy_paneer = tk.Label(frame4, text="McSpicy Paneer", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcspicy_paneer.place(x=50, y=160)

price_mcspicy_paneer = Label(frame4, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcspicy_paneer.place(x=315, y=160)

qty_mcspicy_paneer = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcspicy_paneer.place(x=440, y=160)

var_mcspicy_paneer = IntVar(value=0)
sb_mcspicy_paneer = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcspicy_paneer)
sb_mcspicy_paneer.place(x=470, y=160)

mcveggie = tk.Label(frame4, text="McVeggie", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcveggie.place(x=50, y=200)

price_mcveggie = Label(frame4, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcveggie.place(x=315, y=200)

qty_mcveggie = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcveggie.place(x=440, y=200)

var_mcveggie = IntVar(value=0)
sb_mcveggie = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcveggie)
sb_mcveggie.place(x=470, y=200)

mex_mcaloo = tk.Label(frame4, text="Mexican McAloo Tikki", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mex_mcaloo.place(x=50, y=240)

price_mex_mcaloo = Label(frame4, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mex_mcaloo.place(x=315, y=240)

qty_mex_mcaloo = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mex_mcaloo.place(x=440, y=240)

var_mex_mcaloo = IntVar(value=0)
sb_mex_mcaloo = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mex_mcaloo)
sb_mex_mcaloo.place(x=470, y=240)

mcaloo = tk.Label(frame4, text="McAloo Tikki", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcaloo.place(x=50, y=280)

price_mcaloo = Label(frame4, text="Rs.50", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcaloo.place(x=315, y=280)

qty_mcaloo = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcaloo.place(x=440, y=280)

var_mcaloo = IntVar(value=0)
sb_mcaloo = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcaloo)
sb_mcaloo.place(x=470, y=280)

chicken_kebab = tk.Label(frame4, text="Chicken Kebab Burger", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
chicken_kebab.place(x=50, y=320)

price_chicken_kebab = Label(frame4, text="Rs.180", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_chicken_kebab.place(x=315, y=320)

qty_chicken_kebab = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_chicken_kebab.place(x=440, y=320)

var_chicken_kebab = IntVar(value=0)
sb_chicken_kebab = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_chicken_kebab)
sb_chicken_kebab.place(x=470, y=320)

mcd_beverages = tk.Label(frame4, text="BEVERAGES:", bg="#310054", fg="#ffa500", font=['Calibri', 17,"bold"])
mcd_beverages.place(x=20, y=380)

thums_up = tk.Label(frame4, text="Thumbs Up", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
thums_up.place(x=50, y=420)

price_thums_up = Label(frame4, text="Rs.85", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_thums_up.place(x=315, y=420)

qty_thums_up = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_thums_up.place(x=440, y=420)

var_thums_up = IntVar(value=0)
sb_thums_up = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_thums_up)
sb_thums_up.place(x=470, y=420)

coke = tk.Label(frame4, text="Coke", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
coke.place(x=50, y=460)

price_coke = Label(frame4, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_coke.place(x=315, y=460)

qty_coke = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_coke.place(x=440, y=460)

var_coke = IntVar(value=0)
sb_coke = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_coke)
sb_coke.place(x=470, y=460)

iced_tea = tk.Label(frame4, text="Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
iced_tea.place(x=50, y=500)

price_iced_tea = Label(frame4, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_iced_tea.place(x=315, y=500)

qty_iced_tea = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_iced_tea.place(x=440, y=500)

var_iced_tea = IntVar(value=0)
sb_iced_tea = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_iced_tea)
sb_iced_tea.place(x=470, y=500)

mcd_fries_and_sides = tk.Label(frame4, text="FRIES & SIDES:", bg="#310054", fg="#ffa500", font=['Calibri', 17,"bold"])
mcd_fries_and_sides.place(x=620, y=80)

reg_fries = tk.Label(frame4, text="Regular Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
reg_fries.place(x=650, y=120)

price_reg_fries = Label(frame4, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_reg_fries.place(x=850, y=120)

qty_reg_fries = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_reg_fries.place(x=960, y=120)

var_reg_fries = IntVar(value=0)
sb_reg_fries = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_reg_fries)
sb_reg_fries.place(x=990, y=120)

med_fries = tk.Label(frame4, text="Medium Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
med_fries.place(x=650, y=160)

price_med_fries = Label(frame4, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_med_fries.place(x=850, y=160)

qty_med_fries = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_med_fries.place(x=960, y=160)

var_med_fries = IntVar(value=0)
sb_med_fries = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_med_fries)
sb_med_fries.place(x=990, y=160)

large_fries = tk.Label(frame4, text="Large Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
large_fries.place(x=650, y=200)

price_large_fries = Label(frame4, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_large_fries.place(x=850, y=200)

qty_large_fries = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_large_fries.place(x=960, y=200)

var_large_fries = IntVar(value=0)
sb_large_fries = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_large_fries)
sb_large_fries.place(x=990, y=200)

masala_wedges = tk.Label(frame4, text="Masala Wedeges", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
masala_wedges.place(x=650, y=240)

price_masala_wedges = Label(frame4, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_masala_wedges.place(x=850, y=240)

qty_masala_wedges = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_masala_wedges.place(x=960, y=240)

var_masala_wedges = IntVar(value=0)
sb_masala_wedges = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_masala_wedges)
sb_masala_wedges.place(x=990, y=240)

chicken_strips = tk.Label(frame4, text="Chicken Strips", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
chicken_strips.place(x=650, y=280)

price_chicken_strips = Label(frame4, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_chicken_strips.place(x=850, y=280)

qty_chicken_strips = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_chicken_strips.place(x=960, y=280)

var_chicken_strips = IntVar(value=0)
sb_chicken_strips = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_chicken_strips)
sb_chicken_strips.place(x=990, y=280)

mcwings = tk.Label(frame4, text="McWings", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcwings.place(x=650, y=320)

price_mcwings = Label(frame4, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcwings.place(x=850, y=320)

qty_mcwings = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcwings.place(x=960, y=320)

var_mcwings = IntVar()
sb_mcwings = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcwings)
sb_mcwings.place(x=990, y=320)

mcd_desserts = tk.Label(frame4, text="DESSERTS:", bg="#310054", fg="#ffa500", font=['Calibri', 17,"bold"])
mcd_desserts.place(x=620, y=380)

mcswirl = tk.Label(frame4, text="McSwirl", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcswirl.place(x=650, y=420)

price_mcswirl = Label(frame4, text="Rs.30", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcswirl.place(x=850, y=420)

qty_mcswirl = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcswirl.place(x=960, y=420)

var_mcswirl = IntVar(value=0)
sb_mcswirl = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcswirl)
sb_mcswirl.place(x=990, y=420)

mcflurry = tk.Label(frame4, text="McFlurry", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mcflurry.place(x=650, y=460)

price_mcflurry = Label(frame4, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mcflurry.place(x=850, y=460)

qty_mcflurry = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mcflurry.place(x=960, y=460)

var_mcflurry = IntVar(value=0)
sb_mcflurry = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcflurry)
sb_mcflurry.place(x=990, y=460)

soft_serve = tk.Label(frame4, text="Soft Serve", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
soft_serve.place(x=650, y=500)

price_soft_serve = Label(frame4, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_soft_serve.place(x=850, y=500)

qty_soft_serve = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_soft_serve.place(x=960, y=500)

var_soft_serve = IntVar(value=0)
sb_soft_serve = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_soft_serve)
sb_soft_serve.place(x=990, y=500)

b_mcd_get_bill = tk.Button(frame4, text="Get Bill", command=mcd_get_order)
b_mcd_get_bill.place(x=1050, y=575)
b_mcd_get_bill["width"] = 20
b_mcd_get_bill["fg"] = "#00f3b2"
b_mcd_get_bill["highlightbackground"] = "#310054"

b_mcd_back = tk.Button(frame4, text="Back", command=lambda: show_frame(frame3))
b_mcd_back.place(x=850, y=575)
b_mcd_back["width"] = 20
b_mcd_back["fg"] = "#00f3b2"
b_mcd_back["highlightbackground"] = "#310054"

# ========================================================================================(menu - Kfc)FRAME 5
root.geometry("600x500")
bg_label_f4 = tk.Label(frame5, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

kfc_label = tk.Label(frame5, text="MENU - KFC")
kfc_label["fg"] = "#ffa500"
kfc_label["bg"] = "#310054"
kfc_label["font"] = ("Al Bayan", 30, "underline","bold")
kfc_label.place(x=550, y=10)


def kfc_get_order():
    global city
    city = temp.get()
    show_frame(frame8)
    var_restaurant.set(f"Restaurant :     KFC, {city}")
    kfc_all_items = []  # Adding all items in the list as a tuple in the form (item name, quantity, price)
    kfc_all_items.append(("Big 8", int(var_big_8.get()), 620))
    kfc_all_items.append(("Big 12", int(var_big_12.get()), 730))
    kfc_all_items.append(("Bucket for 2", int(var_bucket_2.get()), 600))
    kfc_all_items.append(("Ultimate Savings Bucket", int(var_saving_bucket.get()), 700))
    kfc_all_items.append(("Red Bull", int(var_red_bull.get()), 160))
    kfc_all_items.append(("Pepsi Can", int(var_pepsi.get()), 60))
    kfc_all_items.append(("Mirinda Can", int(var_mirinda.get()), 60))
    kfc_all_items.append(("Veg Zinger Burger", int(var_veg_zinger.get()), 160))
    kfc_all_items.append(("Classic Zinger Burger", int(var_classic_zinger.get()), 190))
    kfc_all_items.append(("Tandoori Zinger Burger", int(var_tand_zinger.get()), 200))
    kfc_all_items.append(("2 Double Down Burgers", int(var_double_down.get()), 500))
    kfc_all_items.append(("2 pc Veg Patty", int(var_veg_patty.get()), 140))
    kfc_all_items.append(("Medium Fries", int(var_kfc_m_fries.get()), 100))
    kfc_all_items.append(("Large Fries", int(var_kfc_l_fries.get()), 120))
    kfc_all_items.append(("Smokey Red Chicken", int(var_sm_red_chicken.get()), 220))
    kfc_all_items.append(("Mingles Bucket", int(var_mingles.get()), 310))
    kfc_all_items.append(("Medium Popcorn", int(var_med_popcorn.get()), 150))

    # Adding the items the user has selected in this list
    chosen_item_amt = []
    for (name, qty, price) in kfc_all_items:
        if qty > 0:
            chosen_item_name.append(name)
            chosen_item_qty.append(qty)
            chosen_item_price.append(price)
            chosen_item_amt.append(qty * price)
    print(f"{chosen_item_name}\n{chosen_item_qty}\n{chosen_item_price}\n{chosen_item_amt}")

    # Storing all the item names in a string
    name_str = ""
    for x in chosen_item_name:
        name_str += f"{x}\n"
    var_item_name.set(name_str)

    # Storing all the item quantities in a string
    qty_str = ""
    for x in chosen_item_qty:
        qty_str += f"{x}\n"
    var_item_quantity.set(qty_str)

    # Storing all the item amounts in a string
    amt_str = ""
    for x in chosen_item_amt:
        amt_str += f"{x}\n"
    var_item_amt.set(amt_str)

    # Finding and storing the total amount without GST
    amt_wo_gst = 0
    for x in chosen_item_amt:
        amt_wo_gst += x
    var_total_amt_wo_gst.set(f"Sub Total :\t\t{amt_wo_gst}")
    print(amt_wo_gst)

    # Calculating GST
    gst = ((6 / 100) * amt_wo_gst)
    var_gst_amt.set(f"GST :\t\t{gst:.2f}\t(6%)")

    # Finding Total Amount
    amt_w_gst = amt_wo_gst + gst
    var_total_amt_w_gst.set(f"Final Amount :\t{amt_w_gst:.2f}")

    txtfile = open("reservation details.txt", "w")
    txtfile.write(
        f"Hey {fullname}\nBooking has been confirmed, here are the details :\nName : {fullname}\nRestaurant : KFC, {city}\nTimeslot : {timeslot}\nNumber of People : {num_of_ppl}\nTotal Amount : {amt_w_gst}Rs.\n\n")
    txtfile.close()


kfc_chicken = tk.Label(frame5, text="CHICKEN:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
kfc_chicken.place(x=20, y=80)

kfc_price_1 = tk.Label(frame5, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
kfc_price_1.place(x=280, y=80)

kfc_price_2 = tk.Label(frame5, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
kfc_price_2.place(x=800, y=80)

big_8 = tk.Label(frame5, text="Big 8", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
big_8.place(x=50, y=120)

price_big_8 = Label(frame5, text="Rs.620", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_big_8.place(x=315, y=120)

qty_big_8 = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_big_8.place(x=440, y=120)

var_big_8 = IntVar(value=0)
sb_big_8 = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_big_8)
sb_big_8.place(x=470, y=120)

big_12 = tk.Label(frame5, text="Big 12", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
big_12.place(x=50, y=160)

price_big_12 = Label(frame5, text="Rs.730", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_big_12.place(x=315, y=160)

qty_big_12 = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_big_12.place(x=440, y=160)

var_big_12 = IntVar(value=0)
sb_big_12 = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_big_12)
sb_big_12.place(x=470, y=160)

bucket_2 = tk.Label(frame5, text="Bucket for 2", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
bucket_2.place(x=50, y=200)

price_bucket_2 = Label(frame5, text="Rs.600", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_bucket_2.place(x=315, y=200)

qty_bucket_2 = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_bucket_2.place(x=440, y=200)

var_bucket_2 = IntVar(value=0)
sb_bucket_2 = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_bucket_2)
sb_bucket_2.place(x=470, y=200)

saving_bucket = tk.Label(frame5, text="Ultimate Savings Bucket", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
saving_bucket.place(x=50, y=240)

price_saving_bucket = Label(frame5, text="Rs.700", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_saving_bucket.place(x=315, y=240)

qty_saving_bucket = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_saving_bucket.place(x=440, y=240)

var_saving_bucket = IntVar(value=0)
sb_saving_bucket = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_saving_bucket)
sb_saving_bucket.place(x=470, y=240)

kfc_beverages = tk.Label(frame5, text="BEVERAGES:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
kfc_beverages.place(x=20, y=300)

red_bull = tk.Label(frame5, text="Red Bull", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
red_bull.place(x=50, y=340)

price_red_bull = Label(frame5, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_red_bull.place(x=315, y=340)

qty_red_bull = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_red_bull.place(x=440, y=340)

var_red_bull = IntVar(value=0)
sb_red_bull = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_red_bull)
sb_red_bull.place(x=470, y=340)

pepsi = tk.Label(frame5, text="Pepsi Can", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
pepsi.place(x=50, y=380)

price_pepsi = Label(frame5, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_pepsi.place(x=315, y=380)

qty_pepsi = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_pepsi.place(x=440, y=380)

var_pepsi = IntVar(value=0)
sb_pepsi = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_pepsi)
sb_pepsi.place(x=470, y=380)

mirinda = tk.Label(frame5, text="Mirinda Can", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mirinda.place(x=50, y=420)

price_mirinda = Label(frame5, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mirinda.place(x=315, y=420)

qty_mirinda = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mirinda.place(x=440, y=420)

var_mirinda = IntVar(value=0)
sb_mirinda = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_mirinda)
sb_mirinda.place(x=470, y=420)

kfc_burgers = tk.Label(frame5, text="BURGERS:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
kfc_burgers.place(x=20, y=480)

veg_zinger = tk.Label(frame5, text="Veg Zinger Burger", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
veg_zinger.place(x=50, y=520)

price_veg_zinger = Label(frame5, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_veg_zinger.place(x=315, y=520)

qty_veg_zinger = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_veg_zinger.place(x=440, y=520)

var_veg_zinger = IntVar(value=0)
sb_veg_zinger = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_veg_zinger)
sb_veg_zinger.place(x=470, y=520)

classic_zinger = tk.Label(frame5, text="Classic Zinger Burger", bg="#310054", fg="#00f3b2",
                          font=['Calibri', 15, 'bold'])
classic_zinger.place(x=50, y=560)

price_classic_zinger = Label(frame5, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_classic_zinger.place(x=315, y=560)

qty_classic_zinger = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_classic_zinger.place(x=440, y=560)

var_classic_zinger = IntVar(value=0)
sb_classic_zinger = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_classic_zinger)
sb_classic_zinger.place(x=470, y=560)

tand_zinger = tk.Label(frame5, text="Tandoori Zinger Burger", bg="#310054", fg="#00f3b2",
                       font=['Calibri', 15, 'bold'])
tand_zinger.place(x=50, y=600)

price_tand_zinger = Label(frame5, text="Rs.200", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_tand_zinger.place(x=315, y=600)

qty_tand_zinger = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_tand_zinger.place(x=440, y=600)

var_tand_zinger = IntVar(value=0)
sb_tand_zinger = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_tand_zinger)
sb_tand_zinger.place(x=470, y=600)

double_down = tk.Label(frame5, text="2 Double Down Burgers", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
double_down.place(x=50, y=640)

price_double_down = Label(frame5, text="Rs.500", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_double_down.place(x=315, y=640)

qty_double_down = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_double_down.place(x=440, y=640)

var_double_down = IntVar(value=0)
sb_double_down = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_double_down)
sb_double_down.place(x=470, y=640)

kfc_snacks = tk.Label(frame5, text="SNACKS:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
kfc_snacks.place(x=620, y=80)

veg_patty = tk.Label(frame5, text="2 pc Veg Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
veg_patty.place(x=650, y=120)

price_veg_patty = Label(frame5, text="Rs.140", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_veg_patty.place(x=850, y=120)

qty_veg_patty = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_veg_patty.place(x=960, y=120)

var_veg_patty = IntVar(value=0)
sb_veg_patty = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_veg_patty)
sb_veg_patty.place(x=990, y=120)

kfc_m_fries = tk.Label(frame5, text="Medium Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
kfc_m_fries.place(x=650, y=160)

price_kfc_m_fries = Label(frame5, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_kfc_m_fries.place(x=850, y=160)

qty_kfc_m_fries = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_kfc_m_fries.place(x=960, y=160)

var_kfc_m_fries = IntVar(value=0)
sb_kfc_m_fries = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_kfc_m_fries)
sb_kfc_m_fries.place(x=990, y=160)

kfc_l_fries = tk.Label(frame5, text="Large Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
kfc_l_fries.place(x=650, y=200)

price_kfc_l_fries = Label(frame5, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_kfc_l_fries.place(x=850, y=200)

qty_kfc_l_fries = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_kfc_l_fries.place(x=960, y=200)

var_kfc_l_fries = IntVar(value=0)
sb_kfc_l_fries = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_kfc_l_fries)
sb_kfc_l_fries.place(x=990, y=200)

sm_red_chicken = tk.Label(frame5, text="Smokey Red Chicken", bg="#310054", fg="#00f3b2",
                          font=['Calibri', 15])
sm_red_chicken.place(x=650, y=240)

price_sm_red_chicken = Label(frame5, text="Rs.220", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_sm_red_chicken.place(x=850, y=240)

qty_sm_red_chicken = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_sm_red_chicken.place(x=960, y=240)

var_sm_red_chicken = IntVar(value=0)
sb_sm_red_chicken = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_sm_red_chicken)
sb_sm_red_chicken.place(x=990, y=240)

mingles = tk.Label(frame5, text="Mingles Bucket", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mingles.place(x=650, y=280)

price_mingles = Label(frame5, text="Rs.310", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mingles.place(x=850, y=280)

qty_mingles = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mingles.place(x=960, y=280)

var_mingles = IntVar(value=0)
sb_mingles = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_mingles)
sb_mingles.place(x=990, y=280)

med_popcorn = tk.Label(frame5, text="Medium Popcorn", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
med_popcorn.place(x=650, y=320)

price_med_popcorn = Label(frame5, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_med_popcorn.place(x=850, y=320)

qty_med_popcorn = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_med_popcorn.place(x=960, y=320)

var_med_popcorn = IntVar(value=0)
sb_med_popcorn = Spinbox(frame5, from_=0, to=100, width=3, textvariable=var_med_popcorn)
sb_med_popcorn.place(x=990, y=320)

b_kfc_get_bill = tk.Button(frame5, text="Get Bill", command=kfc_get_order)
b_kfc_get_bill.place(x=1050, y=575)
b_kfc_get_bill["width"] = 20
b_kfc_get_bill["fg"] = "#00f3b2"
b_kfc_get_bill["highlightbackground"] =  "#310054"

b_kfc_back = tk.Button(frame5, text="Back", command=lambda: show_frame(frame3))
b_kfc_back.place(x=850, y=575)
b_kfc_back["width"] = 20
b_kfc_back["fg"] =  "#00f3b2"
b_kfc_back["highlightbackground"] = "#310054"

# ========================================================================================(menu - dunkin)FRAME 6
root.geometry("600x500")
bg_label_f4 = tk.Label(frame6, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

dunkin_label = tk.Label(frame6, text="MENU - DUNKIN' DONUTS ")
dunkin_label["fg"] = "#ffa500"
dunkin_label["bg"] = "#310054"
dunkin_label["font"] = ("Al Bayan", 30, "underline","bold")
dunkin_label.place(x=480, y=10)


def dunkin_get_order():
    global city
    city = temp.get()
    var_restaurant.set(f"Restaurant :     Dunkin' Donuts, {city}")
    show_frame(frame8)
    dunkin_all_items = []
    dunkin_all_items.append(("Rainbow Pop", int(var_rainbow_pop.get()), 90))
    dunkin_all_items.append(("Choco Pop", int(var_choco_pop.get()), 90))
    dunkin_all_items.append(("Boston Crème", int(var_boston_creme.get()), 90))
    dunkin_all_items.append(("Choco Overdose", int(var_choco_overdose.get()), 90))
    dunkin_all_items.append(("Peanut Butter Island", int(var_peanut_butter.get()), 100))
    dunkin_all_items.append(("White Choco & Strawberry", int(var_white_choc_strawberry.get()), 100))
    dunkin_all_items.append(("Chocotella", int(var_chocotella.get()), 100))
    dunkin_all_items.append(("Choco Berry Bomb", int(var_choco_berry.get()), 100))
    dunkin_all_items.append(("Caramel Dunkaccino", int(var_caramel_dunk.get()), 190))
    dunkin_all_items.append(("Virgin Mojito", int(var_virgin_mojito.get()), 120))
    dunkin_all_items.append(("Fruit Berry", int(var_fruit_berry.get()), 210))
    dunkin_all_items.append(("Caramel Iced Coffee", int(var_caramel_ice_coffee.get()), 190))
    dunkin_all_items.append(("Potato Wedges", int(var_dunkin_wedges.get()), 80))
    dunkin_all_items.append(("Veg Nachos", int(var_veg_nachos.get()), 100))
    dunkin_all_items.append(("Chicken Nachos", int(var_chicken_nachos.get()), 110))

    # Adding the items the user has selected in this list
    chosen_item_amt = []
    for (name, qty, price) in dunkin_all_items:
        if qty > 0:
            chosen_item_name.append(name)
            chosen_item_qty.append(qty)
            chosen_item_price.append(price)
            chosen_item_amt.append(qty * price)
    print(f"{chosen_item_name}\n{chosen_item_qty}\n{chosen_item_price}\n{chosen_item_amt}")

    # Storing all the item names in a string
    name_str = ""
    for x in chosen_item_name:
        name_str += f"{x}\n"
    var_item_name.set(name_str)

    # Storing all the item quantities in a string
    qty_str = ""
    for x in chosen_item_qty:
        qty_str += f"{x}\n"
    var_item_quantity.set(qty_str)

    # Storing all the item amounts in a string
    amt_str = ""
    for x in chosen_item_amt:
        amt_str += f"{x}\n"
    var_item_amt.set(amt_str)

    # Finding and storing the total amount without GST
    amt_wo_gst = 0
    for x in chosen_item_amt:
        amt_wo_gst += x
    var_total_amt_wo_gst.set(f"Sub Total :\t\t{amt_wo_gst}")
    print(amt_wo_gst)

    # Calculating GST
    gst = ((6 / 100) * amt_wo_gst)
    var_gst_amt.set(f"GST :\t\t{gst:.2f}\t(6%)")

    # Finding Total Amount
    amt_w_gst = amt_wo_gst + gst
    var_total_amt_w_gst.set(f"Final Amount :\t{amt_w_gst:.2f}")

    txtfile = open("reservation details.txt", "w")
    txtfile.write(
        f"Hey {fullname}\nBooking has been confirmed, here are the details :\nName : {fullname}\nRestaurant : Dunkin' Donuts, {city}\nTimeslot : {timeslot}\nNumber of people : {num_of_ppl}\nTotal Amount : {amt_w_gst}Rs.\n\n")
    txtfile.close()


dunkin_donuts = tk.Label(frame6, text="DONUTS:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
dunkin_donuts.place(x=20, y=80)

price_1 = tk.Label(frame6, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
price_1.place(x=280, y=80)

price_2 = tk.Label(frame6, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
price_2.place(x=800, y=80)

rainbow_pop = tk.Label(frame6, text="Rainbow Pop", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
rainbow_pop.place(x=50, y=120)

price_rainbow_pop = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_rainbow_pop.place(x=315, y=120)

qty_rainbow_pop = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_rainbow_pop.place(x=440, y=120)

var_rainbow_pop = IntVar()
sb_rainbow_pop = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_rainbow_pop)
sb_rainbow_pop.place(x=470, y=120)

choco_pop = tk.Label(frame6, text="Choco Pop", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
choco_pop.place(x=50, y=160)

price_choco_pop = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_choco_pop.place(x=315, y=160)

qty_choco_pop = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_choco_pop.place(x=440, y=160)

var_choco_pop = IntVar()
sb_choco_pop = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_choco_pop)
sb_choco_pop.place(x=470, y=160)

boston_creme = tk.Label(frame6, text="Boston Crème", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
boston_creme.place(x=50, y=200)

price_boston_creme = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_boston_creme.place(x=315, y=200)

qty_boston_creme = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_boston_creme.place(x=440, y=200)

var_boston_creme = IntVar()
sb_boston_creme = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_boston_creme)
sb_boston_creme.place(x=470, y=200)

choco_overdose = tk.Label(frame6, text="Choco Overdose", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
choco_overdose.place(x=50, y=240)

price_choco_overdose = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_choco_overdose.place(x=315, y=240)

qty_choco_overdose = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_choco_overdose.place(x=440, y=240)

var_choco_overdose = IntVar()
sb_choco_overdose = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_choco_overdose)
sb_choco_overdose.place(x=470, y=240)

peanut_butter = tk.Label(frame6, text="Peanut Butter Island", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
peanut_butter.place(x=50, y=280)

price_peanut_butter = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_peanut_butter.place(x=315, y=280)

qty_peanut_butter = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_peanut_butter.place(x=440, y=280)

var_peanut_butter = IntVar()
sb_peanut_butter = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_peanut_butter)
sb_peanut_butter.place(x=470, y=280)

white_choc_strawberry = tk.Label(frame6, text="White Choco & Strawberry", bg="#310054", fg="#00f3b2",
                                 font=['Calibri', 15])
white_choc_strawberry.place(x=50, y=320)

price_white_choc_strawberry = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_white_choc_strawberry.place(x=315, y=320)

qty_white_choc_strawberry = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_white_choc_strawberry.place(x=440, y=320)

var_white_choc_strawberry = IntVar()
sb_white_choc_strawberry = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_white_choc_strawberry)
sb_white_choc_strawberry.place(x=470, y=320)

chocotella = tk.Label(frame6, text="Chocotella", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
chocotella.place(x=50, y=360)

price_chocotella = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_chocotella.place(x=315, y=360)

qty_chocotella = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_chocotella.place(x=440, y=360)

var_chocotella = IntVar()
sb_chocotella = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_chocotella)
sb_chocotella.place(x=470, y=360)

choco_berry = tk.Label(frame6, text="Choco Berry Bomb", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
choco_berry.place(x=50, y=400)

price_choco_berry = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_choco_berry.place(x=315, y=400)

qty_choco_berry = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_choco_berry.place(x=440, y=400)

var_choco_berry = IntVar()
sb_choco_berry = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_choco_berry)
sb_choco_berry.place(x=470, y=400)

dunkin_beverages = tk.Label(frame6, text="BEVERAGES:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
dunkin_beverages.place(x=20, y=460)

caramel_dunk = tk.Label(frame6, text="Caramel Dunkaccino", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
caramel_dunk.place(x=50, y=500)

price_caramel_dunk = Label(frame6, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_caramel_dunk.place(x=315, y=500)

qty_caramel_dunk = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_caramel_dunk.place(x=440, y=500)

var_caramel_dunk = IntVar()
sb_caramel_dunk = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_caramel_dunk)
sb_caramel_dunk.place(x=470, y=500)

virgin_mojito = tk.Label(frame6, text="Virgin Mojito", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
virgin_mojito.place(x=50, y=540)

price_virgin_mojito = Label(frame6, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_virgin_mojito.place(x=315, y=540)

qty_virgin_mojito = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_virgin_mojito.place(x=440, y=540)

var_virgin_mojito = IntVar()
sb_virgin_mojito = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_virgin_mojito)
sb_virgin_mojito.place(x=470, y=540)

fruit_berry = tk.Label(frame6, text="Fruit Berry", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
fruit_berry.place(x=50, y=580)

price_fruit_berry = Label(frame6, text="Rs.210", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_fruit_berry.place(x=315, y=580)

qty_fruit_berry = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_fruit_berry.place(x=440, y=580)

var_fruit_berry = IntVar()
sb_fruit_berry = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_fruit_berry)
sb_fruit_berry.place(x=470, y=580)

caramel_ice_coffee = tk.Label(frame6, text="Caramel Iced Coffee", bg="#310054", fg="#00f3b2",
                              font=['Calibri', 15])
caramel_ice_coffee.place(x=50, y=620)

price_caramel_ice_coffee = Label(frame6, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_caramel_ice_coffee.place(x=315, y=620)

qty_caramel_ice_coffee = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_caramel_ice_coffee.place(x=440, y=620)

var_caramel_ice_coffee = IntVar()
sb_caramel_ice_coffee = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_caramel_ice_coffee)
sb_caramel_ice_coffee.place(x=470, y=620)

dunkin_sides = tk.Label(frame6, text="SIDES & EXTRAS:", bg="#310054", fg="#ffa500", font=['Calibri', 17,"bold"])
dunkin_sides.place(x=620, y=80)

dunkin_wedges = tk.Label(frame6, text="Potato Wedges", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
dunkin_wedges.place(x=630, y=130)

price_dunkin_wedges = Label(frame6, text="Rs.80", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_dunkin_wedges.place(x=850, y=130)

qty_dunkin_wedges = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_dunkin_wedges.place(x=960, y=130)

var_dunkin_wedges = IntVar()
sb_dunkin_wedges = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_dunkin_wedges)
sb_dunkin_wedges.place(x=990, y=130)

veg_nachos = tk.Label(frame6, text="Veg Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
veg_nachos.place(x=630, y=170)

price_veg_nachos = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_veg_nachos.place(x=850, y=170)

qty_veg_nachos = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_veg_nachos.place(x=960, y=170)

var_veg_nachos = IntVar()
sb_veg_nachos = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_veg_nachos)
sb_veg_nachos.place(x=990, y=170)

chicken_nachos = tk.Label(frame6, text="Chicken Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
chicken_nachos.place(x=630, y=210)

price_chicken_nachos = Label(frame6, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_chicken_nachos.place(x=850, y=210)

qty_chicken_nachos = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_chicken_nachos.place(x=960, y=210)

var_chicken_nachos = IntVar()
sb_chicken_nachos = Spinbox(frame6, from_=0, to=100, width=3, textvariable=var_chicken_nachos)
sb_chicken_nachos.place(x=990, y=210)

b_dunkin_get_bill = tk.Button(frame6, text="Get Bill", command=dunkin_get_order)
b_dunkin_get_bill.place(x=1050, y=575)
b_dunkin_get_bill["width"] = 20
b_dunkin_get_bill["fg"] =  "#00f3b2"
b_dunkin_get_bill["highlightbackground"] = "#310054"

b_dunkin_back = tk.Button(frame6, text="Back", command=lambda: show_frame(frame3))
b_dunkin_back.place(x=850, y=575)
b_dunkin_back["width"] = 20
b_dunkin_back["fg"] = "#00f3b2"
b_dunkin_back["highlightbackground"] = "#310054"

# ========================================================================================(menu - subway)FRAME 7
root.geometry("600x500")
bg_label_f4 = tk.Label(frame7, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

subway_label = tk.Label(frame7, text="MENU - SUBWAY ")
subway_label["fg"] = "#ffa500"
subway_label["bg"] = "#310054"
subway_label["font"] = ("Al Bayan", 30, "underline","bold")
subway_label.place(x=510, y=10)


def subway_get_order():
    show_frame(frame8)
    global city
    city = temp.get()
    var_restaurant.set(f"Restaurant :     Subway, {city}")
    subway_all_items = []
    subway_all_items.append(("Chicken Teriyaki", int(var_chicken_teriyaki.get()), 260))
    subway_all_items.append(("Corn & Peas", int(var_corn_peas.get()), 230))
    subway_all_items.append(("Peri Peri Chicken", int(var_peri_peri_chicken.get()), 250))
    subway_all_items.append(("Mexican Patty", int(var_mex_patty.get()), 230))
    subway_all_items.append(("Paneer Tikka", int(var_sub_paneer_tikka.get()), 230))
    subway_all_items.append(("Mountain Dew", int(var_mountain_dew.get()), 60))
    subway_all_items.append(("Orange Juice", int(var_orange_juice.get()), 70))
    subway_all_items.append(("Iced Tea", int(var_subway_iced_tea.get()), 50))
    subway_all_items.append(("Rich Chocolate Truffle", int(var_choc_truffle.get()), 60))
    subway_all_items.append(("Chocolate Cookie", int(var_choc_cookie.get()), 30))
    subway_all_items.append(("Lays Chips (Classic)", int(var_lays_classic.get()), 25))
    subway_all_items.append(("Nachos", int(var_nachos.get()), 100))
    subway_all_items.append(("Hash Browns", int(var_hashbrown.get()), 90))
    subway_all_items.append(("Chorizo Flatbread Pizza", int(var_chorizo.get()), 150))

    # Adding the items the user has selected in this list
    chosen_item_amt = []
    for (name, qty, price) in subway_all_items:
        if qty > 0:
            chosen_item_name.append(name)
            chosen_item_qty.append(qty)
            chosen_item_price.append(price)
            chosen_item_amt.append(qty * price)
    print(f"{chosen_item_name}\n{chosen_item_qty}\n{chosen_item_price}\n{chosen_item_amt}")

    # Storing all the item names in a string
    name_str = ""
    for x in chosen_item_name:
        name_str += f"{x}\n"
    var_item_name.set(name_str)

    # Storing all the item quantities in a string
    qty_str = ""
    for x in chosen_item_qty:
        qty_str += f"{x}\n"
    var_item_quantity.set(qty_str)

    # Storing all the item amounts in a string
    amt_str = ""
    for x in chosen_item_amt:
        amt_str += f"{x}\n"
    var_item_amt.set(amt_str)

    # Finding and storing the total amount without GST
    amt_wo_gst = 0
    for x in chosen_item_amt:
        amt_wo_gst += x
    var_total_amt_wo_gst.set(f"Sub Total :\t\t{amt_wo_gst}")
    print(amt_wo_gst)

    # Calculating GST
    gst = ((6 / 100) * amt_wo_gst)
    var_gst_amt.set(f"GST :\t\t{gst:.2f}\t(6%)")

    # Finding Total Amount
    amt_w_gst = amt_wo_gst + gst
    var_total_amt_w_gst.set(f"Final Amount :\t{amt_w_gst:.2f}")

    txtfile = open("reservation details.txt", "w")
    txtfile.write(
        f"Hey {fullname}\nBooking has been confirmed, here are the details :\nName : {fullname}\nRestaurant : Subway, {city}\nTimeslot : {timeslot}\nNumber of people : {num_of_ppl}\nTotal Amount : {amt_w_gst}Rs.\n\n")
    txtfile.close()


subway_wraps = tk.Label(frame7, text="SIGNATURE WRAPS:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
subway_wraps.place(x=20, y=80)

subway_price_1 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
subway_price_1.place(x=280, y=80)

subway_price_2 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
subway_price_2.place(x=800, y=80)

chicken_teriyaki = tk.Label(frame7, text="Chicken Teriyaki", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
chicken_teriyaki.place(x=50, y=160)

price_chicken_teriyaki = Label(frame7, text="Rs.260", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_chicken_teriyaki.place(x=315, y=160)

qty_chicken_teriyaki = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_chicken_teriyaki.place(x=440, y=160)

var_chicken_teriyaki = IntVar(value=0)
sb_chicken_teriyaki = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_chicken_teriyaki)
sb_chicken_teriyaki.place(x=470, y=160)

corn_peas = tk.Label(frame7, text="Corn and Peas", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
corn_peas.place(x=50, y=200)

price_corn_peas = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_corn_peas.place(x=315, y=200)

qty_corn_peas = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_corn_peas.place(x=440, y=200)

var_corn_peas = IntVar(value=0)
sb_corn_peas = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_corn_peas)
sb_corn_peas.place(x=470, y=200)

peri_peri_chicken = tk.Label(frame7, text="Peri Peri Chicken", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
peri_peri_chicken.place(x=50, y=240)

price_peri_peri_chicken = Label(frame7, text="Rs.250", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_peri_peri_chicken.place(x=315, y=240)

qty_peri_peri_chicken = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_peri_peri_chicken.place(x=440, y=240)

var_peri_peri_chicken = IntVar(value=0)
sb_peri_peri_chicken = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_peri_peri_chicken)
sb_peri_peri_chicken.place(x=470, y=240)

mex_patty = tk.Label(frame7, text="Mexican Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mex_patty.place(x=50, y=280)

price_mex_patty = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mex_patty.place(x=315, y=280)

qty_mex_patty = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mex_patty.place(x=440, y=280)

var_mex_patty = IntVar(value=0)
sb_mex_patty = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_mex_patty)
sb_mex_patty.place(x=470, y=280)

sub_paneer_tikka = tk.Label(frame7, text="Paneer Tikka", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
sub_paneer_tikka.place(x=50, y=320)

price_sub_paneer_tikka = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_sub_paneer_tikka.place(x=315, y=320)

qty_sub_paneer_tikka = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_sub_paneer_tikka.place(x=440, y=320)

var_sub_paneer_tikka = IntVar(value=0)
sb_sub_paneer_tikka = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_sub_paneer_tikka)
sb_sub_paneer_tikka.place(x=470, y=320)

subway_beverages = tk.Label(frame7, text="BEVERAGES:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
subway_beverages.place(x=20, y=380)

mountain_dew = tk.Label(frame7, text="Mountain Dew", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
mountain_dew.place(x=50, y=420)

price_mountain_dew = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_mountain_dew.place(x=315, y=420)

qty_mountain_dew = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_mountain_dew.place(x=440, y=420)

var_mountain_dew = IntVar(value=0)
sb_mountain_dew = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_mountain_dew)
sb_mountain_dew.place(x=470, y=420)

orange_juice = tk.Label(frame7, text="Orange Juice", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
orange_juice.place(x=50, y=460)

price_orange_juice = Label(frame7, text="Rs.70", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_orange_juice.place(x=315, y=460)

qty_orange_juice = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_orange_juice.place(x=440, y=460)

var_orange_juice = IntVar(value=0)
sb_orange_juice = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_orange_juice)
sb_orange_juice.place(x=470, y=460)

subway_iced_tea = tk.Label(frame7, text="Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
subway_iced_tea.place(x=50, y=500)

price_subway_iced_tea = Label(frame7, text="Rs.50", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_subway_iced_tea.place(x=315, y=500)

qty_subway_iced_tea = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_subway_iced_tea.place(x=440, y=500)

var_subway_iced_tea = IntVar(value=0)
sb_subway_iced_tea = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_subway_iced_tea)
sb_subway_iced_tea.place(x=470, y=500)

subway_desserts = tk.Label(frame7, text="DESSERTS:", bg="#310054", fg="#ffa500", font=['Calibri', 17,"bold"])
subway_desserts.place(x=20, y=560)

choc_truffle = tk.Label(frame7, text="Rich Chocolate Truffle", bg="#310054", fg="#00f3b2",
                        font=['Calibri', 15, 'bold'])
choc_truffle.place(x=50, y=600)

price_choc_truffle = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_choc_truffle.place(x=315, y=600)

qty_choc_truffle = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_choc_truffle.place(x=440, y=600)

var_choc_truffle = IntVar(value=0)
sb_choc_truffle = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_choc_truffle)
sb_choc_truffle.place(x=470, y=600)

choc_cookie = tk.Label(frame7, text="Chocolate Cookie", bg="#310054", fg="#00f3b2",
                       font=['Calibri', 15])
choc_cookie.place(x=50, y=640)

price_choc_cookie = Label(frame7, text="Rs.30", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_choc_cookie.place(x=315, y=640)

qty_choc_cookie = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_choc_cookie.place(x=440, y=640)

var_choc_cookie = IntVar(value=0)
sb_choc_cookie = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_choc_cookie)
sb_choc_cookie.place(x=470, y=640)

subway_sides = tk.Label(frame7, text="SIDES & EXTRAS:", bg="#310054", fg="#ffa500", font=['Calibri', 17, 'bold'])
subway_sides.place(x=620, y=80)

lays_classic = tk.Label(frame7, text="Lays Chips (Classic)", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
lays_classic.place(x=650, y=120)

price_lays_classic = Label(frame7, text="Rs.25", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_lays_classic.place(x=850, y=120)

qty_lays_classic = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_lays_classic.place(x=960, y=120)

var_lays_classic = IntVar(value=0)
sb_lays_classic = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_lays_classic)
sb_lays_classic.place(x=990, y=120)

nachos = tk.Label(frame7, text="Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
nachos.place(x=650, y=160)

price_nachos = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_nachos.place(x=850, y=160)

qty_nachos = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_nachos.place(x=960, y=160)

var_nachos = IntVar(value=0)
sb_nachos = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_nachos)
sb_nachos.place(x=990, y=160)

hashbrown = tk.Label(frame7, text="Hash Browns", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
hashbrown.place(x=650, y=200)

price_hashbrown = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_hashbrown.place(x=850, y=200)

qty_hashbrown = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_hashbrown.place(x=960, y=200)

var_hashbrown = IntVar(value=0)
sb_hashbrown = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_hashbrown)
sb_hashbrown.place(x=990, y=200)

chorizo = tk.Label(frame7, text="Chorizo Flatbread Pizza", bg="#310054", fg="#00f3b2",
                   font=['Calibri', 15])
chorizo.place(x=600, y=240)

price_chorizo = Label(frame7, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15])
price_chorizo.place(x=850, y=240)

qty_chorizo = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11])
qty_chorizo.place(x=960, y=240)

var_chorizo = IntVar(value=0)
sb_chorizo = Spinbox(frame7, from_=0, to=100, width=3, textvariable=var_chorizo)
sb_chorizo.place(x=990, y=240)

b_subway_get_bill = tk.Button(frame7, text="Get Bill", command=subway_get_order)
b_subway_get_bill.place(x=1050, y=575)
b_subway_get_bill["width"] = 20
b_subway_get_bill["fg"] = "#00f3b2"
b_subway_get_bill["highlightbackground"] = "#310054"

b_subway_back = tk.Button(frame7, text="Back", command=lambda: show_frame(frame3))
b_subway_back.place(x=850, y=575)
b_subway_back["width"] = 20
b_subway_back["fg"] =  "#00f3b2"
b_subway_back["highlightbackground"] = "#310054"

# ==================(BILL)
bg_label_f8 = Label(frame8, bg="#310054")
bg_label_f8.pack(fill='both', expand=True)

# Bill Frame Heading Label
bill_label = tk.Label(frame8, text="BILL")
bill_label["fg"] = "#ffa500"
bill_label["bg"] = "#310054"
bill_label["font"] = ( "Al Bayan",30, "underline","bold")
bill_label.place(x=600, y=30)

line_c1 = Canvas(frame8,width = 900,height = 500,bg = "#310054" )
line_c1.create_line(0,50,1000,50,fill = "#00f3b2")
line_c1.create_line(0,300,1000,300,fill = "#00f3b2")
line_c1.create_line(300,0,300,300,fill = "#00f3b2")
line_c1.create_line(600,0,600,300,fill = "#00f3b2")
line_c1.place(x = 210,y= 90)

# Items Column Header
l_items = Label(frame8, text="Items", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
l_items.place(x=300, y=100)

# Quantity Column Header
l_qty = Label(frame8, text="Quantity", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
l_qty.place(x=600, y=100)

# Amount Column Header
l_amt = Label(frame8, text="Amount", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
l_amt.place(x=900, y=100)

# Label to Display item names
var_item_name = StringVar()
l_bill_name = Label(frame8, anchor="w", textvariable=var_item_name, bg="#310054", fg="#00f3b2",
                    font=['Calibri', 14, 'bold'])
l_bill_name.place(x=250, y=150)

# Label to Display item quantity
var_item_quantity = StringVar()
l_bill_qty = Label(frame8, anchor="w", textvariable=var_item_quantity, bg="#310054", fg="#00f3b2",
                   font=['Calibri', 14, "bold"])
l_bill_qty.place(x=630, y=150)

# Label to Display item amount
var_item_amt = StringVar()
l_bill_amt = Label(frame8, anchor="w", textvariable=var_item_amt, bg="#310054", fg="#00f3b2",
                   font=['Calibri', 14, 'bold'])
l_bill_amt.place(x=930, y=150)

# Label to Display Total Amount without GST
var_total_amt_wo_gst = StringVar()
l_amt_wo_gst = Label(frame8, anchor="w", textvariable=var_total_amt_wo_gst, bg="#310054", fg="#ffa500",
                     font=['Calibri', 14, 'bold'])
l_amt_wo_gst.place(x=300, y=410)

# Label to show GST Amount
var_gst_amt = StringVar()
l_gst_amt = Label(frame8, anchor="w", textvariable=var_gst_amt, bg="#310054", fg="#ffa500",
                  font=['Calibri', 14, 'bold'])
l_gst_amt.place(x=300, y=440)

# Label to show Total Amount with GST
var_total_amt_w_gst = StringVar()
l_amt_w_gst = Label(frame8, anchor="w", textvariable=var_total_amt_w_gst, bg="#310054", fg="#ffa500",
                    font=['Calibri', 14, 'bold'])
l_amt_w_gst.place(x=300, y=470)

# Next Window Button
res_details = tk.Button(frame8, text="Show Reservation Details", command=lambda: show_frame(frame9))
res_details.place(x=850, y=625)
res_details["width"] = 30
res_details["fg"] =  "#00f3b2"
res_details["highlightbackground"] = "#310054"

# Previous Window Button
bill_back = tk.Button(frame8, text="Back", command=lambda: show_frame(frame3))
bill_back.place(x=650, y=625)
bill_back["width"] = 20
bill_back["fg"] = "#00f3b2"
bill_back["highlightbackground"] = "#310054"

# ==================(RESERVATION CONFIRMATION)

bg_label_f9 = Label(frame9, bg="#310054")
bg_label_f9.pack(fill='both', expand=True)


def send_email():
    # Sending email
    sender_email = "foodhunter.reservation@gmail.com"
    sender_pass = "heenashevde"
    rec_email = email_entrytext.get()
    txtfile = open("reservation details.txt", "r")
    message = txtfile.read()
    txtfile.close()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_pass)
    content = f"Subject : Restaurant Reservation\n\n{message}"
    server.sendmail(sender_email, rec_email, content)
    server.quit()


def exit_program():
    send_email()
    root.destroy()


# Frame Title
confirm_label = tk.Label(frame9, text="RESERVATION CONFIRMATION")
confirm_label["fg"] =  "#ffa500"
confirm_label["bg"] = "#310054"
confirm_label["font"] = ("Al Bayan", 30, "underline","bold")
confirm_label.place(x=430, y=40)

# Name Confirmation Label
var_name = StringVar()
l_name = Label(frame9, textvariable=var_name, bg="#310054", fg="#00f3b2", font=['Calibri', 20, 'bold'])
l_name.place(x=260, y=150)

# Restaurant Confirmation Label
var_restaurant = StringVar()
l_restaurant = Label(frame9, textvariable=var_restaurant, bg="#310054", fg="#00f3b2", font=['Calibri', 20, 'bold'])
l_restaurant.place(x=260, y=200)

# Time Slot Confirmation Label
var_time = StringVar()
l_time = Label(frame9, textvariable=var_time, bg="#310054", fg="#00f3b2", font=['Calibri', 20, 'bold'])
l_time.place(x=260, y=250)

# Number of People Confirmation Label
var_num_ppl = StringVar()
l_num_ppl = Label(frame9, textvariable=var_num_ppl, bg="#310054", fg="#00f3b2", font=['Calibri', 20, 'bold'])
l_num_ppl.place(x=260, y=300)

# Previous Window Button
confirm_back = tk.Button(frame9, text="See Bill Details", command=lambda: show_frame(frame8))
confirm_back.place(x=400, y=500)
confirm_back["width"] = 20
confirm_back["fg"] ="#00f3b2"
confirm_back["highlightbackground"] = "#310054"

# Exit Button
exit_button = tk.Button(frame9, text="Confirm and Exit", command=exit_program)
exit_button.place(x=630, y=500)
exit_button["width"] = 20
exit_button["fg"] = "#00f3b2"
exit_button["highlightbackground"] = "#310054"

show_frame(frame1)

root.mainloop()
