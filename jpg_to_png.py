from PIL import Image
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        raise Exception("Must select at least one file")
    
    for arg in args[1:]:
        img = Image.open(arg)
        new_name = arg.replace('jpg', 'png')
        img.save(new_name)
        img.close()


