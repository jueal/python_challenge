import zipfile
import os
import re

def find_result(zipname):
    file_dict = dict()
    with zipfile.ZipFile(zipname) as zip:
        filename = zip.namelist()
        for name in filename:
            with zip.open(name) as file:
                file_dict[name] = file.read()

    num = "90052"
    name = num + ".txt"
    while True:
        try:
            str = file_dict[name].decode('utf-8')
        except:
            break
        #print(str)
        print(zip.getinfo(name).comment.decode('utf-8'), end="")
        pattern = re.compile(r'[0-9]+')
        num = pattern.findall(str)
        name = "".join(num) + ".txt"
        #print(name)
    '''
    Next nothing is 46145
    get 'collect the comments'
    '''

def main():
    zipname = "channel.zip"
    find_result(zipname)
    # get 'hockey'

if __name__ == '__main__':
    main()