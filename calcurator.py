import tkinter as tk


operation =[]
numbers =[]

def on_button_click_number(button_name):
    numbers.append(button_name)


def on_button_click_operation(button_name):
    operation.append(button_name)




root = tk.Tk()
root.title("Calcualtor")



button_reset= tk.Button(root, text="res", command=lambda:on_button_click_operation("res"))
button_reset.grid(row=0, column=0, padx=10, pady=10) 

button_bracket= tk.Button(root, text="()", command=lambda:on_button_click_operation("()"))
button_bracket.grid(row=0, column=1, padx=10, pady=10) 

button_precent= tk.Button(root, text="%", command=lambda:on_button_click_operation("%"))
button_precent.grid(row=0, column=2, padx=10, pady=10) 

button_divison= tk.Button(root, text=":", command=lambda:on_button_click_operation(":"))
button_divison.grid(row=0, column=3, padx=10, pady=10)





button1 = tk.Button(root, text=1, command=lambda:on_button_click_number(1))
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=2, command=lambda:on_button_click_number(2))
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(root, text=3, command=lambda:on_button_click_number(3))
button3.grid(row=1, column=2, padx=10, pady=10) 

button_multi = tk.Button(root, text="", command=lambda:on_button_click_operation(""))
button_multi.grid(row=1, column=3, padx=10, pady=10) 





button4 = tk.Button(root, text=4, command=lambda:on_button_click_number(4))
button4.grid(row=2, column=0, padx=10, pady=10)

button5 = tk.Button(root, text=5, command=lambda:on_button_click_number(5))
button5.grid(row=2, column=1, padx=10, pady=10)

button6 = tk.Button(root, text=6, command=lambda:on_button_click_number(6))
button6.grid(row=2, column=2, padx=10, pady=10)

button_minus= tk.Button(root, text="-", command=lambda:on_button_click_operation("-"))
button_minus.grid(row=2, column=3, padx=10, pady=10) 




button7 = tk.Button(root, text=7, command=lambda:on_button_click_number(7))
button7.grid(row=3, column=0, padx=10, pady=10)

button8 = tk.Button(root, text=8, command=lambda:on_button_click_number(8))
button8.grid(row=3, column=1, padx=10, pady=10)

button9 = tk.Button(root, text=9, command=lambda:on_button_click_number(9))
button9.grid(row=3, column=2, padx=10, pady=10)

button_plus = tk.Button(root, text="+", command=lambda:on_button_click_operation("+"))
button_plus.grid(row=3, column=3, padx=10, pady=10) 




button0= tk.Button(root, text=0, command=lambda:on_button_click_number(0))
button0.grid(row=4, column=0, padx=10, pady=10) 

button_coma= tk.Button(root, text=",", command=lambda:on_button_click_operation(","))
button_coma.grid(row=4, column=1, padx=10, pady=10) 

button_del= tk.Button(root, text="del", command=lambda:on_button_click_operation("del"))
button_del.grid(row=4, column=2, padx=10, pady=10) 

button_makes= tk.Button(root, text="=", command=lambda:on_button_click_operation("="))
button_makes.grid(row=4, column=3, padx=10, pady=10) 



 
button_extra= tk.Button(root, text="√", command=lambda:on_button_click_operation("√"))
button_extra.grid(row=5, column=0, padx=10, pady=10) 

button_pi= tk.Button(root, text="π", command=lambda:on_button_click_operation("π"))
button_pi.grid(row=5, column=1, padx=10, pady=10) 

button_expone= tk.Button(root, text="^", command=lambda:on_button_click_operation("^"))
button_expone.grid(row=5, column=2, padx=10, pady=10) 

button_factorial= tk.Button(root, text="!", command=lambda:on_button_click_operation("!"))
button_factorial.grid(row=5, column=3, padx=10, pady=10)

root.mainloop()