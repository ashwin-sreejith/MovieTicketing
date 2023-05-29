class Movie:
    """Class to handle movie entries"""

    _MOVIE_ID_COUNT: int = 0

    def __init__(self, movie_id, movie_name, seats_available):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.seats_available = seats_available
        self._revenue = 0
        self.ticket_details = {}

    @property
    def movie_name(self):
        return self._movie_name

    @movie_name.setter
    def movie_name(self, movie_name):
        self._movie_name = movie_name.capitalize()

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id):
        if len(movie_id) > 1:
            self._movie_id = movie_id
        else:
            self._movie_id = movie_id + str(Movie._MOVIE_ID_COUNT)
            Movie._MOVIE_ID_COUNT += 1

    @property
    def seats_available(self):
        return self._seats_available

    @seats_available.setter
    def seats_available(self, seats: int):
        self._seats_available = int(seats)

    @staticmethod
    def get_customer_id_count():
        return Movie._MOVIE_ID_COUNT

    @staticmethod
    def set_movie_id_count(movie_id_number: int):
        Movie._MOVIE_ID_COUNT = movie_id_number

    @property
    def revenue(self):
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        self._revenue += revenue

    @property
    def ticket_details(self):
        return self._ticket_details.copy()

    @ticket_details.setter
    def ticket_details(self, ticket):
        self._ticket_details = ticket

    def update_ticket_details(self, ticket):
        for ticket_entry in ticket:
            ticket_type, quantity = ticket_entry
            if ticket_type.ticket_name in self._ticket_details:
                self._ticket_details[ticket_type.ticket_name] += quantity
            else:
                self._ticket_details[ticket_type.ticket_name] = quantity

    def display_info(self):
        print(self.movie_id.center(40) + "|" + self.movie_name.center(40) + "|"
              + str(self.seats_available).center(40))

    def to_string(self):
        return f"{self._movie_id}, {self._movie_name}, {self._seats_available}"
