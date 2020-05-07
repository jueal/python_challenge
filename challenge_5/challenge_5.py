import pickle
import urllib

def get_code(url):
    html = urllib.request.urlopen(url)
    source_code = html.read()
    return source_code

def main():
    url = "http://www.pythonchallenge.com/pc/def/banner.p"
    urllib.request.urlretrieve(url, filename = 'banner.pkl')
    with open("banner.pkl", 'rb') as fp:
        result = pickle.load(fp)

    for i in result:
        for j in i:
            print(j[0] * j[1], end="")
        print("\n")
# channel

if __name__ == '__main__':
    main()