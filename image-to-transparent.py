from PIL import Image
import os
import sys

def convert_white_to_transparent(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path).convert("RGBA")

            old_pixels = img.getdata()
            new_pixels = []

            for pixel in old_pixels:
                if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                    new_pixels.append((255, 255, 255, 0))
                else:
                    new_pixels.append(pixel)

            img.putdata(new_pixels)

            output_path = os.path.join(output_folder, filename)
            img.save(output_path, "PNG")

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 3:
        raise Exception("Must specify an input folder path and output folder path")
    
    convert_white_to_transparent(args[1], args[2])
