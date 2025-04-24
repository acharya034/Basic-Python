import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update the time every second

root = tk.Tk()
root.title('Digital Clock')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

time()  # Initial call to display time
root.mainloop()
