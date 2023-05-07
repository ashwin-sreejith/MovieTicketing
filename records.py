from rewardStepCustomer import RewardStepCustomer
from rewardFlatCustomer import RewardFlatCustomer
from customer import Customer
from movie import Movie
from ticket import Ticket


class Records:
    """Class to handle database"""

    def __init__(self):
        self._existing_customers = []
        self._existing_movies = []
        self._existing_ticket_types = []
        self.read_customer()
        self.read_movies()
        self.read_tickets()

    def read_customer(self):
        """Loads the customer data from file and appends to list of existing customers"""
        try:
            with open('./COSC2531_Assignment2_txtfiles/customers.txt', 'r') as customer_file:
                line = customer_file.readline()
                while line:
                    customer_data = line.strip().split(',')
                    customer_data = [entry.strip() for entry in customer_data if entry != ""]
                    if len(customer_data) > 3:
                        self.load_reward_step_customer(customer_data)
                    elif len(customer_data) > 2:
                        self.load_reward_flat_customer(customer_data)
                    else:
                        self.load_customer(customer_data)
                    line = customer_file.readline()
        except FileNotFoundError:
            print("Error : Please ensure the right file path is specified! File should be in "
                  "'COSC2531_Assignment2_txtfiles' folder in the current working directory.")
        finally:
            print("Finished reading customer data!")

    def load_reward_step_customer(self, customer_data: list):
        """Instantiates RewardStepCustomers"""
        reward_step_customer = RewardStepCustomer(customer_data[0], customer_data[1])
        self._existing_customers.append(reward_step_customer)
        reward_step_customer.discount_rate = customer_data[2]
        reward_step_customer.set_threshold(customer_data[3])

    def load_reward_flat_customer(self, customer_data: list):
        """Instantiates RewardFlatCustomers"""
        reward_flat_customer = RewardFlatCustomer(customer_data[0], customer_data[1])
        self._existing_customers.append(reward_flat_customer)
        reward_flat_customer.set_discount_rate(customer_data[2])

    def load_customer(self, customer_data: list):
        """Instantiates Normal Customers"""
        customer = Customer(customer_data[0], customer_data[1])
        self._existing_customers.append(customer)

    def read_movies(self):
        """Loads the movies from file and appends to list of existing movies"""
        try:
            with open('./COSC2531_Assignment2_txtfiles/movies.txt', 'r') as movie_file:
                line = movie_file.readline()
                while line:
                    movie_data = line.strip().split(',')
                    movie_data = [entry.strip() for entry in movie_data if entry != ""]
                    self.load_movies(movie_data)
                    line = movie_file.readline()
        except FileNotFoundError:
            print("Error : Please ensure the right file path is specified! File should be in "
                  "'COSC2531_Assignment2_txtfiles' folder in the current working directory.")
        finally:
            print("Finished reading movie data!")

    def load_movies(self, movie_data: list):
        """Instantiates movies"""
        movie = Movie(movie_data[0], movie_data[1], movie_data[2])
        self._existing_movies.append(movie)

    def read_tickets(self):
        try:
            with open('./COSC2531_Assignment2_txtfiles/tickets.txt', 'r') as ticket_file:
                line = ticket_file.readline()
                while line:
                    ticket_data = line.strip().split(',')
                    ticket_data = [entry.strip() for entry in ticket_data if entry != ""]
                    self.load_tickets(ticket_data)
                    line = ticket_file.readline()
        except FileNotFoundError:
            print("Error : Please ensure the right file path is specified! File should be in "
                  "'COSC2531_Assignment2_txtfiles' folder in the current working directory.")
        finally:
            print("Finished reading ticket data!")

    def load_tickets(self, ticket_data: list):
        """Instantiates ticket-types"""
        ticket = Ticket(ticket_data[0], ticket_data[1], ticket_data[2])
        self._existing_ticket_types.append(ticket)

    def find_customer(self, query):
        """ Search for customer in existing customers"""
        for item in self._existing_customers:
            if query.upper() == item.customer_name or query.upper() == item.customer_id.upper():
                return item
        return None

    def find_movie(self, query):
        """ Search for customer in existing customers"""
        for item in self._existing_movies:
            if query.upper() == item.movie_name.upper() or query.upper() == item.movie_id.upper():
                return item
        return None

    def find_ticket(self, query):
        """ Search for customer in existing customers"""
        for item in self._existing_ticket_types:
            if query.upper() == item.ticket_name.upper() or query.upper() == item.ticket_id.upper():
                return item
        return None
