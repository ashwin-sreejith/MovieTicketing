from customer import Customer


class RewardFlatCustomer(Customer):
    """ Class to handle customers in flat rewards program"""

    # Constructor to instantiate objects
    def __init__(self, customer_id, customer_name):
        # invokes constructor of parent class
        super().__init__(customer_id, customer_name)
        self._discount_rate = 0.2
        self._discount = 0

    # getter for discount rate
    def get_discount_rate(self):
        return self._discount_rate

    # setter method for discount rate
    def set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    # overrides similar function of parent to calculate discount as 20% of cost
    def get_discount(self, cost):
        self._discount = self._discount_rate * cost
        return self._discount

    # overrides display_info method of customer class to print discount rate as well
    def display_info(self):
        print(f"Flat rewards Customer ID : {self._customer_id}, " + f"Customer Name : {self._customer_name}, " +
              f"Discount rate : {self._discount_rate}, " + f"Availed Discount : {self._discount}")

    # Other getter methods for customer name and ID are not overridden in this class as there is no modifications to be
    # made to those functions. Since the child already inherits those functions from the parent, they can be accessed
    # using the child object
    # If needed the following implementations can be done :
    #
    #     def get_customer_name(self):
    #         return super().get_customer_name()
    #
    #     def get_customer_id(self):
    #         return super().get_customer_id()
