# IMPORT STATEMENTS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
from math import *
from operator import *

# MAIN WINDOW TKINTER --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

mainwindow = Tk()
mainwindow.title("Wallpaper Quoting System")
mainwindow.geometry("1920x1080")

# VARIABLES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

current_style = StringVar()
style_label_text = StringVar()
style_label_text.set("Please Select Style")

current_colour = StringVar()
colour_label_text = StringVar()
colour_label_text.set("Please Select Colour")

current_finish = StringVar()
finish_label_text = StringVar()
finish_label_text.set("Please Select Finish")

current_size = StringVar()
current_size.set("0")
size_label_text = StringVar()
size_label_text.set("Size: 0 Meters Squared")

current_price = StringVar()
price_label_text = StringVar()
price_label_text.set("Price: £0.00")

current_lining = StringVar()
lining_label_text = StringVar()
lining_label_text.set("Please Select Lining Y/N")

current_paste = StringVar()
paste_label_text = StringVar()
paste_label_text.set("Please Select Paste Y/N")

Rolls_Required = StringVar()
Rolls_Required_label_text = StringVar()
Rolls_Required_label_text.set("Rolls Required: 0")

Lining_Required = StringVar()
Lining_Required_label_text = StringVar()
Lining_Required_label_text.set("Lining Required")

Paste_Required = StringVar()
Paste_Required_label_text = StringVar()
Paste_Required_label_text.set("Paste Required")

Total_Price = 0

# List for use in the canvas widget later
addsub = [add, sub] 

# List to store orders
orders = [] 

receipt_number = 0

# FUNCTIONS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Updates the style variable and the canvas widget
def style_updater(style, design1, design2):
    current_style.set(style)
    if style == "Style 1":
        design1.tk.call('raise', design1)
    elif style == "Style 2":
        design2.tk.call('raise', design2)
    elif style == "None":
        design_none.tk.call('raise', design_none)
    price_updater(current_size, current_finish, current_style, current_lining, current_paste)
    style_label_text.set("Style: " + style)

# Updates the colour variable and the canvas widget
def colour_updater(colour):
    current_colour.set(colour)
    if current_style.get() == "Style 1":
        design1.itemconfig("design1", fill = colour)
    elif current_style.get() == "Style 2":
        design2.itemconfig("design2", fill = colour)
    colour_label_text.set("Colour: " + colour)

# Updates the finish variable and the price
def finish_updater(finish):
    current_finish.set(finish)
    price_updater(current_size, current_finish, current_style, current_lining, current_paste)
    finish_label_text.set("Finish: " + finish)

# Updates the size variable and the price, as long as the input is a number
def size_updater(size):
    try:
        current_size.set(size)
        Rolls_Required.set(ceil(float(size) / 5.226))
        price_updater(current_size, current_finish, current_style, current_lining, current_paste)
        size_label_text.set("Size: " + size + " Meters Squared")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Updates the lining variable and the price
def lining_updater(lining):
    current_lining.set(lining)
    Lining_Required = ceil(float(float(current_size.get()) / 10.4))
    price_updater(current_size, current_finish, current_style, current_lining, current_paste)
    if lining == "Y":
        lining_label_text.set("Lining: " + str(Lining_Required) + " Rolls")
    else:
        lining_label_text.set("Lining: No")

# Updates the paste variable and the price
def paste_updater(paste):
    current_paste.set(paste)
    Paste_Required = ceil(float(float(current_size.get()) / 53))
    price_updater(current_size, current_finish, current_style, current_lining, current_paste)
    if paste == "Y":
        paste_label_text.set("Paste: " + str(Paste_Required) + " Tubs")
    else:
        paste_label_text.set("Paste: No")

