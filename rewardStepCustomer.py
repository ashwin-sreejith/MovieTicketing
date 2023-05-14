from customer import Customer


class RewardStepCustomer(Customer):
    """ Class to handle customers in step rewards program"""

    _THRESHOLD: float = 50

    # Constructor to instantiate the objects
    def __init__(self, customer_id, customer_name):
        # Invokes parent constructor
        super().__init__(customer_id, customer_name)
        self.discount_rate = 0.3
        self._discount = 0

    # getter for discount rate
    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate: float):
        self._discount_rate = float(discount_rate)

    # getter for current threshold
    @staticmethod
    def get_threshold():
        return RewardStepCustomer._THRESHOLD

    # setter for threshold value
    @staticmethod
    def set_threshold(threshold: float):
        RewardStepCustomer._THRESHOLD = float(threshold)

    # Calculates discount as per cost of purchase
    def get_discount(self, cost: float):
        self._discount = self._discount_rate * cost if cost >= RewardStepCustomer._THRESHOLD else 0
        return self._discount

    def display_info(self):
        print(f"Step rewards Customer ID : {self._customer_id}, " + f"Customer Name : {self._customer_name}, " +
              f"Discount rate : {self._discount_rate}, " + f"Threshold : {RewardStepCustomer._THRESHOLD}, " +
              f"Availed Discount : {self._discount}")

    def to_string(self):
        return f"{self.customer_id}, {self.customer_name}, {self.discount_rate}, {RewardStepCustomer._THRESHOLD}"
