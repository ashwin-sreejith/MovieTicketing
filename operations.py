from records import Records
from customer import Customer
from rewardFlatCustomer import RewardFlatCustomer
from rewardStepCustomer import RewardStepCustomer
from booking import Booking


class Operations:
    """Main class to handle all operations"""

    _customer_id_count: int = 12
    _record = Records()

    def __init__(self):
        self.show_menu()

    @staticmethod
    def show_menu():
        while True:
            print("Welcome to RMIT movie ticketing system!\n"
                  "####################################################################################\n"
                  "You can choose from the following options:\n"
                  "1: Purchase a ticket\n"
                  "2: Display existing customers' information\n"
                  "3: Display existing movies' information\n"
                  "4: Display existing ticket types' information\n"
                  "0: Exit the program\n"
                  "####################################################################################"
                  )
            choice_mapping = {1: Operations.purchase_ticket,
                              2: Operations.show_existing_customers,
                              3: Operations.show_existing_movies,
                              4: Operations.show_existing_ticket_types}

            try:
                choice = int(input("Choose one option : "))
                choice_function = choice_mapping.get(choice)
                if choice == 0:
                    break
                elif choice_function is None:
                    print("Invalid choice! Please choose a valid option.")
                else:
                    choice_function()
            except ValueError:
                print("Please choose a number as shown in the menu!")

    @staticmethod
    def purchase_ticket():
        customer_name = input("Enter the customer name : ").strip().upper()
        movie_name = Operations.check_movie()
        ticket_type = Operations.check_ticket_type()
        ticket_quantity = Operations.check_ticket(movie_name)
        customer_name = Operations.check_customer(customer_name)
        book_tickets = Booking(customer_name, movie_name, ticket_type, ticket_quantity)
        cost_data = book_tickets.compute_cost()
        final_cost = cost_data[0] + cost_data[1] - cost_data[2]
        Operations.show_receipt(customer_name, movie_name, ticket_type, ticket_quantity, cost_data, final_cost)

    @staticmethod
    def check_customer(customer_name: str):
        is_customer_available = Operations._record.find_customer(customer_name)
        if not is_customer_available:
            customer = Operations.add_customer_to_storage(customer_name)
            return customer
        else:
            return is_customer_available

    # function to accept movie name from user
    @staticmethod
    def check_movie():
        # while loop used to generate an infinite loop until a correct movie name is entered
        while True:
            # Accepts movie name from user
            movie_name = input("Enter the movie name : ").strip()
            is_movie_available = Operations._record.find_movie(movie_name)
            # Checks if movie entered exists
            if not is_movie_available:
                print(f"Sorry! movie {movie_name} not found. Please try again.")
                # Checks if the chosen movie has vacant seats
            elif is_movie_available.seats_available == 0:
                print(f"Sorry {movie_name} is fully booked. Try a different movie!")
            else:
                # returns the movie name back to the caller
                return is_movie_available

    # function to accept ticket type from user
    @staticmethod
    def check_ticket_type():
        while True:
            # Accepts ticket type
            ticket_type = input("Enter a ticket type : ").strip()
            is_ticket_available = Operations._record.find_ticket(ticket_type)
            if not is_ticket_available:
                print(f"Sorry! ticket type {ticket_type} not found.")
            else:
                return is_ticket_available

    @staticmethod
    def save_to_file(obj, filepath: str = "./COSC2531_Assignment2_txtfiles/"):
        try:
            with open(filepath, 'a') as file:
                file.write("\n" + obj.to_string())
        except FileNotFoundError:
            print("Error : File not found!")

    @staticmethod
    def add_to_program(customer_name: str, is_reward: bool = False):
        this_customer = None
        while is_reward:
            program_code = input("Choose the discount program (F - RewardFlatCustomer, S - RewardStepCustomer) : "). \
                upper().strip()
            if program_code == "S":
                this_customer = RewardStepCustomer(program_code + str(Operations._customer_id_count), customer_name)
                Operations._customer_id_count += 1
                break
            elif program_code == "F":
                this_customer = RewardFlatCustomer(program_code + str(Operations._customer_id_count), customer_name)
                Operations._customer_id_count += 1
                break
            else:
                print("Sorry! Please choose between (F - RewardFlatCustomer / S - RewardStepCustomer)")
        if not is_reward:
            this_customer = Customer("C" + str(Operations._customer_id_count), customer_name)
            Operations._customer_id_count += 1
        Operations._record.add_to_customers(this_customer)
        Operations.save_to_file(this_customer, 'customers.txt')
        return this_customer

    @staticmethod
    def add_customer_to_storage(customer_name: str):
        while True:
            # Prompts user to enter if customer wishes to join the program
            choice = input("Does the customer want to join the rewards program? (Y - YES, N - NO) : ").upper().strip()
            # If y or Y is chosen
            if choice == 'Y':
                customer = Operations.add_to_program(customer_name, True)
                return customer
            elif choice == 'N':
                customer = Operations.add_to_program(customer_name)
                return customer
            else:
                print("Sorry! Please enter 'Y' for YES and 'N' for NO")

    @staticmethod
    def check_ticket(movie):
        while True:
            try:
                quantity = int(input("Enter the ticket quantity (Enter only whole numbers) : "))
                if quantity == 0 or quantity < 0:
                    print("Ticket quantity cannot be zero or negative, please enter a valid number!")
                else:
                    break
            except ValueError:
                print("Enter a valid number as ticket quantity")
        if quantity > movie.seats_available:
            print(f"Sorry! only {movie.seats_available} seats left for {movie.movie_name}")
        else:
            movie.seats_available -= quantity
            return quantity

    @staticmethod
    def show_existing_customers():
        id_mapping = {'C': "Standard",
                      'F': "Flat Rewards",
                      'S': "Step Rewards"}
        print("-" * 205)
        print("Customer Database".center(200))
        print("-" * 205)
        print("Rewards Program".center(40) + "|" + "Customer ID".center(40) + "|" + "Customer Name".center(40) + "|" +
              "Discount Rate".center(40) + "|" + "Threshold Rate".center(40))
        print("-" * 205)
        for customer in Operations._record.existing_customers:
            customer_data = customer.to_string().split(',')
            reward_program = id_mapping.get(customer_data[0][0])
            if reward_program == "Standard":
                customer_data += [0, 0]
            elif reward_program == "Flat Rewards":
                customer_data += [0]
            print(reward_program.center(40), end="|")
            for index in range(len(customer_data)):
                print(str(customer_data[index]).center(40), end="|")
            print()
        print()

    @staticmethod
    def show_existing_movies():
        print("-" * 120)
        print("Movie Database".center(120))
        print("-" * 120)
        print("Movie ID".center(40) + "|" + "Movie Name".center(40) + "|" + "Available Seats".center(40))
        print("-" * 120)
        for movie in Operations._record.existing_movies:
            print(movie.movie_id.center(40) + "|" + movie.movie_name.center(40) + "|"
                  + str(movie.seats_available).center(40))
        print()

    @staticmethod
    def show_existing_ticket_types():
        print("-" * 120)
        print("Ticket Type Database".center(120))
        print("-" * 120)
        print("Ticket ID".center(40) + "|" + "Ticket Type".center(40) + "|" + "Ticket price".center(40))
        print("-" * 120)
        for ticket in Operations._record.existing_ticket_types:
            print(ticket.ticket_id.center(40) + "|" + ticket.ticket_name.center(40) + "|"
                  + str(ticket.ticket_price).center(40))
        print()

    @staticmethod
    def show_receipt(customer, movie, ticket_type, ticket_quantity: int, cost_data: tuple, total_cost: float):
        print("--------------------------------------------------------------------------------\n"
              f"Receipt of {customer.customer_name.capitalize()}\n"
              "--------------------------------------------------------------------------------"
              )
        print("Movie:".ljust(40) + movie.movie_name.rjust(40))
        print("Ticket Type:".ljust(40) + ticket_type.ticket_name.rjust(40))
        print("Ticket Unit-price:".ljust(40) + str(ticket_type.ticket_price).rjust(40))
        print("Ticket Quantity:".ljust(40) + str(ticket_quantity).rjust(40))
        print("--------------------------------------------------------------------------------")
        print("Discount:".ljust(40) + str(round(cost_data[2], 1)).rjust(40))
        print("Booking Fee:".ljust(40) + str(cost_data[1]).rjust(40))
        print("Total Cost:".ljust(40) + str(round(total_cost, 1)).rjust(40))


