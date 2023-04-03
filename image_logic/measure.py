from PIL import Image

# Open the PNG file
with Image.open('output_image.png') as img:

    # Get the X and Y dimensions
    x_dim, y_dim = img.size
    
    # Print the dimensions
    print(f"The dimensions of the PNG image are {x_dim} x {y_dim}")