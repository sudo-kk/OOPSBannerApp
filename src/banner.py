"""
Base Banner class demonstrating Abstraction and Encapsulation
"""
from abc import ABC, abstractmethod


class Banner(ABC):
    """
    Abstract base class for all banner types.
    Demonstrates ABSTRACTION - defining a contract that all banners must follow.
    Demonstrates ENCAPSULATION - hiding internal implementation details.
    """
    
    def __init__(self, text: str):
        """
        Initialize a banner with text.
        
        Args:
            text: The text to display in the banner
        """
        self._text = text  # Protected attribute (encapsulation)
        self._width = self._calculate_width()
    
    @property
    def text(self) -> str:
        """Get the banner text (encapsulation - controlled access)"""
        return self._text
    
    @text.setter
    def text(self, value: str):
        """Set the banner text and recalculate width"""
        self._text = value
        self._width = self._calculate_width()
    
    @property
    def width(self) -> int:
        """Get the banner width"""
        return self._width
    
    def _calculate_width(self) -> int:
        """
        Calculate the width of the banner.
        Protected method (encapsulation - internal implementation detail)
        """
        return len(self._text) if self._text else 0
    
    @abstractmethod
    def display(self) -> str:
        """
        Display the banner.
        Abstract method - must be implemented by subclasses (abstraction)
        
        Returns:
            str: The formatted banner as a string
        """
        pass
    
    def __str__(self) -> str:
        """String representation of the banner"""
        return self.display()
