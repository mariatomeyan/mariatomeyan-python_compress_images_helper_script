# Image Compression Script README

This Python script compresses images in a specified input folder and saves the compressed images to an output folder. The script reduces the image file sizes by adjusting the JPEG quality, ensuring that each file does not exceed a specified maximum size (default is 1 MB).

# Features
Bulk Compression: Compresses all .png, .jpg, and .jpeg images in the input folder.
Quality Adjustment: Automatically adjusts JPEG quality to meet the desired maximum file size.
Easy Configuration: Simple variables to set input/output directories and maximum file size.
Progress Reporting: Prints out the compression details for each image processed.
Requirements
Python 3.x

# Pillow Library: An image processing library for Python.

# Install Pillow using pip:

bash
Copy code
pip install Pillow
Usage
Clone or Download the Script

Save the script to your local machine with a .py extension, e.g., compress_images.py.

Set the Input and Output Folders

Modify the input_folder and output_folder variables in the script to point to your directories:

python
Copy code
> input_folder = '/path/to/your/input_folder'
> output_folder = '/path/to/your/output_folder'
> Set the Maximum File Size (Optional)

By default, the script sets the maximum file size to 1 MB. You can change this by modifying the max_size_mb parameter:

python
Copy code
> compress_images(input_folder, output_folder, max_size_mb=1)
Run the Script

Open a terminal, navigate to the directory containing the script, and run:

> bash
Copy code
> python compress_images.py
