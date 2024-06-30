import inquirer
import os
from PIL import Image

def pixelate_image(image_path, pixel_size):
    # Open the image
    img = Image.open(image_path)
    
    # Get the size of the image
    width, height = img.size
    
    # Calculate number of pixels in both dimensions
    num_pixels_width = width // pixel_size
    num_pixels_height = height // pixel_size
    
    # Resize image to small size and back to original size to create pixelation effect
    img_small = img.resize((num_pixels_width, num_pixels_height), Image.NEAREST)
    img_pixelated = img_small.resize((width, height), Image.NEAREST)
    
    return img_pixelated

def select_file():
    # List files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    
    if not files:
        print("No image files found in the current directory.")
        return None

    questions = [
        inquirer.List('file',
                      message="Select an image file",
                      choices=files,
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    return answers['file'] if answers else None

def slider(term, min_val=2, max_val=100):
    pixel_size = min_val
    with term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)
            print(f"Use arrow keys to set pixel size: {pixel_size}px (Press Enter to select)")
            print("[" + "=" * (pixel_size - min_val) + " " * (max_val - pixel_size) + "]")
            key = term.inkey()
            if key.name == 'KEY_LEFT' and pixel_size > min_val:
                pixel_size -= 1
            elif key.name == 'KEY_RIGHT' and pixel_size < max_val:
                pixel_size += 1
            elif key.name == 'KEY_ENTER':
                break
    return pixel_size

def image_to_hex_array(img):
    # Open the image
    # img = Image.open(image_path)
    
    # Get the size of the image
    width, height = img.size
    
    # Convert the image to RGB
    img = img.convert('RGB')
    
    # Create a 2D array to store the hex codes
    hex_array = []
    
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            row.append(hex_code)
        hex_array.append(row)
    
    return hex_array

def hex_array_to_image(hex_array):
    """Converts a 2D array of hex color codes to an Image object."""
    try:
        # Get the dimensions of the hex array
        height = len(hex_array)
        width = len(hex_array[0]) if height > 0 else 0
        
        if width == 0:
            raise ValueError("Hex array must have at least one row with hex codes.")
        
        # Create a new Image object with RGB mode and size based on the hex array
        img = Image.new('RGB', (width, height))
        
        # Iterate through each pixel in the hex array
        for y in range(height):
            for x in range(width):
                # Get the hex code from the hex array
                hex_code = hex_array[y][x]
                
                # Convert hex code to RGB tuple
                rgb = tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))  # Convert hex to RGB
                
                # Set the pixel color in the Image object
                img.putpixel((x, y), rgb)
        
        return img
    
    except Exception as e:
        print(f"Error converting hex array to Image: {e}")
        return None

def main():

    # Select a file using CLI
    image_path = select_file()

    if not image_path:
        print("No file selected.")
        return



    pixel_size = 20
    
    # Pixelate the image
    pixelated_image = pixelate_image(image_path, pixel_size)
    
    # Save or display the pixelated image
    image_array = image_to_hex_array(pixelated_image)
    # print(image_array)
    # print(len(image_array))
    # pixelated_image.show()
    hex_array_to_image(image_array).show()
    # pixelated_image.save("pixelated_image.png")  # Uncomment to save the pixelated image
    print(image_path)
    
if __name__ == "__main__":
    main()
