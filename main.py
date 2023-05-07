from customer import Customer
from rewardFlatCustomer import RewardFlatCustomer
from rewardStepCustomer import RewardStepCustomer
from movie import Movie
from ticket import Ticket
from booking import Booking
from records import Records

# customer1 = Customer(4, 'Ash')
# print(customer1.get_customer_id())
# print(customer1.get_customer_name())
# customer1.display_info()
# #
# customer2 = RewardFlatCustomer(18, 'Mouni')
# print(customer2.get_discount(25))
# print(customer2.get_discount(65))
# print(customer2.customer_id)
# print(customer2.customer_name)
# customer2.display_info()

#
# customer3 = RewardStepCustomer(3, 'Achu')
# print(customer3.get_customer_id())
# print(customer3.get_customer_name())
# print(customer3.get_discount(25))
# print(customer3.get_discount(65))
# customer3.display_info()
#
# movie1 = Movie(1, "Avatar", 50)
# ticket1 = Ticket(1, "adult", 25)
# booking1 = Booking(customer2, movie1, ticket1, 2)
# print(booking1.compute_cost())

record1 = Records()
print(record1.find_ticket('child').ticket_id)