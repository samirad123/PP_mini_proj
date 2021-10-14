import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


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
registration_form_label["font"] = ("Calibri", 30, "underline")
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
button_submit.place(x=300, y=400)
button_submit["width"] = 20
button_submit["fg"] = "#00f3b2"
button_submit["highlightbackground"] = "#310054"

# Submit Button
button_back = tk.Button(frame2, text="Back", command=lambda: show_frame(frame1))
button_back.place(x=130, y=400)
button_back["width"] = 20
button_back["fg"] = "#00f3b2"
button_back["highlightbackground"] = "#310054"

# ==================Frame 3 code

root.geometry("800x900")
bg_label_f3 = tk.Label(frame3, bg="#310054")
bg_label_f3.pack(fill='both', expand=True)

# restaurants title label
resto_label = tk.Label(frame3, text="CHOOSE THE RESTAURANTS")
resto_label["fg"] = "#00f3b2"
resto_label["bg"] = "#310054"
resto_label["font"] = ("Calibri", 30, "underline")
resto_label.place(x=100, y=40)

# image mcd logo
mcd_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/mcd_logo (1).png"))
mcd_logo_label = tk.Label(frame3, image=mcd_logo)
mcd_logo_label["highlightbackground"] = "#310054"
mcd_logo_label.place(x=90, y=100)

# mcd
mcd_label = tk.Label(frame3, text="McDonalds : ")
mcd_label["fg"] = "#00f3b2"
mcd_label["bg"] = "#310054"
mcd_label["font"] = ("Calibri", 14)
mcd_label.place(x=230, y=100)

# finish reservation button mcd
finish_button_mcd = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_mcd["fg"] = "#00f3b2"
finish_button_mcd["highlightbackground"] = "#310054"
finish_button_mcd["font"] = ("Calibri", 15)
finish_button_mcd.place(x=230, y=150)

# continue to order button mcd
continue_to_order_mcd = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame4))
continue_to_order_mcd["fg"] = "#00f3b2"
continue_to_order_mcd["highlightbackground"] = "#310054"
continue_to_order_mcd["font"] = ("Calibri", 15)
continue_to_order_mcd.place(x=400, y=150)

# image kfc
kfc_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/kfc logo img (1).png"))
kfc_logo_label = tk.Label(frame3, image=kfc_logo)
kfc_logo_label["highlightbackground"] = "#310054"
kfc_logo_label.place(x=70, y=250)

# kfc
kfc_label = tk.Label(frame3, text="KFC : ")
kfc_label["fg"] = "#00f3b2"
kfc_label["bg"] = "#310054"
kfc_label["font"] = ("Calibri", 14)
kfc_label.place(x=220, y=250)

# finish reservation button kfc
finish_button_kfc = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_kfc["fg"] = "#00f3b2"
finish_button_kfc["highlightbackground"] = "#310054"
finish_button_kfc["font"] = ("Calibri", 15)
finish_button_kfc.place(x=220, y=300)

# continue to order button kfc
continue_to_order_kfc = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame5))
continue_to_order_kfc["fg"] = "#00f3b2"
continue_to_order_kfc["highlightbackground"] = "#310054"
continue_to_order_kfc["font"] = ("Calibri", 15)
continue_to_order_kfc.place(x=390, y=300)

# image dunkin
dunkin_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/dunkin_logo (2).png"))
dunkin_logo_label = tk.Label(frame3, image=dunkin_logo)
dunkin_logo_label["highlightbackground"] = "#310054"
dunkin_logo_label.place(x=40, y=380)

# dunkin
dunkin_label = tk.Label(frame3, text="Dunkin' Donuts : ")
dunkin_label["fg"] = "#00f3b2"
dunkin_label["bg"] = "#310054"
dunkin_label["font"] = ("Calibri", 14)
dunkin_label.place(x=220, y=380)

# finish reservation button dunkin
finish_button_dunkin = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_dunkin["fg"] = "#00f3b2"
finish_button_dunkin["highlightbackground"] = "#310054"
finish_button_dunkin["font"] = ("Calibri", 15)
finish_button_dunkin.place(x=220, y=430)

# continue to order button dunkin
continue_to_order_dunkin = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame6))
continue_to_order_dunkin["fg"] = "#00f3b2"
continue_to_order_dunkin["highlightbackground"] = "#310054"
continue_to_order_dunkin["font"] = ("Calibri", 15)
continue_to_order_dunkin.place(x=390, y=430)

# image subway
subway_logo = ImageTk.PhotoImage(Image.open("/Users/samiradeepak/Desktop/subway_logo (1).png"))
subway_logo_label = tk.Label(frame3, image=subway_logo)
subway_logo_label["highlightbackground"] = "#310054"
subway_logo_label.place(x=50, y=500)

# subway
subway_label = tk.Label(frame3, text="Subway : ")
subway_label["fg"] = "#00f3b2"
subway_label["bg"] = "#310054"
subway_label["font"] = ("Calibri", 14)
subway_label.place(x=220, y=500)

# finish reservation button subway
finish_button_subway = tk.Button(frame3, text="Finish Reservation", command=lambda: show_frame(frame9))
finish_button_subway["fg"] = "#00f3b2"
finish_button_subway["highlightbackground"] = "#310054"
finish_button_subway["font"] = ("Calibri", 15)
finish_button_subway.place(x=220, y=530)

# continue to order button subway
continue_to_order_subway = tk.Button(frame3, text="Continue to order", command=lambda: show_frame(frame7))
continue_to_order_subway["fg"] = "#00f3b2"
continue_to_order_subway["highlightbackground"] = "#310054"
continue_to_order_subway["font"] = ("Calibri", 15)
continue_to_order_subway.place(x=390, y=530)

button_back_f2 = tk.Button(frame3, text="Back", command=lambda: show_frame(frame2))
button_back_f2.place(x=390, y=650)
button_back_f2["width"] = 20
button_back_f2["fg"] = "#00f3b2"
button_back_f2["highlightbackground"] = "#310054"

