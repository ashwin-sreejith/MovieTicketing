from customer import Customer


class RewardFlatCustomer(Customer):
    """ Class to handle customers in flat rewards program"""

    _DISCOUNT_RATE: float = 0.2

    # Constructor to instantiate objects
    def __init__(self, customer_id, customer_name):
        # invokes constructor of parent class
        super().__init__(customer_id, customer_name)
        self._discount = 0

    # getter for discount rate
    @property
    def discount(self):
        return self._discount

    # setter method for discount rate
    @staticmethod
    def set_discount_rate(discount_rate: float):
        RewardFlatCustomer._DISCOUNT_RATE = discount_rate

    # overrides similar function of parent to calculate discount as 20% of cost
    def get_discount(self, cost: float):
        self._discount = RewardFlatCustomer._DISCOUNT_RATE * cost
        return self._discount

    # overrides display_info method of customer class to print discount rate as well
    def display_info(self):
        print(f"Flat rewards Customer ID : {self._customer_id}, " + f"Customer Name : {self._customer_name}, " +
              f"Discount rate : {RewardFlatCustomer._DISCOUNT_RATE}, " + f"Availed Discount : {self._discount}")

    def to_string(self):
        return f"{self.customer_id}, {self.customer_name}, {RewardFlatCustomer._DISCOUNT_RATE}"
