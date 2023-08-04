# util
various scripts I use frequently <br><br>

### pdf_combine.py <br>
combines any number of pdf files by appending them to each other in order<br>
**Dependencies:**<br>
PyPDF2 3.0.1<br>
**To Run:**<br>
python pdf_combine.py filename1.pdf filename2.pdf filename3.pdf

### jpg_to_png.py <br>
takes a jpg image and creates a new file in png format<br>
only takes the name of the jpg file as an argument, the png file will automatically be given the same name with a .png extension<br>
**Dependencies:**<br>
Pillow 9.2.0<br>
**To Run:**<br>
python jpg_to_png.py img.jpg

### png_to_jpg.py <br>
takes a png image and creates a new file in jpg format<br>
only takes the name of the png file as an argument, the jpg file will automatically be given the same name with a .jpg extension<br>
**Dependencies:**<br>
Pillow 9.2.0<br>
**To Run:**<br>
python png_to_jpg.py img.png

### qr.py <br>
generate a QR code from a given link<br>
the QR code will be a png file with the filename specified as an argument<br>
**Dependencies:**<br>
qrcode 7.4.2<br>
**To Run:**<br>
python qr.py url filename

