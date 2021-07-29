class Information:

    def __init__(self):
        self.__name = ""
        self.__address = ""
        self.__age = 0
        self.__number = ""

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_number(self):
        return self.__number

def main():
    my_info = Information()
    friend_info = Information()
    family_info = Information()

    name = input("Enter your name:")
    my_info.set_name(name)
    print (my_info.get_name())

main()