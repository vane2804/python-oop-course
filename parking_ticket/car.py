class Car:

    def __init__(self, license_number):
        self.__license_number = license_number
        self.__ticket = None
        return

    def assign_ticket(self, ticket):
        self.__ticket = ticket

    def get_license_number(self):
        return self.__license_number

    def get_ticket(self):
        return self.__ticket