from tkinter import*
root = Tk()

#window title
root.title("Registration Form")
root.geometry("600x500")
#root["bg"] = "#e3e3e3"

#Registration Form Label
registration_form_label = tk.Label(root)
registration_form_label.place(x=180,y=60)
#dictionary attributes for label
registration_form_label["text"] = "Registration Form"
registration_form_label["font"] = ("Calibri", 30)


#Fullname Label
fullname_label = tk.Label(root, text="FULL NAME :")
fullname_label.place(x=70,y=130)
#textbox - Entry text
fullname_entrytext = tk.Entry(root)
fullname_entrytext.place(x=240,y=130)


#time(breakfast,lunch,dinner)
time_slot = tk.Label(root,text = "TIME SLOT :")
time_slot.place(x = 70 , y = 210)
#creating optionmenu for time slots
list_of_slots = ["Breakfast : 8:00 a.m. - 11:00 a.m.","Lunch : 1:00 p.m. - 3:00 p.m.","Dinner : 8:00 p.m. - 11:00 p.m."]
temp1 = StringVar()
slot_optionmenu = tk.OptionMenu(root, temp1, *list_of_slots)
slot_optionmenu.place(x=240, y=210)
temp1.set("Select your time slot")


#location label
user_location = tk.Label(root,text = "LOCATION :")
user_location.place(x=70,y=280)
#creatting optionmenu for locations
list_of_states = ["Mumbai","Delhi","Bangalore","Kolkata"]
temp = StringVar()
state_optionmenu = tk.OptionMenu(root, temp, *list_of_states)
state_optionmenu.place(x=240, y=280)
temp.set("Select your state")


#number of people
num_ppl = tk.Label(root,text = "NUMBER OF PEOPLE :")
num_ppl.place(x = 70 ,y = 340)
num_spin = tk.Spinbox(root, from_=1, to=15, width=8)
num_spin.place(x = 240 ,y = 340)


#Submit Button
button_submit = tk.Button(root, text="Submit",command=lambda: show_frame(frame2))
button_submit.place(x=180,y=380)
button_submit["width"] = 20
button_submit["fg"] = "white"
button_submit["highlightbackground"] = "#761515"


















root.mainloop()