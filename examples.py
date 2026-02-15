#!/usr/bin/env python3
"""
Examples demonstrating how to use the OOPS Banner App
"""

from src.banner_types import (
    SimpleBanner,
    BorderedBanner,
    FramedBanner,
    CenteredBanner
)
from src.banner_factory import BannerFactory
from src.decorators import PaddedDecorator, PrefixDecorator, NumberedDecorator


def example_1_basic_usage():
    """Example 1: Basic banner creation and display"""
    print("Example 1: Basic Usage")
    print("-" * 50)
    
    # Create a simple banner
    banner = SimpleBanner("Welcome to OOP!")
    print(banner.display())
    print()
    
    # Create a bordered banner
    banner = BorderedBanner("Python Programming", border_char='=')
    print(banner.display())
    print()


def example_2_factory_pattern():
    """Example 2: Using the factory pattern"""
    print("Example 2: Factory Pattern")
    print("-" * 50)
    
    # Create banners using factory
    messages = [
        ("framed", "Learning OOP"),
        ("bordered", "Design Patterns"),
        ("uppercase", "Important Notice")
    ]
    
    for banner_type, text in messages:
        banner = BannerFactory.create_banner(banner_type, text)
        print(f"{banner_type.upper()}:")
        print(banner.display())
        print()


def example_3_property_access():
    """Example 3: Accessing and modifying properties"""
    print("Example 3: Property Access and Modification")
    print("-" * 50)
    
    banner = BorderedBanner("Original Text")
    print("Original:")
    print(banner.display())
    print(f"Width: {banner.width}")
    print()
    
    # Modify text using property setter
    banner.text = "Updated Text"
    print("After modification:")
    print(banner.display())
    print(f"New width: {banner.width}")
    print()


def example_4_decorators():
    """Example 4: Using decorators"""
    print("Example 4: Decorators")
    print("-" * 50)
    
    # Base banner
    banner = FramedBanner("Decorated")
    
    # Apply decorators
    padded = PaddedDecorator(banner, padding=1)
    prefixed = PrefixDecorator(banner, prefix=">> ")
    numbered = NumberedDecorator(banner)
    
    print("Padded:")
    print(padded.display())
    
    print("Prefixed:")
    print(prefixed.display())
    print()
    
    print("Numbered:")
    print(numbered.display())
    print()


def example_5_polymorphism():
    """Example 5: Polymorphic behavior"""
    print("Example 5: Polymorphism")
    print("-" * 50)
    
    # Function that works with any banner type
    def display_banner(banner):
        print(banner.display())
    
    # Works with different banner types
    banners = [
        SimpleBanner("Polymorphic behavior"),
        BorderedBanner("Works with any banner"),
        FramedBanner("Same interface, different output")
    ]
    
    for banner in banners:
        display_banner(banner)
        print()


def example_6_custom_banner():
    """Example 6: Creating and registering a custom banner"""
    print("Example 6: Custom Banner Type")
    print("-" * 50)
    
    # Import base class
    from src.banner import Banner
    
    # Define custom banner
    class ExcitedBanner(Banner):
        def display(self):
            return f"!!! {self._text.upper()} !!!"
    
    # Register with factory
    BannerFactory.register_banner_type('excited', ExcitedBanner)
    
    # Use it
    banner = BannerFactory.create_banner('excited', 'This is exciting')
    print(banner.display())
    print()


def example_7_chaining_decorators():
    """Example 7: Chaining multiple decorators"""
    print("Example 7: Decorator Chaining")
    print("-" * 50)
    
    # Create base banner
    banner = BorderedBanner("Multi-decorated")
    
    # Chain decorators
    decorated = NumberedDecorator(
        PrefixDecorator(
            PaddedDecorator(banner, padding=1),
            prefix="* "
        )
    )
    
    print(decorated.display())
    print()


def main():
    """Run all examples"""
    print("=" * 50)
    print("OOPS BANNER APP - USAGE EXAMPLES")
    print("=" * 50)
    print()
    
    example_1_basic_usage()
    example_2_factory_pattern()
    example_3_property_access()
    example_4_decorators()
    example_5_polymorphism()
    example_6_custom_banner()
    example_7_chaining_decorators()
    
    print("=" * 50)
    print("End of examples")
    print("=" * 50)


if __name__ == "__main__":
    main()
