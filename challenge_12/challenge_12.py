from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import io

def main():
    with open("evil2.gfx", 'rb') as file:
        data = file.read()

    for i in range(5):
        f = data[i::5]
        img = Image.open(io.BytesIO(f))
        img.show()

# five image:
# dis pro port ional ity(be crossed out)


if __name__ == '__main__':
    main()