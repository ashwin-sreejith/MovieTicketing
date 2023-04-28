from customer import Customer
from rewardFlatCustomer import RewardFlatCustomer

customer1 = Customer(4, 'Ash')
print(customer1.get_customer_id())
print(customer1.get_customer_name())
customer1.display_info()

customer2 = RewardFlatCustomer(18, 'Mouni')
print(customer2.get_customer_id())
print(customer2.get_customer_name())
customer2.display_info()

