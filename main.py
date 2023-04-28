from customer import Customer
from rewardFlatCustomer import RewardFlatCustomer
from rewardStepCustomer import RewardStepCustomer

customer1 = Customer(4, 'Ash')
print(customer1.get_customer_id())
print(customer1.get_customer_name())
customer1.display_info()

customer2 = RewardFlatCustomer(18, 'Mouni')
print(customer2.get_discount(25))
print(customer2.get_discount(65))
print(customer2.get_customer_id())
print(customer2.get_customer_name())
customer2.display_info()

customer3 = RewardStepCustomer(3, 'Achu')
print(customer3.get_customer_id())
print(customer3.get_customer_name())
print(customer3.get_discount(25))
print(customer3.get_discount(65))
customer3.display_info()


