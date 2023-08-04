
import sys
from PyPDF2 import PdfMerger

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        raise Exception("You must select at least 2 documents to combine")
    
    result = PdfMerger()
    
    for pdf in args[1:]:
        result.append(pdf)

    result.write("combined.pdf")
    result.close()
