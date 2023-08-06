from PIL import Image, ImageDraw, ImageFont
from PIL import ImageTk
from constants import soft_blue, beige_brown, font_path

logo = None
tk_image = None

def generate_logo(text_content, text_color, label):
    global logo, tk_image
    text_content = text_content or "Lynda Vu"
    text_color = text_color or "white"

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
    label.create_image(0, 0, anchor="nw", image=tk_image)
    label.image = tk_image
