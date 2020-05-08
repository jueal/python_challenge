# click the bull
# a = [1, 11, 21, 1211, 111221, and len(a[30]) = ?
import string

def count(number):
    result = ""
    s = number[0]
    num = 0
    for i in number:
        if i == s:
            num += 1
        else:
            result += str(num)
            result += s
            num = 1
            s = i
    result += str(num)
    result += s
    print(len(result))
    return result

def main():
    number = count("1")
    for i in range(1, 30):
        print("%d :" %i, end="")
        number = count(number)
# 5808

if __name__ == '__main__':
    main()
