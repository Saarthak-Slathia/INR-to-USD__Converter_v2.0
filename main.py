from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
from PIL import Image, ImageTk

def conversion():
    try:
        rawData = input.get()
        val = float (input.get())
        # print(val)
        output = val * 0.013
        output_round = round(output, 2)
        display_output.config(text=f"₹ {rawData} (Rupees/INR) is equal to $ {output_round} (Dollars/USD)")
    except ValueError:
        display_output.config(text="Sorry, Invalid Input !!! Enter the input in Numbers :(")
    except Exception:
        display_output.config(text="Oh oh !!! Maybe there is some error at our end. Please try again later :(")

root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance") # Theme options - breeze, clearlooks, blue, black, equilux etc. Find more about them at --> https://ttkthemes.readthedocs.io/en/latest/themes.html
root.geometry("800x450+350+150")
root.title("USD to INR")
root.iconbitmap(r"D:\Saarthak\Programming\Python\Tkinter\GUI\MyGUI\favicon.ico")
root.config(bg="white smoke")

header = ttk.Label(root, text="INR to USD Converter", font=("Josefin Sans", 21))
header.pack(pady=40)


input_label = ttk.Label(root, text="Enter the value in INR below:-", font=("Josefin Sans", 8))
input_label.pack()
input = ttk.Entry(root, width=25)
input.pack()

image = Image.open(r"D:\Saarthak\Programming\Python\Tkinter\GUI\MyGUI\btn.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)

submit = ttk.Button(root, text="Convert", command=conversion)
submit.pack(pady=30)

display_output = ttk.Label(root, text="Submit to get value in USD", font=("Josefin Sans", 15))
display_output.pack(pady=40)

root.mainloop()