# ==================Frame 4 code(MENU OF RESTO - MCD)
root.geometry("600x500")
bg_label_f4 = tk.Label(frame4, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

global mcd_chosen_item_name
mcd_chosen_item_name = []
global mcd_chosen_item_qty
mcd_chosen_item_qty = []
global mcd_chosen_item_price
mcd_chosen_item_price = []


def mcd_get_order():
    show_frame(frame8)
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
    mcd_chosen_item_amt = []
    for (name, qty, price) in mcd_all_items:
        if qty > 0:
            mcd_chosen_item_name.append(name)
            mcd_chosen_item_qty.append(qty)
            mcd_chosen_item_price.append(price)
            mcd_chosen_item_amt.append(qty * price)
    print(f"{mcd_chosen_item_name}\n{mcd_chosen_item_qty}\n{mcd_chosen_item_price}\n{mcd_chosen_item_amt}")

    # Storing all the item names in a string
    name_str = ""
    for x in mcd_chosen_item_name:
        name_str += f"{x}\n"
    var_item_name.set(name_str)

    # Storing all the item quantities in a string
    qty_str = ""
    for x in mcd_chosen_item_qty:
        qty_str += f"{x}\n"
    var_item_quantity.set(qty_str)

    # Storing all the item amounts in a string
    amt_str = ""
    for x in mcd_chosen_item_amt:
        amt_str += f"{x}\n"
    var_item_amt.set(amt_str)

    # Finding and storing the total amount without GST
    amt_wo_gst = 0
    for x in mcd_chosen_item_amt:
        amt_wo_gst += x
    var_total_amt_wo_gst.set(f"Sub Total :\t{amt_wo_gst}")
    print(amt_wo_gst)

    # Calculating GST
    gst = ((6 / 100) * amt_wo_gst)
    var_gst_amt.set(f"GST :\t\t{gst:.2f}\t(6%)")

    # Finding Total Amount
    amt_w_gst = amt_wo_gst + gst
    var_total_amt_w_gst.set(f"Final Amount :\t{amt_w_gst:.2f}")


mcd_label = tk.Label(frame4, text="MENU - MCDONALDS")
mcd_label["fg"] = "#00f3b2"
mcd_label["bg"] = "#310054"
mcd_label["font"] = ("Calibri", 30, "underline")
mcd_label.place(x=350, y=20)

mcd_burgers = tk.Label(frame4, text="BURGERS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
mcd_burgers.place(x=20, y=80)

mcd_price_1 = tk.Label(frame4, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
mcd_price_1.place(x=280, y=80)

mcd_price_2 = tk.Label(frame4, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
mcd_price_2.place(x=800, y=80)

mcspicy_chicken = tk.Label(frame4, text="McSpicy Chicken", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcspicy_chicken.place(x=50, y=120)

price_mcspicy_chicken = Label(frame4, text="Rs.170", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcspicy_chicken.place(x=315, y=120)

qty_mcspicy_chicken = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcspicy_chicken.place(x=440, y=120)

var_mcspicy_chicken = IntVar(value=0)
sb_mcspicy_chicken = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcspicy_chicken)
sb_mcspicy_chicken.place(x=470, y=120)

mcspicy_paneer = tk.Label(frame4, text="McSpicy Paneer", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcspicy_paneer.place(x=50, y=160)

price_mcspicy_paneer = Label(frame4, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcspicy_paneer.place(x=315, y=160)

qty_mcspicy_paneer = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcspicy_paneer.place(x=440, y=160)

var_mcspicy_paneer = IntVar(value=0)
sb_mcspicy_paneer = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcspicy_paneer)
sb_mcspicy_paneer.place(x=470, y=160)

mcveggie = tk.Label(frame4, text="McVeggie", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcveggie.place(x=50, y=200)

price_mcveggie = Label(frame4, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcveggie.place(x=315, y=200)

qty_mcveggie = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcveggie.place(x=440, y=200)

var_mcveggie = IntVar(value=0)
sb_mcveggie = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcveggie)
sb_mcveggie.place(x=470, y=200)

mex_mcaloo = tk.Label(frame4, text="Mexican McAloo Tikki", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mex_mcaloo.place(x=50, y=240)

price_mex_mcaloo = Label(frame4, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mex_mcaloo.place(x=315, y=240)

qty_mex_mcaloo = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mex_mcaloo.place(x=440, y=240)

var_mex_mcaloo = IntVar(value=0)
sb_mex_mcaloo = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mex_mcaloo)
sb_mex_mcaloo.place(x=470, y=240)

mcaloo = tk.Label(frame4, text="McAloo Tikki", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcaloo.place(x=50, y=280)

price_mcaloo = Label(frame4, text="Rs.50", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcaloo.place(x=315, y=280)

qty_mcaloo = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcaloo.place(x=440, y=280)

var_mcaloo = IntVar(value=0)
sb_mcaloo = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcaloo)
sb_mcaloo.place(x=470, y=280)

chicken_kebab = tk.Label(frame4, text="Chicken Kebab Burger", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
chicken_kebab.place(x=50, y=320)

price_chicken_kebab = Label(frame4, text="Rs.180", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_chicken_kebab.place(x=315, y=320)

qty_chicken_kebab = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_chicken_kebab.place(x=440, y=320)

var_chicken_kebab = IntVar(value=0)
sb_chicken_kebab = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_chicken_kebab)
sb_chicken_kebab.place(x=470, y=320)

mcd_beverages = tk.Label(frame4, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
mcd_beverages.place(x=20, y=380)

thums_up = tk.Label(frame4, text="Thums Up", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
thums_up.place(x=50, y=420)

price_thums_up = Label(frame4, text="Rs.85", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_thums_up.place(x=315, y=420)

qty_thums_up = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_thums_up.place(x=440, y=420)

var_thums_up = IntVar(value=0)
sb_thums_up = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_thums_up)
sb_thums_up.place(x=470, y=420)

coke = tk.Label(frame4, text="Coke", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
coke.place(x=50, y=460)

price_coke = Label(frame4, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_coke.place(x=315, y=460)

qty_coke = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_coke.place(x=440, y=460)

var_coke = IntVar(value=0)
sb_coke = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_coke)
sb_coke.place(x=470, y=460)

iced_tea = tk.Label(frame4, text="Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
iced_tea.place(x=50, y=500)

price_iced_tea = Label(frame4, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_iced_tea.place(x=315, y=500)

qty_iced_tea = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_iced_tea.place(x=440, y=500)

var_iced_tea = IntVar(value=0)
sb_iced_tea = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_iced_tea)
sb_iced_tea.place(x=470, y=500)

mcd_fries_and_sides = tk.Label(frame4, text="FRIES & SIDES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
mcd_fries_and_sides.place(x=620, y=80)

reg_fries = tk.Label(frame4, text="Regular Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
reg_fries.place(x=650, y=120)

price_reg_fries = Label(frame4, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_reg_fries.place(x=850, y=120)

qty_reg_fries = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_reg_fries.place(x=960, y=120)

var_reg_fries = IntVar(value=0)
sb_reg_fries = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_reg_fries)
sb_reg_fries.place(x=990, y=120)

med_fries = tk.Label(frame4, text="Medium Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
med_fries.place(x=650, y=160)

price_med_fries = Label(frame4, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_med_fries.place(x=850, y=160)

qty_med_fries = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_med_fries.place(x=960, y=160)

var_med_fries = IntVar(value=0)
sb_med_fries = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_med_fries)
sb_med_fries.place(x=990, y=160)

large_fries = tk.Label(frame4, text="Large Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
large_fries.place(x=650, y=200)

price_large_fries = Label(frame4, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_large_fries.place(x=850, y=200)

qty_large_fries = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_large_fries.place(x=960, y=200)

var_large_fries = IntVar(value=0)
sb_large_fries = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_large_fries)
sb_large_fries.place(x=990, y=200)

masala_wedges = tk.Label(frame4, text="Masala Wedeges", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
masala_wedges.place(x=650, y=240)

price_masala_wedges = Label(frame4, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_masala_wedges.place(x=850, y=240)

qty_masala_wedges = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_masala_wedges.place(x=960, y=240)

var_masala_wedges = IntVar(value=0)
sb_masala_wedges = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_masala_wedges)
sb_masala_wedges.place(x=990, y=240)

chicken_strips = tk.Label(frame4, text="Chicken Strips", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
chicken_strips.place(x=650, y=280)

price_chicken_strips = Label(frame4, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_chicken_strips.place(x=850, y=280)

qty_chicken_strips = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_chicken_strips.place(x=960, y=280)

var_chicken_strips = IntVar(value=0)
sb_chicken_strips = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_chicken_strips)
sb_chicken_strips.place(x=990, y=280)

mcwings = tk.Label(frame4, text="McWings", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcwings.place(x=650, y=320)

price_mcwings = Label(frame4, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcwings.place(x=850, y=320)

qty_mcwings = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcwings.place(x=960, y=320)

var_mcwings = IntVar()
sb_mcwings = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcwings)
sb_mcwings.place(x=990, y=320)

mcd_desserts = tk.Label(frame4, text="DESSERTS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
mcd_desserts.place(x=620, y=380)

mcswirl = tk.Label(frame4, text="McSwirl", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcswirl.place(x=650, y=420)

price_mcswirl = Label(frame4, text="Rs.30", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcswirl.place(x=850, y=420)

qty_mcswirl = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcswirl.place(x=960, y=420)

var_mcswirl = IntVar(value=0)
sb_mcswirl = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcswirl)
sb_mcswirl.place(x=990, y=420)

mcflurry = tk.Label(frame4, text="McFlurry", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mcflurry.place(x=650, y=460)

price_mcflurry = Label(frame4, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mcflurry.place(x=850, y=460)

qty_mcflurry = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mcflurry.place(x=960, y=460)

var_mcflurry = IntVar(value=0)
sb_mcflurry = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_mcflurry)
sb_mcflurry.place(x=990, y=460)

soft_serve = tk.Label(frame4, text="Soft Serve", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
soft_serve.place(x=650, y=500)

price_soft_serve = Label(frame4, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_soft_serve.place(x=850, y=500)

qty_soft_serve = Label(frame4, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_soft_serve.place(x=960, y=500)

var_soft_serve = IntVar(value=0)
sb_soft_serve = Spinbox(frame4, from_=0, to=100, width=3, textvariable=var_soft_serve)
sb_soft_serve.place(x=990, y=500)

b_mcd_get_bill = tk.Button(frame4, text="Get Bill", command=mcd_get_order)
b_mcd_get_bill.place(x=1050, y=575)
b_mcd_get_bill["width"] = 20
b_mcd_get_bill["fg"] = "#310054"
b_mcd_get_bill["highlightbackground"] = "#00f3b2"

b_mcd_back = tk.Button(frame4, text="Back", command=lambda: show_frame(frame3))
b_mcd_back.place(x=850, y=575)
b_mcd_back["width"] = 20
b_mcd_back["fg"] = "#310054"
b_mcd_back["highlightbackground"] = "#00f3b2"

# ========================================================================================(menu - Kfc)FRAME 5
root.geometry("600x500")
bg_label_f4 = tk.Label(frame5, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

kfc_label = tk.Label(frame5, text="MENU - KFC")
kfc_label["fg"] = "#00f3b2"
kfc_label["bg"] = "#310054"
kfc_label["font"] = ("Calibri", 30, "underline")
kfc_label.place(x=350, y=20)

kfc_chicken = tk.Label(frame5, text="CHICKEN:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
kfc_chicken.place(x=20, y=80)

kfc_price_1 = tk.Label(frame5, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
kfc_price_1.place(x=280, y=80)

kfc_price_2 = tk.Label(frame5, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
kfc_price_2.place(x=800, y=80)

big_8 = tk.Label(frame5, text="Big 8", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
big_8.place(x=50, y=120)

price_big_8 = Label(frame5, text="Rs.620", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_big_8.place(x=315, y=120)

qty_big_8 = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_big_8.place(x=440, y=120)

sb_big_8 = Spinbox(frame5, from_=0, to=100, width=3)
sb_big_8.place(x=470, y=120)

big_12 = tk.Label(frame5, text="Big 12", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
big_12.place(x=50, y=160)

price_big_12 = Label(frame5, text="Rs.730", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_big_12.place(x=315, y=160)

qty_big_12 = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_big_12.place(x=440, y=160)

sb_big_12 = Spinbox(frame5, from_=0, to=100, width=3)
sb_big_12.place(x=470, y=160)

bucket_2 = tk.Label(frame5, text="Bucket for 2", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
bucket_2.place(x=50, y=200)

price_bucket_2 = Label(frame5, text="Rs.600", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_bucket_2.place(x=315, y=200)

qty_bucket_2 = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_bucket_2.place(x=440, y=200)

sb_bucket_2 = Spinbox(frame5, from_=0, to=100, width=3)
sb_bucket_2.place(x=470, y=200)

saving_bucket = tk.Label(frame5, text="Ultimate Savings Bucket", bg="#310054", fg="#00f3b2",
                         font=['Calibri', 15, 'bold'])
saving_bucket.place(x=50, y=240)

price_saving_bucket = Label(frame5, text="Rs.700", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_saving_bucket.place(x=315, y=240)

qty_saving_bucket = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_saving_bucket.place(x=440, y=240)

sb_saving_bucket = Spinbox(frame5, from_=0, to=100, width=3)
sb_saving_bucket.place(x=470, y=240)

kfc_beverages = tk.Label(frame5, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
kfc_beverages.place(x=20, y=300)

red_bull = tk.Label(frame5, text="Red Bull Energy Drink", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
red_bull.place(x=50, y=340)

price_red_bull = Label(frame5, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_red_bull.place(x=315, y=340)

qty_red_bull = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_red_bull.place(x=440, y=340)

sb_red_bull = Spinbox(frame5, from_=0, to=100, width=3)
sb_red_bull.place(x=470, y=340)

pepsi = tk.Label(frame5, text="Pepsi Can", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
pepsi.place(x=50, y=380)

price_pepsi = Label(frame5, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_pepsi.place(x=315, y=380)

qty_pepsi = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_pepsi.place(x=440, y=380)

sb_pepsi = Spinbox(frame5, from_=0, to=100, width=3)
sb_pepsi.place(x=470, y=380)

mirinda = tk.Label(frame5, text="Mirinda Can", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mirinda.place(x=50, y=420)

price_mirinda = Label(frame5, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mirinda.place(x=315, y=420)

qty_mirinda = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mirinda.place(x=440, y=420)

sb_mirinda = Spinbox(frame5, from_=0, to=100, width=3)
sb_mirinda.place(x=470, y=420)

kfc_burgers = tk.Label(frame5, text="BURGERS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
kfc_burgers.place(x=20, y=480)

veg_zinger = tk.Label(frame5, text="Veg Zinger Burger", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
veg_zinger.place(x=50, y=520)

price_veg_zinger = Label(frame5, text="Rs.160", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_veg_zinger.place(x=315, y=520)

qty_veg_zinger = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_veg_zinger.place(x=440, y=520)

sb_veg_zinger = Spinbox(frame5, from_=0, to=100, width=3)
sb_veg_zinger.place(x=470, y=520)

classic_zinger = tk.Label(frame5, text="Classic Zinger Burger", bg="#310054", fg="#00f3b2",
                          font=['Calibri', 15, 'bold'])
classic_zinger.place(x=50, y=560)

price_classic_zinger = Label(frame5, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_classic_zinger.place(x=315, y=560)

qty_classic_zinger = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_classic_zinger.place(x=440, y=560)

sb_classic_zinger = Spinbox(frame5, from_=0, to=100, width=3)
sb_classic_zinger.place(x=470, y=560)

tand_zinger = tk.Label(frame5, text="Tandoori Zinger Burger", bg="#310054", fg="#00f3b2",
                       font=['Calibri', 15, 'bold'])
tand_zinger.place(x=50, y=600)

price_tand_zinger = Label(frame5, text="Rs.200", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_tand_zinger.place(x=315, y=600)

qty_tand_zinger = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_tand_zinger.place(x=440, y=600)

sb_tand_zinger = Spinbox(frame5, from_=0, to=100, width=3)
sb_tand_zinger.place(x=470, y=600)

double_down = tk.Label(frame5, text="2 Double Down Burgers", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
double_down.place(x=50, y=640)

price_double_down = Label(frame5, text="Rs.500", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_double_down.place(x=315, y=640)

qty_double_down = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_double_down.place(x=440, y=640)

sb_double_down = Spinbox(frame5, from_=0, to=100, width=3)
sb_double_down.place(x=470, y=640)

kfc_snacks = tk.Label(frame5, text="SNACKS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
kfc_snacks.place(x=620, y=80)

veg_patty = tk.Label(frame5, text="2 pc Veg Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
veg_patty.place(x=650, y=120)

price_veg_patty = Label(frame5, text="Rs.140", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_veg_patty.place(x=850, y=120)

qty_veg_patty = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_veg_patty.place(x=960, y=120)

sb_veg_patty = Spinbox(frame5, from_=0, to=100, width=3)
sb_veg_patty.place(x=990, y=120)

kfc_m_fries = tk.Label(frame5, text="Medium Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
kfc_m_fries.place(x=650, y=160)

price_kfc_m_fries = Label(frame5, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_kfc_m_fries.place(x=850, y=160)

qty_kfc_m_fries = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_kfc_m_fries.place(x=960, y=160)

sb_kfc_m_fries = Spinbox(frame5, from_=0, to=100, width=3)
sb_kfc_m_fries.place(x=990, y=160)

kfc_l_fries = tk.Label(frame5, text="Large Fries", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
kfc_l_fries.place(x=650, y=200)

price_kfc_l_fries = Label(frame5, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_kfc_l_fries.place(x=850, y=200)

qty_kfc_l_fries = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_kfc_l_fries.place(x=960, y=200)

sb_kfc_l_fries = Spinbox(frame5, from_=0, to=100, width=3)
sb_kfc_l_fries.place(x=990, y=200)

sm_red_chicken = tk.Label(frame5, text="Smokey Red Chicken", bg="#310054", fg="#00f3b2",
                          font=['Calibri', 15, 'bold'])
sm_red_chicken.place(x=650, y=240)

price_sm_red_chicken = Label(frame5, text="Rs.220", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_sm_red_chicken.place(x=850, y=240)

qty_sm_red_chicken = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_sm_red_chicken.place(x=960, y=240)

sb_sm_red_chicken = Spinbox(frame5, from_=0, to=100, width=3)
sb_sm_red_chicken.place(x=990, y=240)

mingles = tk.Label(frame5, text="Mingles Bucket", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mingles.place(x=650, y=280)

price_mingles = Label(frame5, text="Rs.310", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mingles.place(x=850, y=280)

qty_mingles = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mingles.place(x=960, y=280)

sb_mingles = Spinbox(frame5, from_=0, to=100, width=3)
sb_mingles.place(x=990, y=280)

med_popcorn = tk.Label(frame5, text="Medium Popcorn", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
med_popcorn.place(x=650, y=320)

price_med_popcorn = Label(frame5, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_med_popcorn.place(x=850, y=320)

qty_med_popcorn = Label(frame5, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_med_popcorn.place(x=960, y=320)

sb_med_popcorn = Spinbox(frame5, from_=0, to=100, width=3)
sb_med_popcorn.place(x=990, y=320)

b_kfc_get_bill = tk.Button(frame5, text="Get Bill", command=lambda: show_frame(frame8))
b_kfc_get_bill.place(x=1050, y=575)
b_kfc_get_bill["width"] = 20
b_kfc_get_bill["fg"] = "#310054"
b_kfc_get_bill["highlightbackground"] = "#00f3b2"

b_kfc_back = tk.Button(frame5, text="Back", command=lambda: show_frame(frame3))
b_kfc_back.place(x=850, y=575)
b_kfc_back["width"] = 20
b_kfc_back["fg"] = "#310054"
b_kfc_back["highlightbackground"] = "#00f3b2"

# ========================================================================================(menu - dunkin)FRAME 6
root.geometry("600x500")
bg_label_f4 = tk.Label(frame6, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

dunkin_label = tk.Label(frame6, text="MENU - DUNKIN' DONUTS ")
dunkin_label["fg"] = "#00f3b2"
dunkin_label["bg"] = "#310054"
dunkin_label["font"] = ("Calibri", 30, "underline")
dunkin_label.place(x=350, y=20)

dunkin_donuts = tk.Label(frame6, text="DONUTS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
dunkin_donuts.place(x=20, y=80)

price_1 = tk.Label(frame6, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
price_1.place(x=280, y=80)

price_2 = tk.Label(frame6, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
price_2.place(x=800, y=80)

rainbow_pop = tk.Label(frame6, text="Rainbow Pop", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
rainbow_pop.place(x=50, y=120)

price_rainbow_pop = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_rainbow_pop.place(x=315, y=120)

qty_rainbow_pop = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_rainbow_pop.place(x=440, y=120)

sb_rainbow_pop = Spinbox(frame6, from_=0, to=100, width=3)
sb_rainbow_pop.place(x=470, y=120)

choco_pop = tk.Label(frame6, text="Choco Pop", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
choco_pop.place(x=50, y=160)

price_choco_pop = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_choco_pop.place(x=315, y=160)

qty_choco_pop = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_choco_pop.place(x=440, y=160)

sb_choco_pop = Spinbox(frame6, from_=0, to=100, width=3)
sb_choco_pop.place(x=470, y=160)

boston_creme = tk.Label(frame6, text="Boston Crème", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
boston_creme.place(x=50, y=200)

price_boston_creme = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_boston_creme.place(x=315, y=200)

qty_boston_creme = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_boston_creme.place(x=440, y=200)

sb_boston_creme = Spinbox(frame6, from_=0, to=100, width=3)
sb_boston_creme.place(x=470, y=200)

choco_overdose = tk.Label(frame6, text="Choco Overdose", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
choco_overdose.place(x=50, y=240)

price_choco_overdose = Label(frame6, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_choco_overdose.place(x=315, y=240)

qty_choco_overdose = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_choco_overdose.place(x=440, y=240)

sb_choco_overdose = Spinbox(frame6, from_=0, to=100, width=3)
sb_choco_overdose.place(x=470, y=240)

peanut_butter = tk.Label(frame6, text="Peanut Butter Island", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
peanut_butter.place(x=50, y=280)

price_peanut_butter = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_peanut_butter.place(x=315, y=280)

qty_peanut_butter = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_peanut_butter.place(x=440, y=280)

sb_peanut_butter = Spinbox(frame6, from_=0, to=100, width=3)
sb_peanut_butter.place(x=470, y=280)

white_choc_strawberry = tk.Label(frame6, text="White Choco & Strawberry", bg="#310054", fg="#00f3b2",
                                 font=['Calibri', 15, 'bold'])
white_choc_strawberry.place(x=50, y=320)

price_white_choc_strawberry = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_white_choc_strawberry.place(x=315, y=320)

qty_white_choc_strawberry = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_white_choc_strawberry.place(x=440, y=320)

sb_white_choc_strawberry = Spinbox(frame6, from_=0, to=100, width=3)
sb_white_choc_strawberry.place(x=470, y=320)

chocotella = tk.Label(frame6, text="Chocotella", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
chocotella.place(x=50, y=360)

price_chocotella = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_chocotella.place(x=315, y=360)

qty_chocotella = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_chocotella.place(x=440, y=360)

sb_chocotella = Spinbox(frame6, from_=0, to=100, width=3)
sb_chocotella.place(x=470, y=360)

choco_berry = tk.Label(frame6, text="Choco Berry Bomb", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
choco_berry.place(x=50, y=400)

price_choco_berry = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_choco_berry.place(x=315, y=400)

qty_choco_berry = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_choco_berry.place(x=440, y=400)

sb_choco_berry = Spinbox(frame6, from_=0, to=100, width=3)
sb_choco_berry.place(x=470, y=400)

dunkin_beverages = tk.Label(frame6, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
dunkin_beverages.place(x=20, y=460)

caramel_dunk = tk.Label(frame6, text="Caramel Dunkaccino", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
caramel_dunk.place(x=50, y=500)

price_caramel_dunk = Label(frame6, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_caramel_dunk.place(x=315, y=500)

qty_caramel_dunk = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_caramel_dunk.place(x=440, y=500)

sb_caramel_dunk = Spinbox(frame6, from_=0, to=100, width=3)
sb_caramel_dunk.place(x=470, y=500)

virgin_mojito = tk.Label(frame6, text="Virgin Mojito", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
virgin_mojito.place(x=50, y=540)

price_virgin_mojito = Label(frame6, text="Rs.120", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_virgin_mojito.place(x=315, y=540)

qty_virgin_mojito = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_virgin_mojito.place(x=440, y=540)

sb_virgin_mojito = Spinbox(frame6, from_=0, to=100, width=3)
sb_virgin_mojito.place(x=470, y=540)

fruit_berry = tk.Label(frame6, text="Fruit Berry", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
fruit_berry.place(x=50, y=580)

price_fruit_berry = Label(frame6, text="Rs.210", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_fruit_berry.place(x=315, y=580)

qty_fruit_berry = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_fruit_berry.place(x=440, y=580)

sb_fruit_berry = Spinbox(frame6, from_=0, to=100, width=3)
sb_fruit_berry.place(x=470, y=580)

caramel_ice_coffee = tk.Label(frame6, text="Caramel Iced Coffee", bg="#310054", fg="#00f3b2",
                              font=['Calibri', 15, 'bold'])
caramel_ice_coffee.place(x=50, y=620)

price_caramel_ice_coffee = Label(frame6, text="Rs.190", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_caramel_ice_coffee.place(x=315, y=620)

qty_caramel_ice_coffee = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_caramel_ice_coffee.place(x=440, y=620)

sb_caramel_ice_coffee = Spinbox(frame6, from_=0, to=100, width=3)
sb_caramel_ice_coffee.place(x=470, y=620)

peach_ice_tea = tk.Label(frame6, text="Peach Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
peach_ice_tea.place(x=50, y=660)

price_peach_ice_tea = Label(frame6, text="Rs.170", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_peach_ice_tea.place(x=315, y=660)

qty_peach_ice_tea = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_peach_ice_tea.place(x=440, y=660)

sb_peach_ice_tea = Spinbox(frame6, from_=0, to=100, width=3)
sb_peach_ice_tea.place(x=470, y=660)

dunkin_sides = tk.Label(frame6, text="SIDES & EXTRAS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
dunkin_sides.place(x=620, y=80)

dunkin_wedges = tk.Label(frame6, text="Potato Wedges", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
dunkin_wedges.place(x=630, y=130)

price_dunkin_wedges = Label(frame6, text="Rs.80", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_dunkin_wedges.place(x=850, y=130)

qty_dunkin_wedges = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_dunkin_wedges.place(x=960, y=130)

sb_dunkin_wedges = Spinbox(frame6, from_=0, to=100, width=3)
sb_dunkin_wedges.place(x=990, y=130)

veg_nachos = tk.Label(frame6, text="Veg Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
veg_nachos.place(x=630, y=170)

price_veg_nachos = Label(frame6, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_veg_nachos.place(x=850, y=170)

qty_veg_nachos = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_veg_nachos.place(x=960, y=170)

sb_veg_nachos = Spinbox(frame6, from_=0, to=100, width=3)
sb_veg_nachos.place(x=990, y=170)

chicken_nachos = tk.Label(frame6, text="Chicken Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
chicken_nachos.place(x=630, y=210)

price_chicken_nachos = Label(frame6, text="Rs.110", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_chicken_nachos.place(x=850, y=210)

qty_chicken_nachos = Label(frame6, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_chicken_nachos.place(x=960, y=210)

sb_chicken_nachos = Spinbox(frame6, from_=0, to=100, width=3)
sb_chicken_nachos.place(x=990, y=210)

b_dunkin_get_bill = tk.Button(frame6, text="Get Bill", command=lambda: show_frame(frame8))
b_dunkin_get_bill.place(x=1050, y=575)
b_dunkin_get_bill["width"] = 20
b_dunkin_get_bill["fg"] = "#310054"
b_dunkin_get_bill["highlightbackground"] = "#00f3b2"

b_dunkin_back = tk.Button(frame6, text="Back", command=lambda: show_frame(frame3))
b_dunkin_back.place(x=850, y=575)
b_dunkin_back["width"] = 20
b_dunkin_back["fg"] = "#310054"
b_dunkin_back["highlightbackground"] = "#00f3b2"

# ========================================================================================(menu - subway)FRAME 7
root.geometry("600x500")
bg_label_f4 = tk.Label(frame7, bg="#310054")
bg_label_f4.pack(fill='both', expand=True)

subway_label = tk.Label(frame7, text="MENU - SUBWAY ")
subway_label["fg"] = "#00f3b2"
subway_label["bg"] = "#310054"
subway_label["font"] = ("Calibri", 30, "underline")
subway_label.place(x=150, y=20)

subway_wraps = tk.Label(frame7, text="SIGNATURE WRAPS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
subway_wraps.place(x=20, y=80)

subway_price_1 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
subway_price_1.place(x=280, y=80)

subway_price_2 = tk.Label(frame7, text="PRICE (in Rs.):", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
subway_price_2.place(x=800, y=80)

chicken_teriyaki = tk.Label(frame7, text="Chicken Teriyaki", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
chicken_teriyaki.place(x=50, y=160)

price_chicken_teriyaki = Label(frame7, text="Rs.260", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_chicken_teriyaki.place(x=315, y=160)

qty_chicken_teriyaki = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_chicken_teriyaki.place(x=440, y=160)

sb_chicken_teriyaki = Spinbox(frame7, from_=0, to=100, width=3)
sb_chicken_teriyaki.place(x=470, y=160)

corn_peas = tk.Label(frame7, text="Corn and Peas", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
corn_peas.place(x=50, y=200)

price_corn_peas = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_corn_peas.place(x=315, y=200)

qty_corn_peas = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_corn_peas.place(x=440, y=200)

sb_corn_peas = Spinbox(frame7, from_=0, to=100, width=3)
sb_corn_peas.place(x=470, y=200)

peri_peri_chicken = tk.Label(frame7, text="Peri Peri Chicken", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
peri_peri_chicken.place(x=50, y=240)

price_peri_peri_chicken = Label(frame7, text="Rs.250", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_peri_peri_chicken.place(x=315, y=240)

qty_peri_peri_chicken = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_peri_peri_chicken.place(x=440, y=240)

sb_peri_peri_chicken = Spinbox(frame7, from_=0, to=100, width=3)
sb_peri_peri_chicken.place(x=470, y=240)

mex_patty = tk.Label(frame7, text="Mexican Patty", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mex_patty.place(x=50, y=280)

price_mex_patty = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mex_patty.place(x=315, y=280)

qty_mex_patty = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mex_patty.place(x=440, y=280)

sb_mex_patty = Spinbox(frame7, from_=0, to=100, width=3)
sb_mex_patty.place(x=470, y=280)

sub_paneer_tikka = tk.Label(frame7, text="Paneer Tikka", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
sub_paneer_tikka.place(x=50, y=320)

price_sub_paneer_tikka = Label(frame7, text="Rs.230", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_sub_paneer_tikka.place(x=315, y=320)

qty_sub_paneer_tikka = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_sub_paneer_tikka.place(x=440, y=320)

sb_sub_paneer_tikka = Spinbox(frame7, from_=0, to=100, width=3)
sb_sub_paneer_tikka.place(x=470, y=320)

subway_beverages = tk.Label(frame7, text="BEVERAGES:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
subway_beverages.place(x=20, y=380)

mountain_dew = tk.Label(frame7, text="Mountain Dew", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
mountain_dew.place(x=50, y=420)

price_mountain_dew = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_mountain_dew.place(x=315, y=420)

qty_mountain_dew = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_mountain_dew.place(x=440, y=420)

sb7_mountain_dew = Spinbox(frame7, from_=0, to=100, width=3)
sb7_mountain_dew.place(x=470, y=420)

orange_juice = tk.Label(frame7, text="Orange Juice", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
orange_juice.place(x=50, y=460)

price_orange_juice = Label(frame7, text="Rs.70", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_orange_juice.place(x=315, y=460)

qty_orange_juice = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_orange_juice.place(x=440, y=460)

sb_orange_juice = Spinbox(frame7, from_=0, to=100, width=3)
sb_orange_juice.place(x=470, y=460)

subway_iced_tea = tk.Label(frame7, text="Iced Tea", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
subway_iced_tea.place(x=50, y=500)

price_subway_iced_tea = Label(frame7, text="Rs.50", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_subway_iced_tea.place(x=315, y=500)

qty_subway_iced_tea = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_subway_iced_tea.place(x=440, y=500)

sb_subway_iced_tea = Spinbox(frame7, from_=0, to=100, width=3)
sb_subway_iced_tea.place(x=470, y=500)

subway_desserts = tk.Label(frame7, text="DESSERTS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
subway_desserts.place(x=20, y=560)

choc_truffle = tk.Label(frame7, text="Rich Chocolate Truffle", bg="#310054", fg="#00f3b2",
                        font=['Calibri', 15, 'bold'])
choc_truffle.place(x=50, y=600)

price_choc_truffle = Label(frame7, text="Rs.60", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_choc_truffle.place(x=315, y=600)

qty_choc_truffle = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_choc_truffle.place(x=440, y=600)

sb_choc_truffle = Spinbox(frame7, from_=0, to=100, width=3)
sb_choc_truffle.place(x=470, y=600)

choc_cookie = tk.Label(frame7, text="Chocolate Cookie", bg="#310054", fg="#00f3b2",
                       font=['Calibri', 15, 'bold'])
choc_cookie.place(x=50, y=640)

price_choc_cookie = Label(frame7, text="Rs.30", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_choc_cookie.place(x=315, y=640)

qty_choc_cookie = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_choc_cookie.place(x=440, y=640)

sb_choc_cookie = Spinbox(frame7, from_=0, to=100, width=3)
sb_choc_cookie.place(x=470, y=640)

subway_sides = tk.Label(frame7, text="SIDES & EXTRAS:", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
subway_sides.place(x=620, y=80)

lays_classic = tk.Label(frame7, text="Lays Chips (Classic)", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
lays_classic.place(x=650, y=120)

price_lays_classic = Label(frame7, text="Rs.25", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_lays_classic.place(x=850, y=120)

qty_lays_classic = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_lays_classic.place(x=960, y=120)

sb_lays_classic = Spinbox(frame7, from_=0, to=100, width=3)
sb_lays_classic.place(x=990, y=120)

nachos = tk.Label(frame7, text="Nachos", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
nachos.place(x=650, y=160)

price_nachos = Label(frame7, text="Rs.100", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_nachos.place(x=850, y=160)

qty_nachos = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_nachos.place(x=960, y=160)

sb_nachos = Spinbox(frame7, from_=0, to=100, width=3)
sb_nachos.place(x=990, y=160)

hashbrown = tk.Label(frame7, text="Hash Browns", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
hashbrown.place(x=650, y=200)

price_hashbrown = Label(frame7, text="Rs.90", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_hashbrown.place(x=850, y=200)

qty_hashbrown = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_hashbrown.place(x=960, y=200)

sb_hashbrown = Spinbox(frame7, from_=0, to=100, width=3)
sb_hashbrown.place(x=990, y=200)

chorizo = tk.Label(frame7, text="Chorizo Flatbread Pizza", bg="#310054", fg="#00f3b2",
                   font=['Calibri', 15, 'bold'])
chorizo.place(x=600, y=240)

price_chorizo = Label(frame7, text="Rs.150", bg="#310054", fg="#00f3b2", font=['Calibri', 15, 'bold'])
price_chorizo.place(x=850, y=240)

qty_chorizo = Label(frame7, text="Qty", bg="#310054", fg="#00f3b2", font=['Calibri', 11, 'bold'])
qty_chorizo.place(x=960, y=240)

sb_chorizo = Spinbox(frame7, from_=0, to=100, width=3)
sb_chorizo.place(x=990, y=240)

b_subway_get_bill = tk.Button(frame7, text="Get Bill", command=lambda: show_frame(frame8))
b_subway_get_bill.place(x=1050, y=575)
b_subway_get_bill["width"] = 20
b_subway_get_bill["fg"] = "#310054"
b_subway_get_bill["highlightbackground"] = "#00f3b2"

b_subway_back = tk.Button(frame7, text="Back", command=lambda: show_frame(frame3))
b_subway_back.place(x=850, y=575)
b_subway_back["width"] = 20
b_subway_back["fg"] = "#310054"
b_subway_back["highlightbackground"] = "#00f3b2"

# ==================(BILL)
bg_label_f8 = Label(frame8, bg="#310054")
bg_label_f8.pack(fill='both', expand=True)

# Bill Frame Heading Label
bill_label = tk.Label(frame8, text="BILL")
bill_label["fg"] = "#00f3b2"
bill_label["bg"] = "#310054"
bill_label["font"] = ("Calibri", 30, "underline")
bill_label.place(x=250, y=40)

# Items Column Header
l_items = Label(frame8, text="Items", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
l_items.place(x=100, y=100)

# Quantity Column Header
l_qty = Label(frame8, text="Quantity", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
l_qty.place(x=300, y=100)

# Amount Column Header
l_amt = Label(frame8, text="Amount", bg="#310054", fg="#00f3b2", font=['Calibri', 17, 'bold'])
l_amt.place(x=500, y=100)

# Label to Display item names
var_item_name = StringVar()
l_bill_name = Label(frame8, anchor="w", textvariable=var_item_name, bg="#310054", fg="#00f3b2",
                    font=['Calibri', 14, 'bold'])
l_bill_name.place(x=75, y=150)

# Label to Display item quantity
var_item_quantity = StringVar()
l_bill_qty = Label(frame8, anchor="w", textvariable=var_item_quantity, bg="#310054", fg="#00f3b2",
                   font=['Calibri', 14, "bold"])
l_bill_qty.place(x=320, y=150)

# Label to Display item amount
var_item_amt = StringVar()
l_bill_amt = Label(frame8, anchor="w", textvariable=var_item_amt, bg="#310054", fg="#00f3b2",
                   font=['Calibri', 14, 'bold'])
l_bill_amt.place(x=520, y=150)

# Label to Display Total Amount without GST
var_total_amt_wo_gst = StringVar()
l_amt_wo_gst = Label(frame8, anchor="w", textvariable=var_total_amt_wo_gst, bg="#310054", fg="#00f3b2",
                     font=['Calibri', 14, 'bold'])
l_amt_wo_gst.place(x=100, y=510)

# Label to show GST Amount
var_gst_amt = StringVar()
l_gst_amt = Label(frame8, anchor="w", textvariable=var_gst_amt, bg="#310054", fg="#00f3b2",
                  font=['Calibri', 14, 'bold'])
l_gst_amt.place(x=100, y=540)

# Label to show Total Amount with GST
var_total_amt_w_gst = StringVar()
l_amt_w_gst = Label(frame8, anchor="w", textvariable=var_total_amt_w_gst, bg="#310054", fg="#00f3b2",
                    font=['Calibri', 14, 'bold'])
l_amt_w_gst.place(x=100, y=570)

# Next Window Button
var_item_qty = StringVar()
res_details = tk.Button(frame8, text="Show Reservation Details", command=lambda: show_frame(frame9))
res_details.place(x=850, y=625)
res_details["width"] = 30
res_details["fg"] = "#310054"
res_details["highlightbackground"] = "#00f3b2"

# Previous Window Button
bill_back = tk.Button(frame8, text="Back", command=lambda: show_frame(frame3))
bill_back.place(x=650, y=625)
bill_back["width"] = 20
bill_back["fg"] = "#310054"
bill_back["highlightbackground"] = "#00f3b2"

# ==================(RESERVATION CONFIRMATION)

bg_label_f9 = Label(frame9, bg="#310054")
bg_label_f9.pack(fill='both', expand=True)

confirm_label = tk.Label(frame, text="RESERVATION CONFIRMATION")
confirm_label["fg"] = "#00f3b2"
confirm_label["bg"] = "#310054"
confirm_label["font"] = ("Calibri", 30, "underline")
confirm_label.place(x=100, y=40)

show_frame(frame1)

root.mainloop()
