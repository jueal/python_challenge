import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
f = urllib.request.urlopen(url)
str = f.read()
str = str.decode('utf-8')

# use re
pattern = re.compile(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
find = pattern.findall(str)

result = ""
for letter in find:
    result += letter[4]
print(result)   # find 'linkedlist'