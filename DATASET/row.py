from PIL import Image
import os

def crop_and_save(image_path, output_root_folder):
    # Open the image
    original_image = Image.open(image_path)

    # Get the dimensions of the original image
    width, height = original_image.size

    # Define the size of each cropped part
    crop_width = width // 12
    crop_height = height // 18

    # Create output root folder if it doesn't exist
    os.makedirs(output_root_folder, exist_ok=True)

    # Loop through each column
    for j in range(18):
        # Create a folder for each row
        row_folder = os.path.join(output_root_folder, f"row_{j}")
        os.makedirs(row_folder, exist_ok=True)

        # Loop through each row
        for i in range(12):
            # Calculate the coordinates for cropping
            left = i * crop_width
            upper = j * crop_height
            right = left + crop_width
            lower = upper + crop_height

            # Crop the image
            cropped_image = original_image.crop((left, upper, right, lower))

            # Save the cropped image to the row folder
            output_path = os.path.join(row_folder, f"set1_p2{i}.png")
            cropped_image.save(output_path)

# Example usage
image_path = "D:\\DATASET\\s1_p2.jpg"
output_root_folder = "p2"
crop_and_save(image_path, output_root_folder)
