from parking_ticket import ParkingTicket
from datetime import datetime
from datetime import timedelta
import random

class ParkingMachine:
    def __init__(self):
        return

    def create_ticket(self):
        new_ticket = ParkingTicket()
        return new_ticket

    def print_ticket(self, parking_lot, license_number, ticket):
        
        company_name = parking_lot.get_company_name()
        rate = parking_lot.get_rate()
        updated_ticket = self.__calculate_payment(rate, ticket)
        start_time = ticket.get_created_at()
        end_time = updated_ticket.get_payed_at()
        payment = updated_ticket.get_payment()

        ticket_info = """
        🚗 {company}
        ------------------
        License Plate: {license}
        From: {start}
        To: {end}
        Rate: Bs. {rate}
        ------------------
        Paid: Bs. {payment}
        """.format(company=company_name, 
        license=license_number, 
        start=start_time, 
        end=end_time,
        rate=rate,
        payment=payment)
        print(ticket_info)
        return

    def __calculate_payment(self, rate, ticket):
        ticket_start_time = ticket.get_created_at()
        ticket_end_time = datetime.now()

        # get random value for minutes passed between 60 to 300 minutes
        minutes_passed = random.randint(60, 300)
        # print("Minutes passed: [{}]".format(minutes_passed))
        ticket_end_time = ticket_end_time + timedelta(minutes=minutes_passed)

        # print("Start time: [{}]".format(ticket_start_time))
        # print("End time: [{}]".format(ticket_end_time))
        delta = ticket_end_time - ticket_start_time
        # print("delta")
        # print(delta)
        total_minutes_passed = int(delta.total_seconds() / 60)

        rate_per_minute = rate / 60

        payment = round(rate_per_minute * total_minutes_passed, 2)
        # print ("Total payment: [{}]".format(payment))

        ticket.set_payment(payment)
        ticket.set_payed_at(ticket_end_time)

        return ticket