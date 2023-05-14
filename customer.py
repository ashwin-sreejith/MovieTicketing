
class Customer:
    """ Customer parent class, handles all customer-centric computing"""

    # Constructor to instantiate the objects
    def __init__(self, customer_id, customer_name):
        # attributes are non-public
        self.customer_name = customer_name
        self.customer_id = customer_id

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name.upper().strip()

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    # calculates discount for customer
    def get_discount(self, cost: float):
        return 0

    # calculates booking fee for customer
    @staticmethod
    def get_booking_fee(ticket_quantity: int):
        return 2 * ticket_quantity

    # displays customer information
    def display_info(self):
        print(f"Customer ID : {self._customer_id}, " + f"Customer Name : {self._customer_name}, Discount : 0")

    def to_string(self):
        return f"{self.customer_id}, {self.customer_name}"
