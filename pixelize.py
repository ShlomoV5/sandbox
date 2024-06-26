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

if __name__ == "__main__":
    # Example usage
    image_path = input("Enter path to the image file: ")
    pixel_size = int(input("Enter pixel size (in square pixels): "))
    
    pixelated_image = pixelate_image(image_path, pixel_size)
    
    # Save or display the pixelated image
    pixelated_image.show()
    # pixelated_image.save("pixelated_image.png")  # Uncomment to save the pixelated image
