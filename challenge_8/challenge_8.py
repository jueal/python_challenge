import bz2

def translate(str):
    return bz2.decompress(str)
# bzip2 algorithm

def main():
    str1 = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    str2 = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    un = translate(str1)
    pw = translate(str2)
    print(un)
    print(pw)

if __name__ == '__main__':
    main()