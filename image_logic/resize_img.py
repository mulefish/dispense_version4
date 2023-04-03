# from PIL import Image

# # Open the image file
# img = Image.open('concentrate_shatter_1 copy.jpg')

# # Calculate the aspect ratio
# aspect_ratio = img.size[0] / img.size[1]

# # Calculate the new height based on the aspect ratio and target width of 100
# new_height = int(100 / aspect_ratio)

# # Resize the image using the new width and height
# resized_img = img.resize((100, new_height))

# # Crop the image to 100x100, clipping any extra height
# resized_img = resized_img.crop((0, 0, 100, 100))

# # Save the resized image
# resized_img.save('output_image.jpg')

from PIL import Image

# Open the image file
img = Image.open('concentrate_shatter_1 copy.png')



# Determine the smaller dimension of the image
width, height = img.size
smaller_dim = min(width, height)

# Resize the image to a square with the smaller dimension as the length
resized_img = img.resize((smaller_dim, smaller_dim))

# Resize the square image to have a length of 100 pixels
resized_img = resized_img.resize((100, 100))

# Save the resized image
resized_img.save('output_image2.png')