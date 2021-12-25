# Author: Andrea Arias

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from os import path
from pyglet import font

# Problem 1
houses = [None] * 8
inputs = []
outputs = []

# Validation problem 1


def validation():
    input_error.config(text="")
    days_error.config(text="")
    error = False
    for index in range(len(houses)):
        if inputs[index].get() == "" or days_input.get() == "":
            return
    for index in range(len(houses)):
        if inputs[index].get() != "1" and inputs[index].get() != "0":
            input_error.config(text="Solamente se aceptan unos y ceros.")
            error = True
    try:
        days = int(days_input.get())
        if(days < 0):
            days_error.config(
                text="Solamente se aceptan números mayores que cero.")
            error = True
    except:
        error = True
        days_error.config(text="Solamente se aceptan números.")
    if error == True:
        return
    for index in range(len(houses)):
        houses[index] = int(inputs[index].get())
    problem_1(houses, days)
# End validation problem 1


def problem_1(houses, days):
    for day in range(days):  # Go through days
        previous_value = 0  # Initialize previous value

        for house in range(len(houses)):
            house_left = previous_value

            if house == len(houses) - 1:
                house_right = 0
            else:
                house_right = houses[house + 1]

            previous_value = houses[house]

            if house_left == house_right:
                houses[house] = 0
            else:
                houses[house] = 1

    for house in range(len(houses)):
        outputs[house]["text"] = houses[house]
# End Problem 1

# Problem 2


def factorial(number):
    if int(number) > 1:
        return number * factorial(number - 1)
    else:
        return 1


def permutation(string, permutations, index):
    if index + 1 == len(string):
        permutations.append(string)
    else:
        swap(string, permutations, index)


def swap(string, permutations, index):
    for char in range(index, len(string)):
        new_string = string[char] + string[0:char] + \
            string[char + 1:len(string)]
        permutation(new_string, permutations, index + 1)


def permute_this():
    string = string_input.get()
    permutations = []
    permutation(string, permutations, 0)
    text = permutations[0]
    for index in range(1, len(permutations)):
        text = text + " " + permutations[index]
    permutation_output.configure(state='normal')
    permutation_output.delete('1.0', END)
    permutation_output.insert(INSERT, text)
    permutation_output.configure(state='disabled')
    permutation_label['text'] = "Permutaciones: " + str(factorial(len(string)))
# End Problem 2


# Window
directory = path.dirname(__file__)
font.add_file(directory + '/RobotoMono-Regular.ttf')
font.add_file(directory + '/superstar_memesbruh03.ttf')

midnight_blue = "#031a6b"
indigo_dye = "#033860"
cg_blue = "#087ca7"
yale_blue = "#004385"
cerulean_crayola = "#05b2dc"

window = Tk()
window.title("XXXXX PROJECT - Andrea Arias")  # Título
window.iconphoto(True, PhotoImage(file=directory + '/gear.png'))
window['bg'] = "white"

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
my_width = 500
my_height = 500
x = (int)(width / 2 - my_width / 2)
y = (int)(height / 2 - my_height / 2)
window.geometry(str(my_width) + "x" + str(my_height) +
                "+" + str(x) + "+" + str(y))

estyle = ttk.Style()
estyle.configure("TNotebook", background=yale_blue)

book = ttk.Notebook(window)

# Tab code 1
tab_1 = Frame(master=book, background=indigo_dye)
tab_1.grid_columnconfigure(0, weight=1)
tab_1.grid_rowconfigure([1, 2, 4], weight=1)

title_1 = Label(master=tab_1, text="PROBLEMA 1", font=(
    "Superstar", 25), foreground="White", background=indigo_dye)
title_1.grid(column=0, row=0, pady=5)

# Days input
days_element = Frame(master=tab_1, background=indigo_dye)
days_element.grid(column=0, row=1)

days_label = Label(master=days_element, text="Días de competencia en el vecindario:", font=(
    "Roboto Mono", 12), foreground="White", background=indigo_dye)
days_label.pack(side=TOP)

days_input = Entry(master=days_element, font=("Roboto Mono", 12),
                   foreground=midnight_blue, background="GreenYellow", justify=CENTER, width=4)
days_input.insert(0, "")
days_input.pack(side=TOP)

days_error = Label(master=days_element, font=(
    "Roboto Mono", 10), foreground="#ff0095", background=indigo_dye)
days_error.pack(side=TOP, fill=BOTH, expand=True)
# End days input

