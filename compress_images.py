import os
from PIL import Image


def compress_images(input_folder, output_folder, max_size_mb=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(input_folder, filename)
            image = Image.open(filepath)


            quality = 95
            output_path = os.path.join(output_folder, filename)
            image.save(output_path, "JPEG", quality=quality)

            # Compress image to fit under max_size_mb
            while os.path.getsize(output_path) > max_size_mb * 1024 * 1024 and quality > 10:
                quality -= 5
                image.save(output_path, "JPEG", quality=quality)

            print(
                f"Compressed {filename} to {quality}% quality and size: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")


input_folder = '/Users/user/Desktop/jpgs'
output_folder = '/Users/user/Desktop/jpgs/compressed'
compress_images(input_folder, output_folder, max_size_mb=1)
