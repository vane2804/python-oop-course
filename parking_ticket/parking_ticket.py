import uuid
from datetime import datetime

class ParkingTicket:
    def __init__(self):
        self.__ticket_number =  uuid.uuid4()
        self.__created_at = datetime.now()
        self.__payed_at = ""
        self.__payment = ""
        return

    def set_ticket_number(self):
        self.__ticket_number = uuid.uuid4()

    def set_created_at(self):
        self.__created_at = datetime.now()

    def set_payed_at(self, new_end_date):
        self.__payed_at = new_end_date

    def set_payment(self, new_payment):
        self.__payment = new_payment

    def get_ticket_number(self):
        return self.__ticket_number

    def get_created_at(self):
        return self.__created_at

    def get_payed_at(self):
        return self.__payed_at

    def get_payment(self):
        return self.__payment


