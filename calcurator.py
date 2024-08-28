import tkinter as tk


def on_button_click(button_name):
    print(f"clic {button_name}")


root = tk.Tk()
root.title("Panel z przyciskami")


button1 = tk.Button(root, text=1, command=lambda:on_button_click(1))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(root, text=2, command=lambda:on_button_click(2))
button2.grid(row=0, column=1, padx=10, pady=10)


root.mainloop()