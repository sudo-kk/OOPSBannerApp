"""
Decorator Pattern implementation for banners
"""
from src.banner import Banner


class BannerDecorator(Banner):
    """
    Base decorator class for adding functionality to banners.
    Demonstrates the DECORATOR DESIGN PATTERN.
    
    This allows adding new behaviors to banner objects dynamically
    without modifying their structure.
    """
    
    def __init__(self, banner: Banner):
        """
        Initialize decorator with a banner to wrap.
        
        Args:
            banner: The banner to decorate
        """
        self._wrapped_banner = banner
        super().__init__(banner.text)
    
    def display(self) -> str:
        """Display the wrapped banner"""
        return self._wrapped_banner.display()


class PaddedDecorator(BannerDecorator):
    """
    Decorator that adds padding around a banner.
    """
    
    def __init__(self, banner: Banner, padding: int = 1):
        """
        Initialize with padding.
        
        Args:
            banner: The banner to decorate
            padding: Number of blank lines to add (default: 1)
        """
        super().__init__(banner)
        self._padding = padding
    
    def display(self) -> str:
        """Display banner with padding"""
        pad = "\n" * self._padding
        return f"{pad}{self._wrapped_banner.display()}{pad}"


class PrefixDecorator(BannerDecorator):
    """
    Decorator that adds a prefix to each line of the banner.
    """
    
    def __init__(self, banner: Banner, prefix: str = ">>> "):
        """
        Initialize with prefix.
        
        Args:
            banner: The banner to decorate
            prefix: String to add before each line
        """
        super().__init__(banner)
        self._prefix = prefix
    
    def display(self) -> str:
        """Display banner with prefix on each line"""
        lines = self._wrapped_banner.display().split('\n')
        return '\n'.join(self._prefix + line for line in lines)


class NumberedDecorator(BannerDecorator):
    """
    Decorator that adds line numbers to a banner.
    """
    
    def display(self) -> str:
        """Display banner with line numbers"""
        lines = self._wrapped_banner.display().split('\n')
        return '\n'.join(f"{i+1}. {line}" for i, line in enumerate(lines))
