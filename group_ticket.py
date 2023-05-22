from ticket import Ticket


class GroupTicket(Ticket):

    def __init__(self, ticket_id, ticket_name, ticket_price, tickets):
        super().__init__(ticket_id, ticket_name, ticket_price)
        self.ticket_components = tickets

    @property
    def ticket_components(self):
        return self._ticket_components

    @ticket_components.setter
    def ticket_components(self, component: dict):
        self._ticket_components = component




