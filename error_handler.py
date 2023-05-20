class Error(Exception):
    """Base class for all exceptions in the program"""
    pass


class MovieNotFoundError(Error):
    """Exception to be raised when movie not in existing list"""
    pass


class TicketTypeNotFoundError(Error):
    """Exception to be raised when ticket type not in existing list"""
    pass


class FullyBookedError(Error):
    """Exception to be raised when available seats is zero"""


class DiscountChoiceInputError(Error):
    """Exception to be raised if an invalid choice is made during opting for discounts"""
    pass


class DiscountProgramChoiceError(Error):
    """Exception to be raised if an invalid choice is made during choosing the discount program"""
    pass


class InvalidTicketQuantityError(Error):
    """Exception to be raised if the ticket quantity entered is negative or 0"""
    pass


class QuantityExceededError(Error):
    """Exception to be raised if the ticket quantity requested exceeds available seats"""
    pass

