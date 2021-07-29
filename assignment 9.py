class Car:

    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def get_year(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

def main():
    make = input("What is the make of the car? ")
    year = input("What is the year of the model? ")

    my_car = Car(year, make)

    print("Make: " + my_car.get_make())
    print("Year: " + my_car.get_year())

    for x in range(5):
        my_car.accelerate()
        print("Speed =", my_car.get_speed())

    for x in range(5):
        my_car.brake()
        print("Speed =", my_car.get_speed())

main()