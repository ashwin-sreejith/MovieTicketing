class Movie:
    """Class to handle movie entries"""

    def __init__(self, movie_id, movie_name, seats_available):
        self._movie_id = movie_id
        self._movie_name = movie_name
        self._seats_available = seats_available

    def display_info(self):
        print(f"Movie ID : {self._movie_id}\n" + f"Movie Name : {self._movie_name}\n" +
              f"Seats available : {self._seats_available}")

