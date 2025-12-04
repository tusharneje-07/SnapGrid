import os
from ttkbootstrap import Style
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar
from tkinter.ttk import Progressbar
from PIL import Image, ImageDraw
from tkinter import messagebox


def arrange_photos(input_folder, output_folder, page_width, page_height, page_margin, grid_margin, rows, cols, progress_var, progress_bar):
    try:
        # Calculate available space
        available_width = page_width - 2 * page_margin - (cols - 1) * grid_margin
        available_height = page_height - 2 * page_margin - (rows - 1) * grid_margin

        grid_width = available_width // cols
        grid_height = int(grid_width * 9 / 16)  # Maintain 16:9 aspect ratio

        # Adjust dimensions if height exceeds available space
        if grid_height * rows + (rows - 1) * grid_margin > available_height:
            grid_height = available_height // rows
            grid_width = int(grid_height * 16 / 9)

        # Load images
        images = [
            os.path.join(input_folder, f)
            for f in os.listdir(input_folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
        os.makedirs(output_folder, exist_ok=True)

        # Set up progress
        progress_var.set(0)
        progress_bar["maximum"] = len(images)

        page_count = 1
        img_index = 0

        while img_index < len(images):
            # Create a blank page
            page = Image.new("RGB", (page_width, page_height), "white")
            draw = ImageDraw.Draw(page)

            for row in range(rows):
                for col in range(cols):
                    if img_index >= len(images):
                        break

                    # Open image
                    img = Image.open(images[img_index])

                    # Ensure the image is 16:9 by cropping
                    img_width, img_height = img.size
                    target_aspect_ratio = 16 / 9
                    img_aspect_ratio = img_width / img_height

                    if img_aspect_ratio > target_aspect_ratio:
                        # Crop width
                        new_width = int(img_height * target_aspect_ratio)
                        left = (img_width - new_width) // 2
                        right = left + new_width
                        img = img.crop((left, 0, right, img_height))
                    elif img_aspect_ratio < target_aspect_ratio:
                        # Crop height
                        new_height = int(img_width / target_aspect_ratio)
                        top = (img_height - new_height) // 2
                        bottom = top + new_height
                        img = img.crop((0, top, img_width, bottom))

                    # Resize to grid dimensions
                    img = img.resize((grid_width, grid_height), Image.LANCZOS)

                    # Calculate position on the page
                    x = page_margin + col * (grid_width + grid_margin)
                    y = page_margin + row * (grid_height + grid_margin)
                    page.paste(img, (x, y))

                    img_index += 1
                    progress_var.set(img_index)
                    progress_bar.update()

            # Save the page
            page.save(os.path.join(output_folder, f"page_{page_count}.jpg"), "JPEG")
            page_count += 1

        messagebox.showinfo("Success", f"All images processed! Pages saved in '{output_folder}'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def browse_folder(entry_field):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_field.set(folder_selected)


def run_application():
    try:
        # Get user inputs
        input_folder = input_folder_var.get()
        output_folder = output_folder_var.get()
        page_width = int(page_width_var.get())
        page_height = int(page_height_var.get())
        page_margin = int(page_margin_var.get())
        grid_margin = int(grid_margin_var.get())
        rows = int(rows_var.get())
        cols = int(cols_var.get())

        # Validate inputs
        if not input_folder or not output_folder:
            raise ValueError("Input and Output folders must be specified.")
        if not os.path.exists(input_folder):
            raise ValueError("Input folder does not exist.")
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and Columns must be greater than 0.")

        # Process images
        arrange_photos(input_folder, output_folder, page_width, page_height, page_margin, grid_margin, rows, cols, progress_var, progress_bar)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create GUI with ttkbootstrap
style = Style("darkly")
root = style.master
root.title("Photo Arranger")

# String variables for user inputs
input_folder_var = StringVar()
output_folder_var = StringVar()
page_width_var = StringVar(value="5400")  # Default A3 width
page_height_var = StringVar(value="3600")  # Default A3 height
page_margin_var = StringVar(value="100")
grid_margin_var = StringVar(value="20")
rows_var = StringVar(value="2")
cols_var = StringVar(value="2")

# Progress bar variable
progress_var = StringVar(value="0")

# Input folder
Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1, padx=10, pady=5)
Button(root, text="Browse", command=lambda: browse_folder(input_folder_var)).grid(row=0, column=2, padx=10, pady=5)

# Output folder
Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1, padx=10, pady=5)
Button(root, text="Browse", command=lambda: browse_folder(output_folder_var)).grid(row=1, column=2, padx=10, pady=5)

# Page width
Label(root, text="Page Width (px):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=page_width_var, width=20).grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Page height
Label(root, text="Page Height (px):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=page_height_var, width=20).grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Page margin
Label(root, text="Page Margin (px):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=page_margin_var, width=20).grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Grid margin
Label(root, text="Grid Margin (px):").grid(row=5, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=grid_margin_var, width=20).grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Rows
Label(root, text="Rows:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=rows_var, width=20).grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Columns
Label(root, text="Columns:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
Entry(root, textvariable=cols_var, width=20).grid(row=7, column=1, padx=10, pady=5, sticky="w")

# Progress bar
progress_bar = Progressbar(root, orient="horizontal", mode="determinate", variable=progress_var)
progress_bar.grid(row=8, column=0, columnspan=3, padx=10, pady=20, sticky="ew")

# Run button
Button(root, text="Run", command=run_application).grid(row=9, column=1, pady=20)

# Start the GUI loop
root.mainloop()