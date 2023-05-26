from records import Records
from customer import Customer
from movie import Movie
from rewardFlatCustomer import RewardFlatCustomer
from rewardStepCustomer import RewardStepCustomer
from booking import Booking
from error_handler import *


class Operations:
    """Main class to handle all operations"""

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
                  "5: Add movies\n"
                  "6: Adjust the discount rate of a RewardStep customer\n"
                  "7: Adjust the discount rate of all RewardFlat customers\n"
                  "9: Display the most popular movie\n"
                  "10: Display all movie records\n"
                  "0: Exit the program\n"
                  "####################################################################################"
                  )
            choice_mapping = {1: Operations.purchase_ticket,
                              2: Operations.show_existing_customers,
                              3: Operations.show_existing_movies,
                              4: Operations.show_existing_ticket_types,
                              5: Operations.add_movie,
                              6: Operations.adjust_step_discount_rate,
                              7: Operations.adjust_flat_discount_rate,
                              9: Operations.most_popular,
                              10: Operations.disp_movie_records}

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
        ticket_quantity = Operations.check_ticket_quantity(movie_name, len(ticket_type))
        customer_name = Operations.check_customer(customer_name)
        book_tickets = Booking(customer_name, movie_name, ticket_type, ticket_quantity)
        cost_data = book_tickets.compute_cost()
        final_cost = cost_data[0] + cost_data[1] - cost_data[2]
        if movie_name:
            ticket_record = Operations.create_ticket_set(ticket_type, ticket_quantity)
            movie_name.update_ticket_details(ticket_record)
            movie_name.revenue = round(final_cost, 1)
            print(movie_name.ticket_details)
        Operations.show_receipt(customer_name, movie_name, ticket_type, ticket_quantity, cost_data, final_cost)

    @staticmethod
    def create_ticket_set(booked_tickets, quantities):
        ticket_quantity_set = []
        for ticket in Operations._record.existing_ticket_types:
            if ticket not in booked_tickets:
                ticket_quantity_set.append((ticket, 0))
            else:
                ticket_quantity_set.append((ticket, quantities[booked_tickets.index(ticket)]))
        return tuple(ticket_quantity_set)

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
            try:
                # Checks if movie entered exists
                if not is_movie_available:
                    raise MovieNotFoundError
                # Checks if the chosen movie has vacant seats
                elif is_movie_available.seats_available == 0:
                    raise FullyBookedError
                else:
                    # returns the movie name back to the caller
                    return is_movie_available
            except MovieNotFoundError:
                print(f"Sorry! movie {movie_name} not found. Please try again.")
            except FullyBookedError:
                print(f"Sorry {movie_name} is fully booked. Try a different movie!")

    @staticmethod
    def check_ticket_type():
        ticket_obj_list = []
        while True:
            flag = True
            # Accepts ticket type
            ticket_type = input("Enter ticket types : ").strip()
            ticket_list = [ticket.strip() for ticket in ticket_type.split(',')]
            for ticket in ticket_list:
                try:
                    is_ticket_available = Operations._record.find_ticket(ticket)
                    if not is_ticket_available:
                        flag = False
                        ticket_obj_list.clear()
                        raise TicketTypeNotFoundError
                    else:
                        ticket_obj_list.append(is_ticket_available)
                except TicketTypeNotFoundError:
                    print(f"Sorry! ticket type {ticket} not found. Please re-enter!")
            if flag:
                return ticket_obj_list

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
            try:
                if program_code == "S":
                    this_customer = RewardStepCustomer(program_code, customer_name)
                    break
                elif program_code == "F":
                    this_customer = RewardFlatCustomer(program_code, customer_name)
                    break
                else:
                    raise DiscountProgramChoiceError
            except DiscountProgramChoiceError:
                print("Sorry! Please choose between (F - RewardFlatCustomer / S - RewardStepCustomer)")
        if not is_reward:
            this_customer = Customer("C", customer_name)
            print(f"Successfully added {customer_name} to storage")
        else:
            print(f"Successfully added {customer_name} to rewards program")
        Operations._record.add_to_customers(this_customer)
        Operations.save_to_file(this_customer, 'customers.txt')
        return this_customer

    @staticmethod
    def add_customer_to_storage(customer_name: str):
        while True:
            # Prompts user to enter if customer wishes to join the program
            choice = input("Does the customer want to join the rewards program? (Y - YES, N - NO) : ").upper().strip()
            try:
                # If y or Y is chosen
                if choice == 'Y':
                    customer = Operations.add_to_program(customer_name, True)
                    return customer
                elif choice == 'N':
                    customer = Operations.add_to_program(customer_name)
                    return customer
                else:
                    raise DiscountChoiceInputError
            except DiscountChoiceInputError:
                print("Sorry! Please enter 'Y' for YES or 'N' for NO")

    @staticmethod
    def check_ticket_quantity(movie, entry_len):
        quantity_list = []
        while True:
            flag = True
            try:
                quantities = input("Enter the ticket quantities for corresponding ticket types in order separated by "
                                   "commas (Enter only whole numbers) : ")
                quantity_list = [int(quantity.strip()) for quantity in quantities.split(',')]
                for quantity in quantity_list:
                    if len(quantity_list) != entry_len:
                        flag = False
                        raise QuantityTicketTypeMatchError
                    elif quantity == 0 or quantity < 0:
                        flag = False
                        raise InvalidQuantityError
                    elif quantity > movie.seats_available or sum(quantity_list) > movie.seats_available:
                        flag = False
                        raise QuantityExceededError
            except ValueError:
                flag = False
                print("Enter a valid number as ticket quantity")
            except InvalidQuantityError:
                print("Ticket quantity cannot be zero or negative, please enter a valid number!")
            except QuantityExceededError:
                print(f"Sorry! only {movie.seats_available} seats left for {movie.movie_name}")
            except QuantityTicketTypeMatchError:
                print(f"You have entered {entry_len} ticket types but {len(quantity_list)} quantities!")
            if flag:
                movie.seats_available -= sum(quantity_list)
                return quantity_list

    @staticmethod
    def add_movie():
        new_movies = input("Please enter movie names as comma separated names : ").split(',')
        new_movies = [movie.strip() for movie in new_movies]
        for movie in new_movies:
            try:
                if not movie:
                    raise InvalidEntryError
                # available_movie_details updated with only new movies, existing movies are skipped
                elif Operations._record.find_movie(movie):
                    print(f"{movie} already exists in the records hence skipped.")
                else:
                    this_movie = Movie("M", movie, 50)
                    this_movie.ticket_details = {ticket.ticket_name: 0 for ticket in
                                                 Operations._record.existing_ticket_types}
                    Operations._record.add_to_movies(this_movie)
                    print(f"Movie {movie} added successfully!")
            except InvalidEntryError:
                print("Movie entered is empty! Not added")
        print()

    @staticmethod
    def adjust_flat_discount_rate():
        while True:
            try:
                new_disc_rate = float(input("Enter the new discount rate : "))
                if new_disc_rate <= 0 or new_disc_rate >= 1:
                    raise InvalidQuantityError
                else:
                    RewardFlatCustomer.set_discount_rate(new_disc_rate)
                    print(f"Discount Rate for all Reward Flat customers modified to {new_disc_rate}.")
                    return new_disc_rate
            except ValueError:
                print("Enter a valid discount rate! (Eg : 0.2) ")
            except InvalidQuantityError:
                print("Discount rate cannot be zero, negative or greater than or equal to 1!")

    @staticmethod
    def adjust_step_discount_rate():
        customer = ""
        while True:
            try:
                customer = input("Enter the customer ID/Name of the Reward Step Customer : ").strip()
                customer_obj = Operations._record.find_customer(customer)
                if not customer:
                    raise InvalidEntryError
                elif not customer_obj:
                    raise CustomerNotFoundError
                elif not isinstance(customer_obj, RewardStepCustomer):
                    raise NotStepInstanceError
                else:
                    disc_rate = Operations.__accept_step_disc_rate(customer_obj)
                    print(f"Discount Rate for {customer} modified to {disc_rate} successfully!")
                    break
            except InvalidEntryError:
                print("No value entered!")
            except CustomerNotFoundError:
                print(f"{customer} is not customer!")
            except NotStepInstanceError:
                print(f"{customer} is not a Reward Step customer!")
            except AttributeError:
                print("No name or ID entered!")

    @staticmethod
    def __accept_step_disc_rate(customer_obj):
        while True:
            try:
                new_disc_rate = float(input("Enter the new discount rate : "))
                if new_disc_rate <= 0 or new_disc_rate >= 1:
                    raise InvalidQuantityError
                else:
                    customer_obj.discount_rate = new_disc_rate
                    return new_disc_rate
            except ValueError:
                print("Enter a valid discount rate! (Eg : 0.2) ")
            except InvalidQuantityError:
                print("Discount rate cannot be zero, negative or greater than or equal to 1!")

    @staticmethod
    def most_popular():
        print("--------------------------------------------------------------------------------\n"
              "Most popular Movie\n"
              "--------------------------------------------------------------------------------"
              )
        movie, revenue = Operations._record.most_popular_movie()
        print(f"{movie} with total revenue of {revenue}$")
        print()

    @staticmethod
    def disp_movie_records():
        print(" ".ljust(20), end='')
        for ticket in Operations._record.existing_ticket_types:
            print(ticket.ticket_name.center(20), end='')
        print("Revenue".center(20))
        for movie in Operations._record.existing_movies:
            print(movie.movie_name.ljust(20), end='')
            for quantity in movie.ticket_details.values():
                print(str(quantity).center(20), end='')
            print(str(movie.revenue).center(20))
        print()

    @staticmethod
    def show_existing_customers():
        id_mapping = {'C': "Standard",
                      'F': "Flat Rewards",
                      'S': "Step Rewards"}
        print("-" * 205)
        print("Customer Database".center(200))
        print("-" * 205)
        print("Rewards Program".center(40) + "|" + "Customer ID".center(40) + "|" + "Customer Name".center(40) + "|" +
              "Discount Rate".center(40) + "|" + "Threshold Rate".center(40) + "|")
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
    def show_receipt(customer, movie: Movie, ticket_type: list, ticket_quantity: list, cost_data: tuple,
                     total_cost: float):
        print("--------------------------------------------------------------------------------\n"
              f"Receipt of {customer.customer_name.capitalize()}\n"
              "--------------------------------------------------------------------------------"
              )
        print("Movie:".ljust(40) + movie.movie_name.rjust(40))
        for ticket, quantity in zip(ticket_type, ticket_quantity):
            print("Ticket Type:".ljust(40) + ticket.ticket_name.rjust(40))
            print("Ticket Unit-price:".ljust(40) + str(ticket.ticket_price).rjust(40))
            print("Ticket Quantity:".ljust(40) + str(quantity).rjust(40))
        print("--------------------------------------------------------------------------------")
        print("Discount:".ljust(40) + str(round(cost_data[2], 1)).rjust(40))
        print("Booking Fee:".ljust(40) + str(cost_data[1]).rjust(40))
        print("Total Cost:".ljust(40) + str(round(total_cost, 1)).rjust(40))
        print()
