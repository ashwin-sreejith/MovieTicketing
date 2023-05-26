class Booking:
    """Class to handle booking details for customers"""

    def __init__(self, customer, movie, ticket_type, ticket_quantity):
        self._customer = customer
        self._movie = movie
        self._ticket_type = ticket_type
        self._ticket_quantity = ticket_quantity
        self.__ticket_cost = 0

    def compute_cost(self) -> tuple:
        """Computes all cost values including total cost, booking fee and discounts and returns a tuple"""
        for ticket, quantity in zip(self._ticket_type, self._ticket_quantity):
            self.__ticket_cost += ticket.ticket_price * quantity
        booking_fee = self._customer.get_booking_fee(sum(self._ticket_quantity))
        discount = self._customer.get_discount(self.__ticket_cost)
        return self.__ticket_cost, booking_fee, discount

