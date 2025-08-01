from PIL import Image, ImageTk
import tkinter as tk

# Load the images (images must be in the same folder as this script)
healed_img = Image.open("healed.png").resize((300, 400))
damaged_img = Image.open("damaged.png").resize((300, 400))

# Create GUI window
window = tk.Tk()
window.title("Self-Healing Screen Mini Project")

# Convert images to Tkinter-compatible format
healed_tk = ImageTk.PhotoImage(healed_img)
damaged_tk = ImageTk.PhotoImage(damaged_img)

# Layout
tk.Label(window, text="Damaged Screen").grid(row=0, column=0)
tk.Label(window, text="Healed Screen").grid(row=0, column=1)

tk.Label(window, image=damaged_tk).grid(row=1, column=0)
tk.Label(window, image=healed_tk).grid(row=1, column=1)

window.mainloop()
