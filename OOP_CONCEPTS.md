# OOP Concepts Summary

This document provides a detailed breakdown of how each Object-Oriented Programming concept is demonstrated in the OOPS Banner App.

## 1. Abstraction

**Definition**: Hiding complex implementation details and showing only essential features.

**Implementation in Banner App**:
- `Banner` class is an abstract base class (ABC) that defines the interface
- Abstract method `display()` forces all subclasses to implement their own version
- Users interact with the simple `display()` interface without knowing implementation details

```python
from abc import ABC, abstractmethod

class Banner(ABC):
    @abstractmethod
    def display(self) -> str:
        """Must be implemented by all subclasses"""
        pass
```

**Key Location**: `src/banner.py`

## 2. Encapsulation

**Definition**: Bundling data and methods that work on that data, restricting direct access to internal state.

**Implementation in Banner App**:
- Protected attributes: `_text`, `_width` (using underscore convention)
- Public interface via `@property` decorators for controlled access
- Private method `_calculate_width()` hides implementation details
- Getters and setters control how attributes are accessed and modified

```python
class Banner(ABC):
    def __init__(self, text: str):
        self._text = text  # Protected attribute
        self._width = self._calculate_width()  # Protected attribute
    
    @property
    def text(self) -> str:
        """Controlled access via property"""
        return self._text
    
    @text.setter
    def text(self, value: str):
        """Controlled modification with side effects"""
        self._text = value
        self._width = self._calculate_width()
```

**Key Location**: `src/banner.py`

## 3. Inheritance

**Definition**: Creating new classes based on existing classes, inheriting their properties and methods.

**Implementation in Banner App**:
- Multiple banner classes inherit from `Banner` base class
- Subclasses inherit common attributes and methods
- Each subclass can extend functionality while maintaining base interface
- Constructor chaining using `super().__init__()`

```python
class BorderedBanner(Banner):
    """Inherits from Banner"""
    
    def __init__(self, text: str, border_char: str = '*'):
        super().__init__(text)  # Call parent constructor
        self._border_char = border_char  # Add new attribute
    
    def display(self) -> str:
        """Implement abstract method"""
        # Custom implementation
```

**Key Locations**: 
- Base class: `src/banner.py`
- Derived classes: `src/banner_types.py`, `src/decorators.py`

**Inheritance Hierarchy**:
```
Banner (ABC)
├── SimpleBanner
├── BorderedBanner
├── FramedBanner
├── DoubleBorderedBanner
├── CenteredBanner
├── UpperCaseBanner
├── ReversedBanner
└── BannerDecorator (ABC)
    ├── PaddedDecorator
    ├── PrefixDecorator
    └── NumberedDecorator
```

## 4. Polymorphism

**Definition**: The ability of objects of different types to be accessed through the same interface, with each type responding differently.

**Implementation in Banner App**:
- All banner types implement the `display()` method differently
- Same method call produces different outputs based on object type
- Enables treating different banner types uniformly in collections

```python
# Same interface, different behaviors
def show_banner(banner: Banner):
    """Works with any Banner subclass"""
    print(banner.display())

# All these work with the same function
show_banner(SimpleBanner("Hello"))      # Plain text
show_banner(BorderedBanner("Hello"))    # With borders
show_banner(FramedBanner("Hello"))      # With frame
```

**Demonstration**: See `demonstrate_polymorphism()` in `main.py`

## 5. Composition

**Definition**: Building complex objects by combining simpler objects.

**Implementation in Banner App**:
- `BannerDecorator` wraps another `Banner` object
- Decorators compose functionality by layering behaviors
- Allows building complex banners from simpler ones

```python
class BannerDecorator(Banner):
    def __init__(self, banner: Banner):
        self._wrapped_banner = banner  # Composition
        super().__init__(banner.text)
```

**Key Location**: `src/decorators.py`

## Design Patterns

### Factory Pattern

