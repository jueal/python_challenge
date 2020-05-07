# right click -> view source code
# find rare characters in the mess below:
# so, count the number of character occurrences.

from collections import Counter
f = open("mess.txt", "r")
str = f.read()
print(Counter(str))

# find 'equality'