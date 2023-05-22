class Customer:
    """ Customer parent class, handles all customer-centric computing"""

    _CUSTOMER_ID_COUNT: int = 0

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
        self._customer_name = customer_name.capitalize().strip()

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if len(customer_id) > 1:
            self._customer_id = customer_id
        else:
            self._customer_id = customer_id + str(Customer._CUSTOMER_ID_COUNT)
            Customer._CUSTOMER_ID_COUNT += 1

    # calculates discount for customer
    def get_discount(self, cost: float):
        return 0

    # calculates booking fee for customer
    @staticmethod
    def get_booking_fee(ticket_quantity: int):
        return 2 * ticket_quantity

    @staticmethod
    def get_customer_id_count():
        return Customer._CUSTOMER_ID_COUNT

    @staticmethod
    def set_customer_id_count(customer_id_number: int):
        Customer._CUSTOMER_ID_COUNT = customer_id_number

    # displays customer information
    def display_info(self):
        print(f"Customer ID : {self._customer_id}, " + f"Customer Name : {self._customer_name}, Discount : 0")

    def to_string(self):
        return f"{self.customer_id}, {self.customer_name}"
