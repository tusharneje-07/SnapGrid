from PIL import Image, ImageDraw
import os
from tqdm import tqdm

# Constants
A3_WIDTH, A3_HEIGHT = 5400, 3600 # A3 size in pixels at 300 DPI
PAGE_MARGIN = 80  # Margin around the entire page (in pixels)
GRID_MARGIN = 20  # Space between images (in pixels)
ROWS, COLS = 4, 3  # 4 rows, 3 columns

# Calculate grid cell dimensions
AVAILABLE_WIDTH = A3_WIDTH - 2 * PAGE_MARGIN - (COLS - 1) * GRID_MARGIN
AVAILABLE_HEIGHT = A3_HEIGHT - 2 * PAGE_MARGIN - (ROWS - 1) * GRID_MARGIN

GRID_WIDTH = AVAILABLE_WIDTH // COLS
GRID_HEIGHT = int(GRID_WIDTH * 9 / 16)  # Maintain 16:9 aspect ratio

# Adjust dimensions if height exceeds available space
if GRID_HEIGHT * ROWS + (ROWS - 1) * GRID_MARGIN > AVAILABLE_HEIGHT:
    GRID_HEIGHT = AVAILABLE_HEIGHT // ROWS
    GRID_WIDTH = int(GRID_HEIGHT * 16 / 9)

def arrange_photos(input_folder, output_folder):
    # Load images
    images = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith((".png", ".jpg", ".jpeg"))]
    os.makedirs(output_folder, exist_ok=True)

    # Progress bar
    print(f"Processing {len(images)} images...")
    progress = tqdm(total=len(images))

    page_count = 1
    img_index = 0

    while img_index < len(images):
        # Create a blank A3 page
        page = Image.new("RGB", (A3_WIDTH, A3_HEIGHT), "white")
        draw = ImageDraw.Draw(page)

        for row in range(ROWS):
            for col in range(COLS):
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
                img = img.resize((GRID_WIDTH, GRID_HEIGHT), Image.LANCZOS)

                # Calculate position on the page
                x = PAGE_MARGIN + col * (GRID_WIDTH + GRID_MARGIN)
                y = PAGE_MARGIN + row * (GRID_HEIGHT + GRID_MARGIN)
                page.paste(img, (x, y))

                img_index += 1
                progress.update(1)

        # Save the page
        page.save(os.path.join(output_folder, f"page_{page_count}.jpg"), "JPEG")
        page_count += 1

    progress.close()
    print(f"All images processed! Pages saved in '{output_folder}'.")

# Input and output folders
input_folder = "input"  # Replace with your input folder path
output_folder = "output"  # Replace with your output folder path

# Call the function
arrange_photos(input_folder, output_folder)