**Purpose**: Encapsulate object creation logic.

**Implementation**:
```python
class BannerFactory:
    _banner_types = {
        'simple': SimpleBanner,
        'bordered': BorderedBanner,
        # ...
    }
    
    @classmethod
    def create_banner(cls, banner_type: str, text: str, **kwargs):
        """Create banner without exposing instantiation details"""
        banner_class = cls._banner_types.get(banner_type.lower())
        if banner_class:
            return banner_class(text, **kwargs)
        return None
```

**Benefits**:
- Centralized object creation
- Easy to add new banner types
- Client code doesn't need to know concrete classes

**Key Location**: `src/banner_factory.py`

### Decorator Pattern

**Purpose**: Add functionality to objects dynamically without modifying their structure.

**Implementation**:
```python
# Wrap banners to add functionality
banner = BorderedBanner("Hello")
padded = PaddedDecorator(banner)
prefixed = PrefixDecorator(padded)
```

**Benefits**:
- Add behaviors at runtime
- Combine decorators flexibly
- Follows Open/Closed Principle (open for extension, closed for modification)

**Key Location**: `src/decorators.py`

## SOLID Principles

### Single Responsibility Principle (SRP)
- Each class has one reason to change
- `Banner` handles text display
- `BannerFactory` handles object creation
- Each decorator adds one specific functionality

### Open/Closed Principle (OCP)
- Classes are open for extension (inheritance) but closed for modification
- Add new banner types without changing existing code
- Decorators extend functionality without modifying banner classes

### Liskov Substitution Principle (LSP)
- Any `Banner` subclass can replace the base `Banner` type
- All maintain the same interface and contract
- Polymorphic use is safe and predictable

### Interface Segregation Principle (ISP)
- `Banner` interface is minimal and focused
- Only one abstract method required: `display()`
- No unnecessary methods forced on implementations

### Dependency Inversion Principle (DIP)
- Code depends on abstractions (`Banner`) not concrete classes
- Factory returns `Banner` interface, not specific types
- Decorators work with `Banner` interface

## Code Organization

### Module Structure
```
src/
├── banner.py          # Core abstraction (ABC)
├── banner_types.py    # Concrete implementations
├── banner_factory.py  # Factory pattern
└── decorators.py      # Decorator pattern
```

### Testing Structure
- Unit tests for each class
- Tests for inheritance behavior
- Tests for polymorphism
- Tests for design patterns
- **25 tests total, all passing**

## Learning Progression

1. **Start with `banner.py`**: Learn abstraction and encapsulation
2. **Move to `banner_types.py`**: Understand inheritance and polymorphism
3. **Study `banner_factory.py`**: Learn factory pattern
4. **Explore `decorators.py`**: Understand decorator pattern and composition
5. **Run `main.py`**: See everything in action
6. **Try `examples.py`**: Practice using the library
7. **Read `tests/test_banners.py`**: Learn testing OOP code

## Key Takeaways

1. **Abstraction** simplifies complex systems by hiding details
2. **Encapsulation** protects data and provides controlled access
3. **Inheritance** enables code reuse and hierarchical relationships
4. **Polymorphism** allows flexible, extensible code
5. **Design Patterns** solve common problems elegantly
6. **Composition** over inheritance for flexible behavior addition
7. **SOLID principles** guide good OOP design

## Practical Applications

These concepts apply to:
- GUI frameworks (buttons, windows inherit from Widget)
- Game development (characters inherit from Entity)
- Web frameworks (views inherit from BaseView)
- Database ORMs (models inherit from Model)
- Plugin systems (use factory and abstract base classes)
- Middleware chains (use decorator pattern)

---

**Remember**: Good OOP design makes code:
- **Maintainable** - Easy to update and fix
- **Extensible** - Easy to add new features
- **Reusable** - Components can be used in different contexts
- **Testable** - Each component can be tested independently
- **Understandable** - Clear structure and responsibilities