# Updates the price, rolls required, lining required and paste required
def price_updater(current_size, current_finish, current_style, current_lining, current_paste):

    Rolls_Required = ceil(float(float(current_size.get())) / 5.226)
    Rolls_Required_label_text.set("Rolls Required: " + str(Rolls_Required))
    Lining_Required = ceil(float(float(current_size.get()) / 10.4))
    Paste_Required = ceil(float(float(current_size.get()) / 53))

    Style_Multiplier = 0
    Finish_Multiplier = 0
    Lining_Multiplier = 0
    Paste_Multiplier = 0

    if current_style.get() == "Style 1":
        Style_Multiplier = 15678
    elif current_style.get() == "Style 2":
        Style_Multiplier = 31356
    else:
        Style_Multiplier = 0

    if current_finish.get() == "Foil":
        Finish_Multiplier = 120.6
    elif current_finish.get() == "Glitter":
        Finish_Multiplier = 180.9
    elif current_finish.get() == "Embossing":
        Finish_Multiplier = 60.3
    else:
        Finish_Multiplier = 0

    if current_lining.get() == "Y":
        Lining_Multiplier = 763
    else:
        Lining_Multiplier = 0

    if current_paste.get() == "Y":
        Paste_Multiplier = 1399
    else:
        Paste_Multiplier = 0

    Price = float(((Rolls_Required*(Finish_Multiplier + Style_Multiplier)) + (Lining_Required * Lining_Multiplier) + (Paste_Required * Paste_Multiplier)) / 100)
    Rounded_Price = round(Price, 2)
    current_price.set(Rounded_Price)
    price_label_text.set("£" + str(Rounded_Price))

# Adds the current item with its customization to the orders list, once all options have been selected
def addtoorder():

    if style_label_text.get() == "Please Select Style":
        messagebox.showerror("Error", "Please select a style.")
    elif colour_label_text.get() == "Please Select Colour":
        messagebox.showerror("Error", "Please select a colour.")
    elif finish_label_text.get() == "Please Select Finish":
        messagebox.showerror("Error", "Please select a finish.")
    elif lining_label_text.get() == "Please Select Lining Y/N":
        messagebox.showerror("Error", "Please select whether you require lining.")
    elif paste_label_text.get() == "Please Select Paste Y/N":
        messagebox.showerror("Error", "Please select whether you require paste.")
    elif size_label_text.get() == "Size: 0 Meters Squared":
        messagebox.showerror("Error", "Please enter required amount.")
    else:
        global Total_Price

        order_list = []

        order_list.append(style_label_text.get())
        order_list.append(colour_label_text.get())
        order_list.append(finish_label_text.get())
        order_list.append(Rolls_Required_label_text.get())
        order_list.append(lining_label_text.get())
        order_list.append(paste_label_text.get())
        order_list.append(price_label_text.get())

        orders.append(order_list)

        Total_Price += float(current_price.get())

# Prints the current order list to a file, with a price total
def print_to_file():
    print("Printing to file")

    global receipt_number
    
    receipt_number += 1

    with open(f"receipt_{receipt_number}.txt", "w") as file:
        file.write("Total Price: £" + str(round((Total_Price) , 2))+ "\n\n")
        for order in orders:
            file.write(str(order) + "\n")
    
# Opens a new window with the current order list, and a price total
def vieworders():

    orders_window = Toplevel(mainwindow)
    orders_window.title("Orders")
    orders_window.geometry("1280x720")

    total_price_label = Label(orders_window, text = "Total Price: £" + str(round((Total_Price) , 2)))

    total_price_label.place(x = 10, y = 10)
    total_price_label.pack(fill = X, pady = 30)
    total_price_label.config(font = ("Arial", 30))

    listbox = Listbox(orders_window)

    for item in orders:
        listbox.insert(END, item)

    listbox.place(x = 0, y = 0)
    listbox.pack(expand = True, fill = BOTH)
    listbox.config(font = ("Arial", 12), justify = CENTER)

# Clears the current order list and resets the price total
def clearorders():
    global Total_Price
    orders.clear()
    Total_Price = 0

# Clears the entry box when clicked on
def clear_entry(event):
    size_req.delete(0, END)

# GUI  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rolls Required 

Rolls_Required_label = Label(mainwindow, textvariable = Rolls_Required_label_text, font = ("Arial", 12), highlightthickness = 3, borderwidth = 2, relief = "raised")
Rolls_Required_label.grid(row = 0, column = 2, padx = 10, pady = 10)

# Options Selection Size

size_req = Entry(mainwindow, width = 42)
size_req.grid(row = 5, column = 1, padx = 10)
size_req.insert(0, "Please enter required amount in meters squared")
size_req.bind("<FocusIn>", clear_entry)

button_sizeconfirm = Button(mainwindow, text="Confirm Size", command = lambda: size_updater(size_req.get()))
button_sizeconfirm.grid(row = 8, column = 1, padx = 10, pady = 10)

