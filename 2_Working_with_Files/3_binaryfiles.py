# Reading binary data from an image file
with open('2_Working_with_Files\image.jpg', 'rb') as file:
    image_data = file.read()

# Writing binary data to a new file
with open('2_Working_with_Files\copy_image.jpg', 'wb') as new_file:
    new_file.write(image_data)
