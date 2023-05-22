from rewardStepCustomer import RewardStepCustomer
from rewardFlatCustomer import RewardFlatCustomer
from customer import Customer
from movie import Movie
from ticket import Ticket
from group_ticket import GroupTicket
from error_handler import *


class Records:
    """Class to handle database"""

    def __init__(self):
        self.existing_customers = []
        self.existing_movies = []
        self.existing_ticket_types = []
        self.read_customer()
        self.read_movies()
        self.read_tickets()

    @property
    def existing_customers(self):
        return self._existing_customers.copy()

    @existing_customers.setter
    def existing_customers(self, customers):
        self._existing_customers = customers

    @property
    def existing_movies(self):
        return self._existing_movies.copy()

    @existing_movies.setter
    def existing_movies(self, movies):
        self._existing_movies = movies

    @property
    def existing_ticket_types(self):
        return self._existing_ticket_types.copy()

    @existing_ticket_types.setter
    def existing_ticket_types(self, tickets):
        self._existing_ticket_types = tickets

    def add_to_customers(self, customer):
        self._existing_customers.append(customer)

    def add_to_movies(self, movie):
        self._existing_movies.append(movie)

    # Modify customer to be taken based on S C or F and not len
    # Reads customers from file and calls the respective load function to load into list
    def read_customer(self):
        """Loads the customer data from file and appends to list of existing customers"""
        try:
            with open('customers.txt', 'r') as customer_file:
                line = customer_file.readline()
                while line:
                    customer_data = line.strip().split(',')
                    customer_data = [entry.strip() for entry in customer_data if entry != ""]
                    customer_code = customer_data[0][0].upper()
                    if customer_code == 'S':
                        self.load_reward_step_customer(customer_data)
                    elif customer_code == 'F':
                        self.load_reward_flat_customer(customer_data)
                    else:
                        self.load_customer(customer_data)
                    customer_id_number = int(customer_data[0][1:]) + 1
                    line = customer_file.readline()
                else:
                    print("Finished reading customer file without errors")
        except FileNotFoundError:
            print("Error : Please ensure the right file path is specified! File should be in "
                  "the current working directory.")
        except IndexError:
            print("File is corrupt")
        finally:
            Customer.set_customer_id_count(customer_id_number)
            # self.display_customers()

    # Loads reward step customers
    def load_reward_step_customer(self, customer_data: list):
        """Instantiates RewardStepCustomers"""
        reward_step_customer = RewardStepCustomer(customer_data[0], customer_data[1])
        self._existing_customers.append(reward_step_customer)
        reward_step_customer.discount_rate = customer_data[2]
        RewardStepCustomer.set_threshold(customer_data[3])

    # Loads reward flat customers
    def load_reward_flat_customer(self, customer_data: list):
        """Instantiates RewardFlatCustomers"""
        reward_flat_customer = RewardFlatCustomer(customer_data[0], customer_data[1])
        self._existing_customers.append(reward_flat_customer)
        RewardFlatCustomer.set_discount_rate(customer_data[2])

    # Loads normal customers
    def load_customer(self, customer_data: list):
        """Instantiates Normal Customers"""
        customer = Customer(customer_data[0], customer_data[1])
        self._existing_customers.append(customer)

    # Reads movie from file and calls the load function to load into a list
    def read_movies(self):
        """Loads the movies from file and appends to list of existing movies"""
        try:
            with open('movies.txt', 'r') as movie_file:
                line = movie_file.readline()
                while line:
                    movie_data = line.strip().split(',')
                    movie_data = [entry.strip() for entry in movie_data if entry != ""]
                    self.load_movies(movie_data)
                    movie_id_number = int(movie_data[0][1:]) + 1
                    line = movie_file.readline()
                else:
                    print("Finished reading movie file without errors")
        except FileNotFoundError:
            print("Error : Please ensure the right file path is specified! File should be in "
                  "the current working directory.")
        finally:
            Movie.set_movie_id_count(movie_id_number)
            # self.display_movie()

    # Loads movies
    def load_movies(self, movie_data: list):
        """Instantiates movies"""
        movie = Movie(movie_data[0], movie_data[1], movie_data[2])
        self._existing_movies.append(movie)

    # Reads tickets from file and calls the load function to load into a list
    def read_tickets(self):
        try:
            with open('tickets.txt', 'r') as ticket_file:
                line = ticket_file.readline()
                while line:
                    ticket_data = line.strip().split(',')
                    ticket_data = [entry.strip() for entry in ticket_data if entry != ""]
                    if ticket_data[0][0].upper() == 'T':
                        self.load_tickets(ticket_data)
                    else:
                        self.load_group_tickets(ticket_data)
                    line = ticket_file.readline()
                else:
                    print("Finished reading ticket file without errors")
        except FileNotFoundError:
            print("Error : Please ensure the right file path is specified! File should be in "
                  "the current working directory.")
        finally:
            pass
            # self.display_ticket()

    # Loads tickets
    def load_tickets(self, ticket_data: list):
        """Instantiates ticket-types"""
        ticket = Ticket(ticket_data[0], ticket_data[1], ticket_data[2])
        self._existing_ticket_types.append(ticket)

    def load_group_tickets(self, ticket_data: list):
        """Instantiates group ticket"""
        if len(ticket_data) % 2 != 0:
            print(f"Invalid Ticket Entry {', '.join(ticket_data)}")
        else:
            try:
                tickets_dict = {ticket_data[i]: ticket_data[i + 1] for i in
                                range(2, len(ticket_data), 2)}
                tickets = {self.find_ticket(ticket): tickets_dict.get(ticket) for ticket in tickets_dict.keys()}
                computed_cost = Records.calc_grp_price(tickets)
                if computed_cost > 0:
                    self._existing_ticket_types.append(GroupTicket(ticket_data[0], ticket_data[1], computed_cost,
                                                                   tickets=tickets))
                else:
                    raise InvalidEntryError
            except TypeError:
                print(f"Invalid Group Ticket found! {', '.join(ticket_data)}")
            except InvalidEntryError:
                print(f"Something wrong with this group ticket! {', '.join(ticket_data)}")

    @staticmethod
    def calc_grp_price(tickets: dict) -> float:
        """Calculates price for given group ticket"""
        cost = 0
        for ticket, quantity in tickets.items():
            cost += float(ticket.ticket_price) * int(quantity)
        cost *= 0.8
        if cost >= 50.0:
            return round(cost, 1)
        else:
            return -1

    # Search method for customer
    def find_customer(self, query: str):
        """ Search for customer in existing customers"""
        for item in self._existing_customers:
            if query.upper() == item.customer_name.upper() or query.upper() == item.customer_id.upper():
                return item
        return None

    # Search method for movie
    def find_movie(self, query: str):
        """ Search for customer in existing customers"""
        for item in self._existing_movies:
            if query.upper() == item.movie_name.upper() or query.upper() == item.movie_id.upper():
                return item
        return None

    # Search method for ticket types
    def find_ticket(self, query: str):
        """ Search for customer in existing customers"""
        for item in self._existing_ticket_types:
            if query.upper() == item.ticket_name.upper() or query.upper() == item.ticket_id.upper():
                return item
        return None

    # Displays all existing customers by invoking their respective display methods
    def display_customers(self):
        for customer in self._existing_customers:
            customer.display_info()

    # Displays all existing movie by invoking their respective display methods
    def display_movie(self):
        for movie in self._existing_movies:
            movie.display_info()

    # Displays all existing ticket types by invoking their respective display methods
    def display_ticket(self):
        for ticket in self._existing_ticket_types:
            ticket.display_info()
