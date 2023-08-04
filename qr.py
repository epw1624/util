import qrcode
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 3:
        raise Exception("must pass exactly two arguments: a link and a name for the qr code file")
    
    img = qrcode.make(args[1])
    img_name = args[2] + ".png"

    img.save(img_name)

