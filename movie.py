class Movie:
    """Class to handle movie entries"""

    def __init__(self, movie_id, movie_name, seats_available):
        self._movie_id = movie_id
        self._movie_name = movie_name
        self._seats_available = seats_available

    @property
    def movie_name(self):
        return self._movie_name

    @movie_name.setter
    def movie_name(self, movie_name):
        self._movie_name = movie_name

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id):
        self._movie_id = movie_id

    @property
    def seats_available(self):
        return self._seats_available

    @seats_available.setter
    def seats_available(self, seats):
        self._seats_available = seats

    def display_info(self):
        print(f"Movie ID : {self._movie_id}\n" + f"Movie Name : {self._movie_name}\n" +
              f"Seats available : {self._seats_available}")
