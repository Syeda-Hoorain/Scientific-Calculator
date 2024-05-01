import tkinter as tk
import math

# Layout:
root= tk.Tk()
root.title("Calculator")
root.geometry("375x600")
root.resizable(0, 0)

# Text styles:
fonts_list=[("Arial", 32, "bold"),("Arial", 10),("Arial", 20, "bold"),("Arial", 14)]
# Colors:
colors=["#F8FAFF","#FFFFFF","#F5F5F5","#CCEDFF","#25265E"]

# Frames:
def create_display_frame():
    frame = tk.Frame(root, height= 221, bg= colors[2])
    frame.pack(expand= True, fill= "both")
    return frame
display_frame = create_display_frame()

def create_button_frame():
    bt = tk.Frame(root)
    bt.pack(expand= True, fill= "both")
    return bt
button_frame = create_button_frame()

# Equation after pressing any operator:
total_expression = ""

#Equation before pressing any operator:
current_expression = ""

# Labels to display frames:
def create_display_labels():
    total_label = tk.Label(display_frame, text= total_expression, anchor= tk.E, bg= colors[2], fg= colors[4], padx= 20, font= fonts_list[1])
    total_label.pack(expand= True, fill= "both")

    label = tk.Label(display_frame, text= current_expression, anchor= tk.E, bg= colors[2], fg= colors[4], padx= 20, font= fonts_list[0])
    label.pack(expand= True, fill= "both")

    return total_label, label
total_label, label = create_display_labels()

# Operations updating the total label and label:
def update_total_label():
    global total_label, total_expression
    expression = total_expression
    for operator, symbol in operators.items():
        expression = expression.replace(operator, symbol)
    total_label.config(text= expression)

def update_label():
    global current_expression
    current_expression = str(current_expression)
    label.config(text= current_expression[:11])

# Adding functionality on frames:
def add_to_expression(value):
    global current_expression
    current_expression += str(value)
    update_label()

def add_operators(operator):
    global current_expression, total_expression
    current_expression += str(operator)
    total_expression = current_expression
    current_expression = ""
    update_total_label()
    update_label()

def add_power_operator():
    global current_expression
    current_expression += "^"
    update_label()

# Operators
def clear():
    global total_expression, current_expression
    total_expression = ""
    current_expression = ""
    update_total_label()
    update_label()

def evaluate():
    global total_expression, current_expression
    # for power function:
    if "^" in current_expression:
        n = int(current_expression[:current_expression.find("^")])
        x = int(current_expression[current_expression.find("^")+1::])
        result = power(n,x)
        current_expression = str(result)
    total_expression += current_expression
    update_total_label()

    try:
        current_expression = eval(total_expression) #add a condition when customizing functions are used.
        total_expression = ""
    except Exception as e:
        current_expression = "Error"
    finally:
        update_label()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*(factorial(n-1))

def power(n, x):
    result = 1
    for count in range(x):
        base=0
        for counter in range(n):
            base+=1
        result=result*base
    return result

def fac_func():
    global current_expression
    result = factorial(int(current_expression))
    current_expression = str(result)
    update_label()

def square():
    global current_expression
    current_expression = str(eval(current_expression + "**2"))
    update_label()

def sqrt():
    global current_expression
    current_expression = str(eval(current_expression + "**0.5"))
    update_label()

def sin_func():
    global current_expression
    expression = float(current_expression)
    current_expression = str(math.sin(expression))
    update_label()

def cos_func():
    global current_expression
    expression = float(current_expression)
    current_expression = str(math.cos(expression))
    update_label()

def tan_func():
    global current_expression
    expression = float(current_expression)
    current_expression = str(math.tan(expression))
    update_label()

digits = {
    7:(2,1), 8:(2,2), 9:(2,3),
    4:(3,1), 5:(3,2), 6:(3,3),
    1:(4,1), 2:(4,2), 3:(4,3),
    0:(5,2), ".":(5,1)
}

# Buttons:
def create_digit_buttons():
    for digit, grid_value in digits.items():
        button = tk.Button(button_frame, text= str(digit), bg= colors[1], fg= colors[4], font= fonts_list[2], borderwidth= 0, command=lambda x=digit: add_to_expression(x))
        button.grid(row=grid_value[0], column=grid_value[1], sticky= tk.NSEW)
create_digit_buttons()

operators ={"/": "\u00F7", "*":"\u00D7", "-":"-", "+":"+"}
def create_operator_buttons():
    r = 1
    for operator, symbol in operators.items():
        button = tk.Button(button_frame, text= symbol, bg= colors[0], fg= colors[4], font= fonts_list[3], borderwidth= 0, command= lambda x=operator: add_operators(x))
        button.grid(row= r, column= 4, sticky= tk.NSEW)
        r += 1
create_operator_buttons()

def create_fac_button():
    button = tk.Button(button_frame, text= "!", bg= colors[1], fg= colors[4], font= fonts_list[3], borderwidth= 0, command= lambda: fac_func())
    button.grid(row= 5, column= 3, sticky= tk.NSEW)

def create_clear_button():
    button = tk.Button(button_frame, text= "C", bg= colors[0], fg= colors[4], font= fonts_list[3], borderwidth= 0, command= lambda: clear())
    button.grid(row= 0, column= 1, sticky= tk.NSEW)

def create_sin_button():
    button = tk.Button(button_frame, text= "sin", bg= colors[0], fg= colors[4], font= fonts_list[3], border= 0, command= lambda: sin_func())
    button.grid(row= 0, column= 2, sticky= tk.NSEW)

def create_cos_button():
    button = tk.Button(button_frame, text= "cos", bg= colors[0], fg= colors[4], font= fonts_list[3], border= 0, command= lambda: cos_func())
    button.grid(row= 0, column= 3, sticky= tk.NSEW)

def create_tan_button():
    button = tk.Button(button_frame, text= "tan", bg= colors[0], fg= colors[4], font= fonts_list[3], border= 0, command= lambda: tan_func())
    button.grid(row= 0, column= 4, sticky= tk.NSEW)

def create_square_button():
    button = tk.Button(button_frame, text= "x\u00b2", bg= colors[0], fg= colors[4], font= fonts_list[3], borderwidth= 0, command= lambda: square())
    button.grid(row= 1, column= 2, sticky= tk.NSEW)

def create_sqrt_button():
    button = tk.Button(button_frame, text= "\u221ax", bg= colors[0], fg= colors[4], font= fonts_list[3], borderwidth= 0, command= lambda: sqrt())
    button.grid(row= 1, column= 3, sticky= tk.NSEW)

def create_power_button():
    button = tk.Button(button_frame, text= "^", bg= colors[0], fg= colors[4], font= fonts_list[3], borderwidth= 0, command= lambda: add_power_operator())
    button.grid(row= 1, column= 1, sticky= tk.NSEW)

def create_equals_to_button():
    button = tk.Button(button_frame, text= "=", bg= colors[3], fg= colors[4], font= fonts_list[3], borderwidth= 0, command=lambda: evaluate())
    button.grid(row= 5, column= 4, sticky= tk.NSEW)

def create_special_buttons():
    create_clear_button()
    create_equals_to_button()
    create_fac_button()
    create_sin_button()
    create_cos_button()
    create_tan_button()
    create_square_button()
    create_sqrt_button()
    create_power_button()
create_special_buttons()

# Buttons Frame:
button_frame.rowconfigure(0, weight= 1)
for i in range(1, 5):
    button_frame.rowconfigure(i, weight= 1)
    button_frame.columnconfigure(i, weight= 1)
button_frame.rowconfigure(5, weight=1)

# Main loop:
root.mainloop()

