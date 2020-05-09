import xmlrpc.client


def main():
    with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
        print(proxy.system.listMethods()) # 'phone'
        print(proxy.system.methodHelp("phone")) # 'Returns the phone of a person'
        print(proxy.system.methodSignature("phone")) # "[['string', 'string']]"
        print(proxy.phone('Bert')) # '555-ITALY'


if __name__ == '__main__':
    main()


# https://blog.csdn.net/weicao1990/article/details/80066655
'''
use wget http://www.pythonchallenge.com/pc/return/evil4.jpg --user huge --password file
download the evil4.jpg, and cat evil4.jpg
get 'Bert is evil! go back!'
so, phone Bert!
'''