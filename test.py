


import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Catch the Falling Objects")

# Create canvas
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Create score label
score = 0
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Create basket
basket = canvas.create_rectangle(270, 550, 330, 580, fill="blue")

# Create falling objects
# objects = []
# for i in range(5):
#     x = random.randint(0, 590)
#     y = random.randint(0, 50)
#     objects.append(canvas.create_oval(x, y, x+10, y+10, fill="red"))

# Move basket
def move_basket(event):
    if event.keysym == "Left":
        canvas.move(basket, -20, 0)
    elif event.keysym == "Right":
        canvas.move(basket, 20, 0)

# Bind arrow keys
canvas.bind_all("<Key>", move_basket)

# # Move objects
# def move_objects():
#     global score
#     for obj in objects:
#         canvas.move(obj, 0, 5)
#         pos = canvas.coords(obj)
#
#         if pos[3] >= 600:
#             x = random.randint(0, 590)
#             y = random.randint(0, 50)
#             canvas.coords(obj, x, y, x+10, y+10)
#         elif len(canvas.find_overlapping(*canvas.coords(basket))) > 1:
#             x = random.randint(0, 590)
#             y = random.randint(0, 50)
#             canvas.coords(obj, x, y, x+10, y+10)
#             score += 1
#             score_label.config(text=f"Score: {score}")
#     root.after(50, move_objects)
#
# move_objects()

root.mainloop()