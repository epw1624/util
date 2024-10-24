import base64
from PIL import Image
from io import BytesIO
import sys

def image_to_base64(filepath):
    with Image.open(filepath) as image:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        bytes = buffered.getvalue()
        base64_encoding = base64.b64encode(bytes).decode('utf-8')
        return base64_encoding
    
if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        raise Exception("Must specify file path")
    
    print(image_to_base64(args[1]))