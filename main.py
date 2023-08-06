# main.py

from tkinter import Canvas, Tk, Toplevel, simpledialog
from logo_generator import generate_logo

def is_click_near_text(click_x, click_y, text_x, text_y, tolerance=30):
    return abs(click_x - text_x) <= tolerance and abs(click_y - text_y) <= tolerance

def on_canvas_click(event):
    # Check if click is near the main text position
    width, height = 800, 400
    main_text_position = (width // 2, height // 2)
    if is_click_near_text(event.x, event.y, *main_text_position):
        new_text = simpledialog.askstring("Input", "Enter new text:")
        if new_text:
            canvas.delete("all")  # Clear the canvas
            generate_logo(new_text, "white", canvas)
    else:
        # Check if click is near the other_text position
        other_text_position = (event.x, event.y)
        if is_click_near_text(event.x, event.y, *other_text_position):
            other_text = simpledialog.askstring("Input", "Enter new text 2:")
            if other_text:
                font = ("Arial", 12)
                text_color = "black"
                # Draw the new text on the canvas at the clicked location
                canvas.create_text(event.x, event.y, text=other_text, font=font, fill=text_color)


window = Tk()
window.title("Gener8 My Logo")
window.geometry("800x400")

canvas = Canvas(window, bg='white', width=800, height=400)
canvas.pack(pady=20)

generate_logo("type sumthing", "white", canvas)

# Bind the canvas click event to the on_canvas_click function
canvas.bind("<Button-1>", on_canvas_click)

window.mainloop()
