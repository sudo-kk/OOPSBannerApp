"""
Banner Factory demonstrating the Factory Design Pattern
"""
from typing import Optional
from src.banner import Banner
from src.banner_types import (
    SimpleBanner,
    BorderedBanner,
    FramedBanner,
    DoubleBorderedBanner,
    CenteredBanner,
    UpperCaseBanner,
    ReversedBanner
)


class BannerFactory:
    """
    Factory class for creating different types of banners.
    Demonstrates the FACTORY DESIGN PATTERN and ENCAPSULATION.
    
    This class encapsulates the logic for creating banner objects,
    providing a simple interface for banner creation without exposing
    the details of how each banner type is instantiated.
    """
    
    # Registry of available banner types
    _banner_types = {
        'simple': SimpleBanner,
        'bordered': BorderedBanner,
        'framed': FramedBanner,
        'double': DoubleBorderedBanner,
        'centered': CenteredBanner,
        'uppercase': UpperCaseBanner,
        'reversed': ReversedBanner
    }
    
    @classmethod
    def create_banner(cls, banner_type: str, text: str, **kwargs) -> Optional[Banner]:
        """
        Create a banner of the specified type.
        
        Args:
            banner_type: Type of banner to create ('simple', 'bordered', etc.)
            text: Text to display in the banner
            **kwargs: Additional keyword arguments for specific banner types
        
        Returns:
            Banner object of the requested type, or None if type is invalid
        
        Example:
            >>> banner = BannerFactory.create_banner('bordered', 'Hello World', border_char='#')
            >>> print(banner.display())
        """
        banner_class = cls._banner_types.get(banner_type.lower())
        if banner_class:
            return banner_class(text, **kwargs)
        return None
    
    @classmethod
    def get_available_types(cls) -> list:
        """
        Get a list of available banner types.
        
        Returns:
            List of available banner type names
        """
        return list(cls._banner_types.keys())
    
    @classmethod
    def register_banner_type(cls, name: str, banner_class: type):
        """
        Register a new banner type.
        Allows extending the factory with custom banner types.
        
        Args:
            name: Name for the banner type
            banner_class: Banner class to register
        """
        if issubclass(banner_class, Banner):
            cls._banner_types[name.lower()] = banner_class
        else:
            raise TypeError("Banner class must inherit from Banner")
