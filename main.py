import tkinter as tk
from logo_generator import generate_logo

def save_logo():
    if logo:
        output_path = r"C:/Coding/GENERATE_LOGO/output/lynda_vu_logo.png"
        logo.save(output_path)
        print(f"Image saved to {output_path}")

window = tk.Tk()
window.title("Gener8 My Logo")
window.geometry("400x300")

text_label = tk.Label(window, text="Enter Text:")
text_label.pack()
text_entry = tk.Entry(window)
text_entry.pack()

color_label = tk.Label(window, text="Enter Text Color:")
color_label.pack()
color_entry = tk.Entry(window)
color_entry.pack()

label = tk.Label(window)
label.pack()

generateBtn = tk.Button(window, text="OK", command=lambda: generate_logo(text_entry.get(), color_entry.get(), label))
generateBtn.pack()

saveBtn = tk.Button(window, text="Save", command=save_logo)
saveBtn.pack()

logo = None
tk_image = None

window.mainloop()
