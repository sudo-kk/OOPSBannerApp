"""
Concrete Banner implementations demonstrating Inheritance and Polymorphism
"""
from src.banner import Banner


class SimpleBanner(Banner):
    """
    Simple banner that displays plain text.
    Demonstrates INHERITANCE - extends Banner class.
    Demonstrates POLYMORPHISM - implements abstract display() method.
    """
    
    def display(self) -> str:
        """Display simple text banner"""
        return self._text


class BorderedBanner(Banner):
    """
    Banner with decorative borders.
    Demonstrates INHERITANCE and POLYMORPHISM.
    """
    
    def __init__(self, text: str, border_char: str = '*'):
        """
        Initialize a bordered banner.
        
        Args:
            text: The text to display
            border_char: Character to use for borders (default: '*')
        """
        super().__init__(text)
        self._border_char = border_char
    
    def display(self) -> str:
        """Display text with borders"""
        border_line = self._border_char * (self._width + 4)
        middle_line = f"{self._border_char} {self._text} {self._border_char}"
        return f"{border_line}\n{middle_line}\n{border_line}"


class FramedBanner(Banner):
    """
    Banner with a decorative frame.
    Demonstrates INHERITANCE and POLYMORPHISM.
    """
    
    def display(self) -> str:
        """Display text with a frame"""
        top_line = "╔" + "═" * (self._width + 2) + "╗"
        middle_line = f"║ {self._text} ║"
        bottom_line = "╚" + "═" * (self._width + 2) + "╝"
        return f"{top_line}\n{middle_line}\n{bottom_line}"


class DoubleBorderedBanner(Banner):
    """
    Banner with double borders.
    Demonstrates INHERITANCE and POLYMORPHISM.
    """
    
    def display(self) -> str:
        """Display text with double borders"""
        outer_border = "=" * (self._width + 8)
        inner_border = "-" * (self._width + 4)
        text_line = f"| {self._text} |"
        return f"{outer_border}\n  {inner_border}\n  {text_line}\n  {inner_border}\n{outer_border}"


class CenteredBanner(Banner):
    """
    Banner that centers text within a specified width.
    Demonstrates INHERITANCE and POLYMORPHISM with additional functionality.
    """
    
    def __init__(self, text: str, total_width: int = 50):
        """
        Initialize a centered banner.
        
        Args:
            text: The text to display
            total_width: Total width of the banner (default: 50)
        """
        super().__init__(text)
        self._total_width = max(total_width, self._width)
    
    def display(self) -> str:
        """Display centered text"""
        padding = (self._total_width - self._width) // 2
        return " " * padding + self._text


class UpperCaseBanner(Banner):
    """
    Banner that displays text in uppercase.
    Demonstrates INHERITANCE and POLYMORPHISM with text transformation.
    """
    
    def display(self) -> str:
        """Display text in uppercase"""
        return self._text.upper()


class ReversedBanner(Banner):
    """
    Banner that displays text in reverse.
    Demonstrates INHERITANCE and POLYMORPHISM with text manipulation.
    """
    
    def display(self) -> str:
        """Display reversed text"""
        return self._text[::-1]
