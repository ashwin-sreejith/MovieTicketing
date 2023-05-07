class Ticket:
    """Class to handle tickets"""

    def __init__(self, ticket_id, ticket_name, ticket_price):
        self._ticket_id = ticket_id
        self._ticket_name = ticket_name
        self._ticket_price = ticket_price

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, ticket_price):
        self._ticket_price = ticket_price

    def display_info(self):
        print(f"Ticket ID : {self._ticket_id}\n" + f"Ticket Name : {self._ticket_name}\n" +
              f"Ticket price : {self._ticket_price}")

