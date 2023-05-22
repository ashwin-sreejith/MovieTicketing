class Movie:
    """Class to handle movie entries"""

    _MOVIE_ID_COUNT: int = 0

    def __init__(self, movie_id, movie_name, seats_available):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.seats_available = seats_available

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

    def display_info(self):
        print(f"Movie ID : {self._movie_id}\n" + f"Movie Name : {self._movie_name}\n" +
              f"Seats available : {self._seats_available}")
