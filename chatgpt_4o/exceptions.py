"""
Custom exceptions for the ChatGPT 4o API.
"""

class APIError(Exception):
    """Base exception for API errors."""
    pass

class AuthenticationError(APIError):
    """Exception raised for authentication errors."""
    pass

class RateLimitError(APIError):
    """Exception raised when API rate limit is exceeded."""
    pass
