from customer import Customer


class RewardStepCustomer(Customer):
    """ Class to handle customers in step rewards program"""
    # Constructor to instantiate the objects
    def __init__(self, customer_id, customer_name):
        # Invokes parent constructor
        super().__init__(customer_id, customer_name)
        self._discount_rate = 0.3
        self._threshold = 50
        self._discount = 0

    # getter for discount rate
    def get_discount_rate(self):
        return self._discount_rate

    # getter for current threshold
    def get_threshold(self):
        return self._threshold

    # setter for discount rate
    def set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    # setter for threshold value
    def set_threshold(self, threshold):
        self._threshold = threshold

    # Calculates discount as per cost of purchase
    def get_discount(self, cost):
        self._discount = self._discount_rate * cost if cost >= self._threshold else 0
        return self._discount

    def display_info(self):
        print(f"Step rewards Customer ID : {self._customer_id}, " + f"Customer Name : {self._customer_name}, " +
              f"Discount rate : {self._discount_rate}, " + f"Threshold : {self._threshold}, " +
              f"Availed Discount : {self._discount}")
