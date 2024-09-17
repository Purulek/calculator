import tkinter as tk
from tkinter import messagebox
import math
import operator

operation =[]
numbers_before =[]
numbers_after = []
number = 0
float_number = 0
    
#appends new number to the calculation 
def on_button_click_number(button_name):
    numbers_before.append(button_name)
    if "." in operation:
        operation.remove(".")
        numbers_before.append(float_number + numbers_before[-1])
        del numbers_before[-3:-1]
    elif "-" in operation:
        print("_"*4, numbers_after)
        if len(numbers_after) == 0 or len(operation) >= len(numbers_after):
            print("_"*4, numbers_after)
            operation.remove("-")   
        else:
            operation.remove("-")
            operation.append("+")
        numbers_before[len(numbers_before)- 1] = "-" + numbers_before[len(numbers_before)- 1]

        


# appends new opertion to eqution
def on_button_click_operation(button_name):
    global number, numbers_before, numbers_after, float_number
    if button_name == "√" or  button_name =="!":
        pass
    
    elif button_name == ".":
        float_number = numbers_before[-1] + "."

    else:
        try:
            number = float(''.join (numbers_before))
            numbers_before = []
            numbers_after.append(number)
            print(numbers_before,"!"*8)

        except:
            pass
    operation.append(button_name)




# command wich execute the calculation  
def on_button_click_exe():
    global number, numbers_before, numbers_after
    print(numbers_after)
    number = float(''.join (numbers_before))
    numbers_before = []
    numbers_after.append(number)
    print(numbers_after)
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv  

    }
    i = 0
    score = 0
    for oper  in operation:
        print(numbers_after)
        print(oper)

        if oper == "√":
            score += math.sqrt(numbers_after[i])  
            
        elif oper == "^":
            score += (numbers_after[i]) ** numbers_after[i+1]
            
        elif oper == "!":
            score += math.factorial(int(numbers_after[i]))
        
            
        elif i == 0:
            i += 1
            score = operators[oper](numbers_after[0],numbers_after[i])
            

        elif i > 1:
            score = operators[oper](score, numbers_after[i])
            
        i += 1

    numbers_after.clear()
    numbers_before.clear()
    operation.clear()
    
    messagebox.showinfo("result", "your's result is: {}".format( score))




def on_button_click_restart():
    numbers_after.clear()
    numbers_before.clear()
    operation.clear()

    

root = tk.Tk()
root.title("Calculator")


# buttons in calcurtor
button_reset= tk.Button(root, text="res", command=lambda:on_button_click_restart())
button_reset.grid(row=0, column=0, padx=10, pady=10) 


button_factorial= tk.Button(root, text="!", command=lambda:on_button_click_operation("!"))
button_factorial.grid(row=0, column=1, padx=10, pady=10)

button_precent= tk.Button(root, text="%", command=lambda:on_button_click_operation("%"))
button_precent.grid(row=0, column=2, padx=10, pady=10) 

button_divison= tk.Button(root, text="/", command=lambda:on_button_click_operation("/"))
button_divison.grid(row=0, column=3, padx=10, pady=10)





button1 = tk.Button(root, text=1, command=lambda:on_button_click_number("1"))
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=2, command=lambda:on_button_click_number("2"))
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(root, text=3, command=lambda:on_button_click_number("3"))
button3.grid(row=1, column=2, padx=10, pady=10) 

button_multi = tk.Button(root, text="*", command=lambda:on_button_click_operation("*"))
button_multi.grid(row=1, column=3, padx=10, pady=10) 





button4 = tk.Button(root, text=4, command=lambda:on_button_click_number("4"))
button4.grid(row=2, column=0, padx=10, pady=10)

button5 = tk.Button(root, text=5, command=lambda:on_button_click_number("5"))
button5.grid(row=2, column=1, padx=10, pady=10)

button6 = tk.Button(root, text=6, command=lambda:on_button_click_number("6"))
button6.grid(row=2, column=2, padx=10, pady=10)

button_minus= tk.Button(root, text="-", command=lambda:on_button_click_operation("-"))
button_minus.grid(row=2, column=3, padx=10, pady=10) 




button7 = tk.Button(root, text=7, command=lambda:on_button_click_number("7"))
button7.grid(row=3, column=0, padx=10, pady=10)

button8 = tk.Button(root, text=8, command=lambda:on_button_click_number("8"))
button8.grid(row=3, column=1, padx=10, pady=10)

button9 = tk.Button(root, text=9, command=lambda:on_button_click_number("9"))
button9.grid(row=3, column=2, padx=10, pady=10)

button_plus = tk.Button(root, text="+", command=lambda:on_button_click_operation("+"))
button_plus.grid(row=3, column=3, padx=10, pady=10) 




button0= tk.Button(root, text=0, command=lambda:on_button_click_number("0"))
button0.grid(row=4, column=0, padx=10, pady=10) 

button_coma= tk.Button(root, text=".", command=lambda:on_button_click_operation("."))
button_coma.grid(row=4, column=1, padx=10, pady=10) 

button_expone= tk.Button(root, text="^", command=lambda:on_button_click_operation("^"))
button_expone.grid(row=4, column=2, padx=10, pady=10) 

button_makes= tk.Button(root, text="=", command=lambda:on_button_click_exe())
button_makes.grid(row=4, column=3, padx=10, pady=10) 



 
button_extra= tk.Button(root, text="√", command=lambda:on_button_click_operation("√"))
button_extra.grid(row=5, column=0, padx=10, pady=10) 

button_pi= tk.Button(root, text="π", command=lambda:on_button_click_number("3.14"))
button_pi.grid(row=5, column=1, padx=10, pady=10) 




root.mainloop()
