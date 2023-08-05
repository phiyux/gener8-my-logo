from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from PIL import ImageTk

def generate_logo():
    global logo  # Declare logo as a global variable
    soft_blue = (204, 229, 255)
    beige_brown = (220, 200, 170)

    # Creating a blank canvas
    width, height = 800, 400
    logo = Image.new("RGB", (width, height), beige_brown)  # Assign the generated image to the global variable logo
    draw = ImageDraw.Draw(logo)

    # Drawing a subtle wave shape
    for i in range(height):
        x = width/2 + (width/4) * (1 - i/height) * (1 + 0.1 * i/height)
        draw.line([(x, i), (width, i)], fill=soft_blue, width=1)

    # Adding the text
    font_size = 60
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"  # Change this path to the correct font path
    font = ImageFont.truetype(font_path, font_size)
    text = "Lynda Vu"

    # Create a blank temporary image to calculate text size
    temp_image = Image.new("RGBA", (1, 1))
    text_lowercase = text.lower()
    temp_draw = ImageDraw.Draw(temp_image)
    text_bbox = temp_draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_position = ((width - text_width)/2, (height - text_height)/2)
    draw.text(text_position, text_lowercase, fill="white", font=font)

    # Conversion of the PIL image to Tkinter image
    tk_image = ImageTk.PhotoImage(logo)  # Use logo instead of image

    # Creating a label to display the image
    label = tk.Label(window, image=tk_image)
    label.image = tk_image  # Keep a reference to the image
    label.pack()

def save_logo():
    if logo:  # Check if the logo has been generated
        output_path = r"C:/Coding/GENERATE_LOGO/output/lynda_vu_logo.png"
        logo.save(output_path)  # Save the global logo variable
        print(f"Image saved to {output_path}")

# Create a new instance of Tkinter
window = tk.Tk()

# Set the window title
window.title("Gener8 My Logo")

# Set the window dimensions
window.geometry("400x300")

# Declare a global variable to store the generated image
logo = None

generateBtn = tk.Button(window, text="Afficher", command=generate_logo)
generateBtn.pack()

saveBtn = tk.Button(window, text="Save", command=save_logo)  # Save button
saveBtn.pack()

# Start the main event loop
window.mainloop()
