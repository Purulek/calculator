import tkinter as tk


def on_button_click(button_name):
    print(f"clic {button_name}")


root = tk.Tk()
root.title("Panel z przyciskami")


button1 = tk.Button(root, text=1, command=lambda:on_button_click(1))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=2, command=lambda:on_button_click(2))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(root, text=3, command=lambda:on_button_click(3))
button3.grid(row=0, column=2, padx=10, pady=10)
button4 = tk.Button(root, text=4, command=lambda:on_button_click(4))
button4.grid(row=1, column=0, padx=10, pady=10)


button5 = tk.Button(root, text=5, command=lambda:on_button_click(5))
button5.grid(row=1, column=1, padx=10, pady=10)




button6 = tk.Button(root, text=6, command=lambda:on_button_click(3))
button6.grid(row=1, column=2, padx=10, pady=10)





button7 = tk.Button(root, text=7, command=lambda:on_button_click(3))
button7.grid(row=2, column=0, padx=10, pady=10)




button8 = tk.Button(root, text=8, command=lambda:on_button_click(8))
button8.grid(row=2, column=1, padx=10, pady=10)



button9 = tk.Button(root, text=9, command=lambda:on_button_click(9))
button9.grid(row=2, column=2, padx=10, pady=10)
import tkinter as tk


def on_button_click(button_name):
    print(f"clic {button_name}")


root = tk.Tk()
root.title("Calcualtor")


button1 = tk.Button(root, text=1, command=lambda:on_button_click(1))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=2, command=lambda:on_button_click(2))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(root, text=3, command=lambda:on_button_click(3))
button3.grid(row=0, column=2, padx=10, pady=10) 

button_multi = tk.Button(root, text="", command=lambda:on_button_click(""))
button_multi.grid(row=0, column=3, padx=10, pady=10) 

button4 = tk.Button(root, text=4, command=lambda:on_button_click(4))
button4.grid(row=1, column=0, padx=10, pady=10)


button5 = tk.Button(root, text=5, command=lambda:on_button_click(5))
button5.grid(row=1, column=1, padx=10, pady=10)




button6 = tk.Button(root, text=6, command=lambda:on_button_click(3))
button6.grid(row=1, column=2, padx=10, pady=10)


button_minus= tk.Button(root, text="-", command=lambda:on_button_click("-"))
button_minus.grid(row=1, column=3, padx=10, pady=10) 


button7 = tk.Button(root, text=7, command=lambda:on_button_click(3))
button7.grid(row=2, column=0, padx=10, pady=10)




button8 = tk.Button(root, text=8, command=lambda:on_button_click(8))
button8.grid(row=2, column=1, padx=10, pady=10)



button9 = tk.Button(root, text=9, command=lambda:on_button_click(9))
button9.grid(row=2, column=2, padx=10, pady=10)

button_plus = tk.Button(root, text="+", command=lambda:on_button_click("+"))
button_plus.grid(row=2, column=3, padx=10, pady=10) 


button0= tk.Button(root, text=0, command=lambda:on_button_click(0))
button0.grid(row=3, column=0, padx=10, pady=10) 


button_coma= tk.Button(root, text=",", command=lambda:on_button_click(","))
button_coma.grid(row=3, column=1, padx=10, pady=10) 


button_del= tk.Button(root, text="del", command=lambda:on_button_click("del"))
button_del.grid(row=3, column=2, padx=10, pady=10) 


button_makes= tk.Button(root, text="=", command=lambda:on_button_click("="))
button_makes.grid(row=3, column=3, padx=10, pady=10) 



root.mainloop()