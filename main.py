
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

if __name__ == "__main__":

    path = '/home/renien/projects/cheerbees/process-image/data/stack-overflow.png'
    # Simple image to string
    print(pytesseract.image_to_string(Image.open(path)))