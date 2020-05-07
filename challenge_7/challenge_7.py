# the result of previous challenge is hockey.
# "it's in the air. look at the letters."
# so, find 'oxygen'. replace hockey with oxygen.

from PIL import Image

def main():
    image = Image.open("oxygen.png")
    rgb_image = image.convert('RGB')
    x, y = image.size
    result = ""
    for i in range(0, 607, 7):
        num = rgb_image.getpixel((i, 43))[0]
        result += chr(num)
    print(result) #get 'smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]'

    my_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    next = ""
    for i in my_list:
        next += chr(i)
    print(next) # get 'integrity'

'''
    for i in range(0, x):
        for j in range(0, y):
            r, g, b = rgb_image.getpixel((i, j))
            print((i, j), (r, g, b))
# print rgb, find x=0~607, y=43~51 is different
'''

if __name__ == '__main__':
    main()


