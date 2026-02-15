#!/usr/bin/env python3
"""
OOPS Banner App - Main Application
Demonstrates Object-Oriented Programming concepts in action
"""
from src.banner_factory import BannerFactory
from src.banner_types import (
    SimpleBanner,
    BorderedBanner,
    FramedBanner,
    DoubleBorderedBanner,
    CenteredBanner,
    UpperCaseBanner,
    ReversedBanner
)
from src.decorators import PaddedDecorator, PrefixDecorator, NumberedDecorator


def demonstrate_basic_banners():
    """Demonstrate basic banner types (Inheritance and Polymorphism)"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION 1: Basic Banner Types")
    print("(Inheritance and Polymorphism)")
    print("=" * 60)
    
    text = "Hello, OOP World!"
    
    print("\n1. SimpleBanner:")
    banner = SimpleBanner(text)
    print(banner.display())
    
    print("\n2. BorderedBanner:")
    banner = BorderedBanner(text)
    print(banner.display())
    
    print("\n3. BorderedBanner with custom border:")
    banner = BorderedBanner(text, border_char='#')
    print(banner.display())
    
    print("\n4. FramedBanner:")
    banner = FramedBanner(text)
    print(banner.display())
    
    print("\n5. DoubleBorderedBanner:")
    banner = DoubleBorderedBanner(text)
    print(banner.display())
    
    print("\n6. CenteredBanner:")
    banner = CenteredBanner(text, total_width=40)
    print(banner.display())
    
    print("\n7. UpperCaseBanner:")
    banner = UpperCaseBanner(text)
    print(banner.display())
    
    print("\n8. ReversedBanner:")
    banner = ReversedBanner(text)
    print(banner.display())


def demonstrate_factory_pattern():
    """Demonstrate Factory Pattern"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION 2: Factory Design Pattern")
    print("=" * 60)
    
    print("\nAvailable banner types:", BannerFactory.get_available_types())
    
    text = "Created by Factory!"
    
    print("\nCreating banners using the factory:")
    for banner_type in ['simple', 'bordered', 'framed']:
        print(f"\n{banner_type.upper()}:")
        banner = BannerFactory.create_banner(banner_type, text)
        if banner:
            print(banner.display())


def demonstrate_decorator_pattern():
    """Demonstrate Decorator Pattern"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION 3: Decorator Design Pattern")
    print("=" * 60)
    
    text = "Decorated Banner"
    
    # Base banner
    print("\nBase banner (Bordered):")
    banner = BorderedBanner(text)
    print(banner.display())
    
    # Add padding
    print("\nWith padding decorator:")
    decorated = PaddedDecorator(banner, padding=1)
    print(decorated.display())
    
    # Add prefix
    print("\nWith prefix decorator:")
    decorated = PrefixDecorator(banner, prefix=">>> ")
    print(decorated.display())
    
    # Add line numbers
    print("\nWith numbered decorator:")
    decorated = NumberedDecorator(banner)
    print(decorated.display())
    
    # Combine decorators (Decorator chaining)
    print("\nWith combined decorators (Padded + Prefixed):")
    decorated = PrefixDecorator(PaddedDecorator(banner), prefix="-> ")
    print(decorated.display())


def demonstrate_encapsulation():
    """Demonstrate Encapsulation"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION 4: Encapsulation")
    print("=" * 60)
    
    banner = BorderedBanner("Initial Text")
    print("\nInitial banner:")
    print(banner.display())
    
    # Using property setter (controlled access)
    print("\nModifying text using property setter:")
    banner.text = "Modified Text"
    print(banner.display())
    
    # Accessing properties
    print(f"\nBanner text property: '{banner.text}'")
    print(f"Banner width property: {banner.width}")


def demonstrate_polymorphism():
    """Demonstrate Polymorphism"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION 5: Polymorphism")
    print("(Same interface, different behaviors)")
    print("=" * 60)
    
    # List of different banner types
    banners = [
        SimpleBanner("Polymorphism"),
        BorderedBanner("Polymorphism"),
        FramedBanner("Polymorphism"),
        UpperCaseBanner("Polymorphism"),
    ]
    
    # Call the same method on different objects
    print("\nCalling display() on different banner types:")
    for i, banner in enumerate(banners, 1):
        print(f"\n{i}. {banner.__class__.__name__}:")
        print(banner.display())


def interactive_mode():
    """Interactive banner creator"""
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE: Create Your Own Banner!")
    print("=" * 60)
    
    try:
        text = input("\nEnter text for your banner: ").strip()
        if not text:
            text = "Default Banner Text"
        
        print("\nAvailable banner types:")
        types = BannerFactory.get_available_types()
        for i, banner_type in enumerate(types, 1):
            print(f"{i}. {banner_type}")
        
        choice = input(f"\nChoose banner type (1-{len(types)}): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(types):
                banner_type = types[idx]
                banner = BannerFactory.create_banner(banner_type, text)
                print("\nYour banner:")
                print(banner.display())
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input!")
    except EOFError:
        print("\nInteractive mode not available in this environment.")


def main():
    """Main application entry point"""
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  OOPS BANNER APP - OOP Learning Project  ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    
    # Run all demonstrations
    demonstrate_basic_banners()
    demonstrate_factory_pattern()
    demonstrate_decorator_pattern()
    demonstrate_encapsulation()
    demonstrate_polymorphism()
    
    # Interactive mode (optional)
    print("\n" + "=" * 60)
    response = input("\nWould you like to try interactive mode? (y/n): ").strip().lower()
    if response == 'y':
        interactive_mode()
    
    print("\n" + "=" * 60)
    print("Thank you for exploring OOP concepts with Banner App!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
