from PIL import Image
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 1:
        raise Exception("Must select at least one file")
    
    for arg in args[1:]:
        img = Image.open(arg)
        new_name = arg.replace('png', 'jpg')
        img.save(new_name)
        img.close()