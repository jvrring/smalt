class SmaltError(Exception):
    """Base class for all Smalt exceptions."""
    pass

class InvalidURLError(SmaltError):
    """Exception raised for invalid API URLs."""
    pass

# 403
class BadRequestError(SmaltError):
    """Exception raised for bad request errors."""
    pass

# 404
class NotFoundError(SmaltError):
    """Exception raised for not found errors."""
    pass

# 429
class TooManyRequestsError(SmaltError):
    """Exception raised for too many requests errors."""
    pass

# 500
class InternalServerError(SmaltError):
    """Exception raised for internal server errors."""
    pass

