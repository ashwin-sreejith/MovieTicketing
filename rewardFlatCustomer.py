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
        RewardFlatCustomer._DISCOUNT_RATE = float(discount_rate)

    # overrides similar function of parent to calculate discount as 20% of cost
    def get_discount(self, cost: float):
        self._discount = RewardFlatCustomer._DISCOUNT_RATE * cost
        return self._discount

    # overrides display_info method of customer class to print discount rate as well
    def display_info(self):
        print("Flat Rewards".center(40) + "|" + f"{self.customer_id}".center(40) + "|" +
              f"{self.customer_name}".center(40) + "|" + f"{RewardFlatCustomer._DISCOUNT_RATE}".center(40) +
              "|" + "0.0".center(40))

    def to_string(self):
        return f"{self.customer_id}, {self.customer_name}, {RewardFlatCustomer._DISCOUNT_RATE}"