# Inputs problem 1
input_element = Frame(master=tab_1, background=indigo_dye)
input_element.grid(column=0, row=2)

input_label = Label(master=input_element, text="Entradas:", font=(
    "Roboto Mono", 12), foreground="White", background=indigo_dye)
input_label.pack(side=TOP)

big_box_1 = Frame(master=input_element, background=indigo_dye)
big_box_1.pack(side=TOP)

for index in range(len(houses)):
    box = Frame(master=big_box_1, background=indigo_dye, borderwidth=0)
    box.grid(row=0, column=index, padx=5)

    my_input = Entry(master=box, font=("Roboto Mono", 12), foreground=midnight_blue,
                     background="GreenYellow", justify=CENTER, width=3)
    my_input.insert(0, "")
    my_input.pack(side=TOP)
    inputs.append(my_input)

    number = Label(master=box, text=(index + 1), font=("Roboto Mono",
                   12), foreground="White", background=indigo_dye)
    number.pack(side=TOP)

input_error = Label(master=input_element, font=(
    "Roboto Mono", 10), foreground="#ff0095", background=indigo_dye)
input_error.pack(side=TOP, fill=BOTH, expand=True)
# End inputs problem 1

button_1 = Button(master=tab_1, text="Calcular", font=("Superstar", 12),
                  foreground=cerulean_crayola, background="White", borderwidth=0, command=validation)
button_1.grid(column=0, row=3, pady=1)

# Outputs problem 1
output_element = Frame(master=tab_1, background=indigo_dye)
output_element.grid(column=0, row=4)

output_label = Label(master=output_element, text="Salidas:", font=(
    "Roboto Mono", 12), foreground="White", background=indigo_dye)
output_label.pack(side=TOP, fill=BOTH, expand=True)

big_box_2 = Frame(master=output_element, background=cg_blue)
big_box_2.pack(side=TOP)

for index in range(8):
    box = Frame(master=big_box_2, background=indigo_dye, borderwidth=0)
    box.grid(row=0, column=index)

    my_output = Label(master=box, text="", font=(
        "Roboto Mono", 12, 'bold'), foreground="White", background=cg_blue, width=4)
    my_output.pack(side=TOP)
    outputs.append(my_output)

    number = Label(master=box, text=(index + 1), font=("Roboto Mono",
                   12), foreground="White", background=indigo_dye)
    number.pack(side=TOP)
# End outputs problem 1
# End tab code 1

# Tab code 2
tab_2 = Frame(master=book, background=indigo_dye)
tab_2.grid_columnconfigure(0, weight=1)
tab_2.grid_rowconfigure([0, 1, 2, 3], weight=1)

title_2 = Label(master=tab_2, text="PROBLEMA 2", font=(
    "Superstar", 25), foreground="White", background=indigo_dye)
title_2.grid(column=0, row=0)

# Input problem 2
string_element = Frame(tab_2, background=indigo_dye)
string_element.grid(column=0, row=1)

string_label = Label(master=string_element, text="Cadena a permutar:", font=(
    "Roboto Mono", 12), foreground="White", background=indigo_dye)
string_label.pack(side=TOP)

string_input = Entry(master=string_element, font=("Roboto Mono", 12),
                     foreground=midnight_blue, background="GreenYellow", justify=CENTER, width=30)
string_input.insert(0, "")
string_input.pack(side=TOP)
# En input problem 2

button_2 = Button(master=tab_2, text="Permutar", font=("Superstar", 12),
                  foreground=cerulean_crayola, background="White", borderwidth=0, command=permute_this)
button_2.grid(column=0, row=2)

# Output problem 2
permutation_element = Frame(tab_2, background=indigo_dye)
permutation_element.grid(column=0, row=3, sticky=EW, padx=100)

permutation_label = Label(master=permutation_element, text="Permutaciónes:", font=(
    "Roboto Mono", 12), foreground="White", background=indigo_dye)
permutation_label.pack(side=TOP)

permutation_output = scrolledtext.ScrolledText(master=permutation_element, font=(
    "Roboto Mono", 12), foreground="White", background=cg_blue, width=30, height=7, state=DISABLED, wrap=WORD)
permutation_output.pack(side=TOP, fill=BOTH, expand=True)
# End output problem 2
# End code 2

book.add(tab_1, text='Problem 1')
book.add(tab_2, text='Problem 2')
book.pack(expand=True, fill=BOTH)

permutation_output.focus()
window.mainloop()
# End window
