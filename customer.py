

class Customer:
    """ Customer parent class, handles all customer-centric computing"""

    # Constructor to instantiate the objects
    def __init__(self, customer_id, customer_name):
        # attributes are non-public
        self._customer_name = None
        self._customer_id = customer_id
        self._set_name(customer_name)

    # processes the input customer_name before initialising the customer name attribute of the object
    def _set_name(self, name):
        self._customer_name = name.upper().strip()

    # Getter method for customer name
    def get_customer_name(self):
        return self._customer_name

    # Getter method for customer ID
    def get_customer_id(self):
        return self._customer_id

    # calculates discount for customer
    def get_discount(self, cost):
        return 0

    # calculates booking fee for customer
    def get_booking_fee(self, ticket_quantity):
        return 2 * ticket_quantity

    # displays customer information
    def display_info(self):
        print(f"Customer ID : {self._customer_id}\n" + f"Customer Name : {self._customer_name}")



