import urllib.request
import re

# get the source code
def get_code(url):
    html = urllib.request.urlopen(url)
    source_code = html.read()
    return source_code.decode('utf-8')

def find_num(str):
    rule = r'[0-9]+'
    pattern = re.compile(rule)
    result = pattern.findall(str)
    return result

def main():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    #num = "12345"
    #num = "8022"
    num = "63579"
    str = get_code(url+num)
    while 1:
        num = find_num(str)
        str = get_code(url+num[0])
        print("num = %s" %num[0])
        print("contxet: %s" %str)

if __name__ == '__main__':
    main()

'''
first time:
    num = 16044
    contxet: Yes. Divide by two and keep going.


second time:
    num = 82683
    contxet: You've been misleaded to here. Go to previous 
    one and check.
previous:
    num = 82682
    contxet: There maybe misleading numbers in the 
    text. One example is 82683. Look only for the next nothing and the next nothing is 63579

last time:
num = 66831
contxet: peak.html
'''