meteres_squared_label = Label(mainwindow, textvariable = size_label_text, font = ("Arial", 12), highlightthickness = 3, borderwidth = 2, relief = "raised")
meteres_squared_label.grid(row = 9, column = 1, padx = 10, pady = (0,30))

# Options Selection Style

options = ["Style 1", "Style 2"]

style_option_menu = OptionMenu(mainwindow, style_label_text, *options, command = lambda x: style_updater(x, design1, design2))
style_option_menu.grid(row = 10, column = 1, padx = 10, pady = 10)
style_option_menu.config(font = ("Arial", 12))

# Options Selection Colour

options = ["Purple", "Dark Slate Grey", "Deep Sky Blue", "Light Sea Green", "Violet Red", "Gold"]

colour_option_menu = OptionMenu(mainwindow, colour_label_text, *options, command = lambda x: colour_updater(x))
colour_option_menu.grid(row = 11, column = 1, padx = 10, pady = 10)
colour_option_menu.config(font = ("Arial", 12))

# Options Selection Finish

options = ["Foil", "Glitter", "Embossing", "None"]

finish_option_menu = OptionMenu(mainwindow, finish_label_text, *options, command = lambda x: finish_updater(x))
finish_option_menu.grid(row = 12, column = 1, padx = 10, pady = 10)
finish_option_menu.config(font = ("Arial", 12))

# Options Selection Lining

options = ["Y", "N"]

lining_option_menu = OptionMenu(mainwindow, lining_label_text, *options, command = lambda x: lining_updater(x))
lining_option_menu.grid(row = 13, column = 1, padx = 10, pady = 10)
lining_option_menu.config(font = ("Arial", 12))

# Options Selection Paste

options = ["Y", "N"]

paste_option_menu = OptionMenu(mainwindow, paste_label_text, *options, command = lambda x: paste_updater(x))
paste_option_menu.config(font = ("Arial", 12))
paste_option_menu.grid(row = 14, column = 1, padx = 10, pady = 10)

# Price

price_label = Label(mainwindow, textvariable = price_label_text, font = ("Arial", 30))
price_label.grid(row = 0, column = 7, padx = 10, pady = 10)

# Current Style Canvas

design1 = Canvas(mainwindow, width = 200, height = 200)
design1.grid(row = 0, column = 1, padx = 10, pady = (10,30), rowspan = 5)   

for i in range(0, 9, 4):
    for op in addsub:
        design1.create_polygon((op(10,(i+2))),20 , 10,(16-(2*i)) , 10,(20-(i*2)) , (op(10,i)),20, tags = "design1")

design2 = Canvas(mainwindow, width = 200, height = 200)
design2.grid(row = 0, column = 1, padx = 10, pady = (10,30), rowspan = 5)

for i in range(0, 9, 4):
    for y in range (0, 21, 20):
        for op in addsub:
            design2.create_polygon(10,10 , y,(op(10,i)) , y,(op(10,(i+2))), tags = "design2")
            design2.create_polygon(10,10 , (op(10,i)),y , (op(10,(i+2))),y, tags = "design2")

design_none = Canvas(mainwindow, width = 200, height = 200)
design_none.grid(row = 0, column = 1, padx = 10, pady = (10,30), rowspan = 5)

design_none.create_rectangle(0,0 , 20,20)

design1.scale("all", 0,0 , 10,10)
design2.scale("all", 0,0 , 10,10)
design_none.scale("all", 0,0 , 10,10)

# Order Management

Orderlistbox = Listbox(mainwindow)

button_addtoorder = Button(mainwindow, text="Add to Order", command = addtoorder)
button_addtoorder.grid(row = 1, column = 7, padx = 10, pady = 10)

button_vieworders = Button(mainwindow, text="View Order", command = vieworders)
button_vieworders.grid(row = 2, column = 7, padx = 10, pady = 10)

button_clearorders = Button(mainwindow, text="Clear Order", command = clearorders)
button_clearorders.grid(row = 3, column = 7, padx = 10, pady = 10)

button_print = Button(mainwindow, text = "Print to File", command = print_to_file)
button_print.grid(row = 4, column = 7, padx = 10, pady = 10)

# Mainloop

mainwindow.mainloop()