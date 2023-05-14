from records import Records
from customer import Customer
from rewardFlatCustomer import RewardFlatCustomer
from rewardStepCustomer import RewardStepCustomer


class Operations:
    """Main class to handle all operations"""

    _customer_id_count: int = 12
    _record = Records()

    def __init__(self):
        self.purchase_ticket()

    @staticmethod
    def purchase_ticket():
        customer_name = Operations.check_customer()
        movie_name = Operations.check_movie()
        ticket_type = Operations.check_ticket_type()

    @staticmethod
    def check_customer():
        # Accepts customer name
        customer_name = input("Enter the customer name : ").strip()
        is_customer_available = Operations._record.find_customer(customer_name)
        if not is_customer_available:
            Operations.add_customer_to_storage(customer_name)
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
            program_code = input("Choose the discount program (F - RewardFlatCustomer, S - RewardStepCustomer)"). \
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
        Operations._record.existing_customers.append(this_customer)
        Operations.save_to_file(this_customer, 'customers.txt')

    @staticmethod
    def add_customer_to_storage(customer_name: str):
        while True:
            # Prompts user to enter if customer wishes to join the program
            choice = input("Does the customer want to join the rewards program? (Y - YES, N - NO) ").upper().strip()
            # If y or Y is chosen
            if choice == 'Y':
                Operations.add_to_program(customer_name, True)
                break
            elif choice == 'N':
                Operations.add_to_program(customer_name)
                break
            else:
                print("Sorry! Please enter 'Y' for YES and 'N' for NO")

