from PIL import Image, ImageDraw, ImageFont

def generate_ascii_map():
    # 1. Create a pure black 800x100 image
    img = Image.new('RGB', (800, 100), color='black')
    draw = ImageDraw.Draw(img)

    # 2. Our 8 characters from dark to bright
    chars = ['.', ':', '-', '=', '+', '*', '#', '@']

    # 3. Try to load a crisp, monospaced coding font
    try:
        # Windows standard monospaced font
        font = ImageFont.truetype("consola.ttf", 65) 
    except IOError:
        try:
            # Mac/Linux fallback
            font = ImageFont.truetype("Courier New.ttf", 65)
        except IOError:
            print("Standard fonts not found. Using default.")
            font = ImageFont.load_default()

    # 4. Draw each character perfectly centered in its 100x100 block
    for i, char in enumerate(chars):
        # Define the start X coordinate of this specific 100px block
        box_x = i * 100
        
        # Get the exact pixel width and height of the character
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        char_height = bbox[3] - bbox[1]
        
        # Calculate X and Y to center it within the 100x100 square
        center_x = box_x + ((100 - char_width) / 2) - bbox[0]
        center_y = ((100 - char_height) / 2) - bbox[1]
        
        # Draw the white text
        draw.text((center_x, center_y), char, fill='white', font=font)

    # 5. Save the mathematically perfect atlas
    img.save('ASCII_Map_Perfect.png')
    print("Successfully created ASCII_Map_Perfect.png!")

if __name__ == "__main__":
    generate_ascii_map()