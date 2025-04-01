"""
ChatGPT 4o API wrapper package.
"""

from .client import ChatGPT4o
from .exceptions import APIError, AuthenticationError, RateLimitError

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = ["ChatGPT4o", "APIError", "AuthenticationError", "RateLimitError"]
