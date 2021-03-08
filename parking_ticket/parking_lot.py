from parking_machine import ParkingMachine
from car import Car

class ParkingLot:
    def __init__(self, rate):
        self.__rate = rate; # rate per hour
        self.__company_name = "~~ New Company ~~"
        self.__machine = ParkingMachine()
        self.__car_list = []
        # return

    def get_rate(self):
        return self.__rate

    def get_company_name(self):
        return self.__company_name

    def register_car(self):
        print("[+] Enter your license number:")
        license_number = input()
        new_car = Car(license_number)

        new_ticket = self.__machine.create_ticket()

        new_car.assign_ticket(new_ticket)
        self.__car_list.append(new_car)

        car_count = len(self.__car_list)
        print("Number of cars in the parking: [{}]".format(car_count))
        return

    def process_car(self):
        print("[+] Enter your license number:")
        license_number = input()
        car = self.__find_car(license_number)
        car_ticket = car.get_ticket()

        self.__machine.print_ticket(self, license_number, car_ticket)

        return

    def __find_car(self, license_number):
        for car in self.__car_list:
            if (car.get_license_number() == license_number):
                return car

# Main #
# def main():
parking_lot = ParkingLot(7)
while(True):
    message = """
    Select an option:
    1. Enter parking
    2. Leave parking
    3. Exit machine
    """
    print(message)
    input_option = input()
    if (input_option == "1"):
        parking_lot.register_car()
    elif (input_option == "2"):
        parking_lot.process_car()
    elif (input_option == "3"):
        exit()
    else:
        print("Option not supported")
