# According to the picture, we know the rule is ascii + 2.

'''
result = ""
f = open("text.txt", "r")
str = f.read()

for i in str:
    if i >= 'a' and i <= 'z':
        temp = chr((ord(i) + 2 - ord('a')) % 26 + ord('a'))
        result += temp
    else:
        result += i
print(result)

Result is "i hope you didnt translate it by hand.
thats what computers are for. doing it in by hand is inefficient and that's why this text is so long.
using string.maketrans() is recommended. now apply on the url."
'''

# try to use maketrans():
import string
f = open("text.txt", "r")
s = f.read()

transtab = str.maketrans(string.ascii_lowercase,
                         string.ascii_lowercase[2:] + string.ascii_letters[:2])
print(s.translate(transtab))

print("map".translate(transtab))    # get "ocr"
