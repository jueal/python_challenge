from PIL import Image

def main():
    image = Image.open("cave.jpg")
    width, height = image.size
    new_img_1 = Image.new(image.mode, (width // 2, height // 2))
    new_img_2 = Image.new(image.mode, (width // 2, height // 2))
    for x in range(0, width):
        for y in range(0, height):
            if (x + y) % 2 == 0:
                new_img_1.putpixel((x // 2, y // 2), image.getpixel((x, y)))
            else:
                new_img_2.putpixel((x // 2, y // 2), image.getpixel((x, y)))
    new_img_1.show()
    new_img_2.show()
    # evil
if __name__ == '__main__':
    main()