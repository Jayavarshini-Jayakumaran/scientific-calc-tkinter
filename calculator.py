from tkinter import *
import math

# Globals
equation_text = ""
output_text = ""
angle_mode = "DEG"

safe_dict = {}

def update_safe_dict():
    global safe_dict, angle_mode
    safe_dict = {
        'sin': lambda x: math.sin(math.radians(x)) if angle_mode == "DEG" else math.sin(x),
        'cos': lambda x: math.cos(math.radians(x)) if angle_mode == "DEG" else math.cos(x),
        'tan': lambda x: math.tan(math.radians(x)) if angle_mode == "DEG" else math.tan(x),
        'asin': lambda x: math.degrees(math.asin(x)) if angle_mode == "DEG" else math.asin(x),
        'acos': lambda x: math.degrees(math.acos(x)) if angle_mode == "DEG" else math.acos(x),
        'atan': lambda x: math.degrees(math.atan(x)) if angle_mode == "DEG" else math.atan(x),
        'sqrt': math.sqrt,
        'log': math.log10,
        'ln': math.log,
        'exp': math.exp,
        'pi': math.pi,
        'e': math.e,
        'pow': pow,
        'abs': abs
    }

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation.set(equation_text)

def equals():
    global equation_text, output_text
    try:
        total = str(eval(equation_text, {"__builtins__": None}, safe_dict))
        output.set(total)
        output_text = total
    except:
        output.set("Error")
        output_text = ""

def clear():
    global equation_text, output_text
    equation.set("")
    output.set("")
    equation_text = ""
    output_text = ""

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation.set(equation_text)

def toggle_mode():
    global angle_mode
    if angle_mode == "DEG":
        mode_button.config(text="RAD")
        angle_mode = "RAD"
    else:
        mode_button.config(text="DEG")
        angle_mode = "DEG"
    update_safe_dict()

# Initialize safe_dict initially
update_safe_dict()

# GUI
window = Tk()
window.title("Pixel Pro Calculator")
icon = PhotoImage(file='assets/Pixel Calculator-Icon.png')
window.iconphoto(True, icon)
window.configure(bg="#FFB6C1")
window.geometry("580x700")
window.resizable(False, False)

# Pixel Fonts
FONT_MAIN = ("Courier New", 22)
FONT_BTN = ("Courier New", 16, "bold")

# Custom Button Creator
def create_button(parent, text, command, row, col, colspan=1, color="#ffd6ba"):
    btn = Button(parent, text=text, font=FONT_BTN, bg=color, fg="#333333",
                 width=5, height=2, relief=FLAT, command=command, bd=3,
                 activebackground="#f9dcc4", activeforeground="#222222",
                 highlightbackground="#d3d3d3", cursor="hand2")
    btn.grid(row=row, column=col, columnspan=colspan, padx=7, pady=7, sticky="nsew")

equation = StringVar()
output = StringVar()

# Entry frames for visible textboxes
equation_frame = Frame(window, bg="#d3d3d3", padx=3, pady=3)
equation_frame.pack(padx=20, pady=(20, 10), fill="x")

entry_equation = Entry(
    equation_frame, textvariable=equation, font=FONT_MAIN, bg="#fff8f0",
    borderwidth=0, relief=FLAT, justify=RIGHT, fg="#333333",
    highlightthickness=0, insertbackground="#333333"
)
entry_equation.pack(fill="both")

output_frame = Frame(window, bg="#d3d3d3", padx=3, pady=3)
output_frame.pack(padx=20, pady=(0, 20), fill="x")

entry_output = Entry(
    output_frame, textvariable=output, font=FONT_MAIN, bg="#fff8f0",
    borderwidth=0, relief=FLAT, justify=RIGHT, fg="#333333",
    highlightthickness=0, insertbackground="#333333"
)
entry_output.pack(fill="both")

# Frame container for buttons
frame = Frame(window, bg="#fef6f5")
frame.pack()

# Scientific Row 1
functions = [('π', 'pi'), ('e', 'e'), ('√', 'sqrt('), ('x²', '**2'), ('x³', '**3'), ('1/x', '1/')]
for i, (txt, val) in enumerate(functions):
    create_button(frame, txt, lambda v=val: button_press(v), 0, i)

# Scientific Row 2
trigs = [('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('), ('ln', 'ln('), ('log', 'log('), ('exp', 'exp(')]
for i, (txt, val) in enumerate(trigs):
    create_button(frame, txt, lambda v=val: button_press(v), 1, i)

# Row 3 (Custom layout with equal & DEG/RAD in this row)
create_button(frame, '7', lambda: button_press('7'), 2, 0)
create_button(frame, '8', lambda: button_press('8'), 2, 1)
create_button(frame, '9', lambda: button_press('9'), 2, 2)
create_button(frame, '+', lambda: button_press('+'), 2, 3)

equal_btn = Button(frame, text="=", font=FONT_BTN, bg="#ffadad", fg="#333333",
                   width=5, height=2, relief=FLAT, command=equals, bd=3,
                   activebackground="#f9c0c0", activeforeground="#222222", cursor="hand2")
equal_btn.grid(row=2, column=4, padx=7, pady=7, sticky="nsew")

mode_button = Button(frame, text="DEG", font=FONT_BTN, bg="#bde0fe", fg="#333333",
                     width=5, height=2, relief=FLAT, command=toggle_mode, bd=3,
                     activebackground="#a0d2ff", activeforeground="#222222", cursor="hand2")
mode_button.grid(row=2, column=5, padx=7, pady=7, sticky="nsew")

# Remaining rows
buttons = [
    [('4', '4'), ('5', '5'), ('6', '6'), ('-', '-')],
    [('1', '1'), ('2', '2'), ('3', '3'), ('*', '*')],
    [('0', '0'), ('.', '.'), ('/', '/'), ('^', '**')],
]

for r, row in enumerate(buttons):
    for c, (txt, val) in enumerate(row):
        create_button(frame, txt, lambda v=val: button_press(v), r+3, c)

# Last row
control = [('(', '('), (')', ')'), ('←', 'back'), ('C', 'clear')]
for i, (txt, val) in enumerate(control):
    cmd = backspace if val == 'back' else (clear if val == 'clear' else lambda v=val: button_press(v))
    create_button(frame, txt, cmd, 6, i)

# Start app
window.mainloop()
