class Booking:
    """Class to handle booking details for customers"""

    def __init__(self, customer, movie, ticket_type, ticket_quantity):
        self._customer = customer
        self._movie = movie
        self._ticket_type = ticket_type
        self._ticket_quantity = ticket_quantity

    def compute_cost(self) -> tuple:
        """Computes all cost values including total cost, booking fee and discounts and returns a tuple"""
        ticket_cost = self._ticket_type.ticket_price * self._ticket_quantity
        booking_fee = self._customer.get_booking_fee(self._ticket_quantity)
        discount = self._customer.get_discount(ticket_cost)
        return ticket_cost, booking_fee, discount

