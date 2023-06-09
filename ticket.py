class Ticket:
    """Class to handle tickets"""

    def __init__(self, ticket_id, ticket_name, ticket_price=0.0):
        self.ticket_id = ticket_id
        self.ticket_name = ticket_name
        self.ticket_price = ticket_price

    @property
    def ticket_name(self):
        return self._ticket_name

    @ticket_name.setter
    def ticket_name(self, ticket_name):
        self._ticket_name = ticket_name

    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        self._ticket_id = ticket_id

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, ticket_price):
        self._ticket_price = float(ticket_price)

    def display_info(self):
        print(self.ticket_id.center(40) + "|" + self.ticket_name.center(40) + "|"
              + str(self.ticket_price).center(40))
