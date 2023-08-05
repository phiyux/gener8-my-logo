from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from PIL import ImageTk

def generate_logo():
    global logo, tk_image
    soft_blue = (204, 229, 255)
    beige_brown = (220, 200, 170)
    text_content = text_entry.get() or "Lynda Vu"
    text_color = color_entry.get() or "white"

    # Creating a blank canvas
    width, height = 800, 400
    logo = Image.new("RGB", (width, height), beige_brown)
    draw = ImageDraw.Draw(logo)

    # Drawing a subtle wave shape
    for i in range(height):
        x = width/2 + (width/4) * (1 - i/height) * (1 + 0.1 * i/height)
        draw.line([(x, i), (width, i)], fill=soft_blue, width=1)

    # Adding the text
    font_size = 60
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # Create a blank temporary image to calculate text size
    temp_image = Image.new("RGBA", (1, 1))
    temp_draw = ImageDraw.Draw(temp_image)
    text_bbox = temp_draw.textbbox((0, 0), text_content, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_position = ((width - text_width)/2, (height - text_height)/2)
    draw.text(text_position, text_content.lower(), fill=text_color, font=font)

    # Conversion of the PIL image to Tkinter image
    tk_image = ImageTk.PhotoImage(logo)
    label.config(image=tk_image)
    label.image = tk_image

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

generateBtn = tk.Button(window, text="OK", command=generate_logo)
generateBtn.pack()

saveBtn = tk.Button(window, text="Save", command=save_logo)
saveBtn.pack()

label = tk.Label(window)
label.pack()

logo = None
tk_image = None

window.mainloop()
