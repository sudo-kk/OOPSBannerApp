# OOPS Banner App

A comprehensive Object-Oriented Programming (OOP) learning project that demonstrates key OOP concepts through a banner application.

## 📚 Learning Objectives

This project demonstrates the following OOP principles:

### 1. **Abstraction**
- Abstract base class `Banner` defines a contract for all banner types
- Abstract method `display()` must be implemented by all concrete classes

### 2. **Encapsulation**
- Private/protected attributes (e.g., `_text`, `_width`)
- Property decorators for controlled access to internal state
- Hidden implementation details in private methods

### 3. **Inheritance**
- Multiple concrete banner classes inherit from the base `Banner` class
- Subclasses extend functionality while maintaining the base interface
- Examples: `SimpleBanner`, `BorderedBanner`, `FramedBanner`, etc.

### 4. **Polymorphism**
- Different banner types implement the same `display()` method differently
- Objects can be used interchangeably through their common interface
- Demonstrates runtime polymorphism

### 5. **Design Patterns**
- **Factory Pattern**: `BannerFactory` for creating banner objects
- **Decorator Pattern**: Decorators for adding functionality dynamically

## 🚀 Features

### Banner Types
1. **SimpleBanner** - Plain text display
2. **BorderedBanner** - Text with customizable borders
3. **FramedBanner** - Text with decorative frame
4. **DoubleBorderedBanner** - Text with double borders
5. **CenteredBanner** - Centered text with specified width
6. **UpperCaseBanner** - Text transformed to uppercase
7. **ReversedBanner** - Text displayed in reverse

### Decorators
1. **PaddedDecorator** - Adds padding around banners
2. **PrefixDecorator** - Adds prefix to each line
3. **NumberedDecorator** - Adds line numbers

## 📦 Installation

No external dependencies required! Uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/sudo-kk/OOPSBannerApp.git
cd OOPSBannerApp

# Run the application
python main.py
```

## 💻 Usage

### Running the Demo

```bash
python main.py
```

This will run multiple demonstrations showcasing different OOP concepts.

### Using in Your Code

```python
from src.banner_types import BorderedBanner, FramedBanner
from src.banner_factory import BannerFactory
from src.decorators import PaddedDecorator

# Direct instantiation
banner = BorderedBanner("Hello, World!")
print(banner.display())

# Using factory pattern
banner = BannerFactory.create_banner('framed', 'Hello, World!')
print(banner.display())

# Using decorators
banner = BorderedBanner("Hello")
decorated = PaddedDecorator(banner, padding=2)
print(decorated.display())

# Modifying banner text
banner.text = "New Text"
print(banner.display())
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
# or
python -m unittest discover tests/
```

## 📂 Project Structure

```
OOPSBannerApp/
│
├── src/
│   ├── __init__.py
│   ├── banner.py           # Abstract base class
│   ├── banner_types.py     # Concrete banner implementations
│   ├── banner_factory.py   # Factory pattern implementation
│   └── decorators.py       # Decorator pattern implementation
│
├── tests/
│   └── test_banners.py     # Unit tests
│
├── main.py                 # Main application with demonstrations
└── README.md               # This file
```

## 🎓 OOP Concepts Demonstrated

### Example 1: Abstraction and Inheritance

```python
# Abstract base class
class Banner(ABC):
    @abstractmethod
    def display(self) -> str:
        pass

# Concrete implementation
class SimpleBanner(Banner):
    def display(self) -> str:
        return self._text
```

### Example 2: Encapsulation

```python
class Banner(ABC):
    def __init__(self, text: str):
        self._text = text  # Protected attribute
    
    @property
    def text(self) -> str:
        return self._text  # Controlled access
    
    @text.setter
    def text(self, value: str):
        self._text = value  # Controlled modification
```

### Example 3: Polymorphism

```python
banners = [
    SimpleBanner("Hello"),
    BorderedBanner("Hello"),
    FramedBanner("Hello")
]

# Same method, different behaviors
for banner in banners:
    print(banner.display())  # Each displays differently
```

### Example 4: Factory Pattern

```python
# Encapsulates object creation logic
banner = BannerFactory.create_banner('bordered', 'Hello', border_char='*')
```

### Example 5: Decorator Pattern

```python
# Add functionality dynamically
banner = SimpleBanner("Hello")
decorated = PaddedDecorator(banner)
more_decorated = PrefixDecorator(decorated, prefix=">>> ")
```

## 🎯 Learning Path

1. **Start with `src/banner.py`** - Understand abstraction and encapsulation
2. **Explore `src/banner_types.py`** - See inheritance and polymorphism
3. **Study `src/banner_factory.py`** - Learn the factory pattern
4. **Review `src/decorators.py`** - Understand the decorator pattern
5. **Run `main.py`** - See all concepts in action
6. **Read `tests/test_banners.py`** - Learn how to test OOP code

## 🛠️ Extending the Project

### Adding a New Banner Type

```python
from src.banner import Banner

class MyCustomBanner(Banner):
    def display(self) -> str:
        # Your custom implementation
        return f"*** {self._text} ***"

# Register with factory (optional)
BannerFactory.register_banner_type('custom', MyCustomBanner)
```

### Creating a New Decorator

```python
from src.decorators import BannerDecorator

class MyDecorator(BannerDecorator):
    def display(self) -> str:
        original = self._wrapped_banner.display()
        # Add your decoration logic
        return f">> {original} <<"
```

## 📝 Key Takeaways

- **Abstraction** helps define clear contracts and interfaces
- **Encapsulation** protects internal state and provides controlled access
- **Inheritance** promotes code reuse and establishes relationships
- **Polymorphism** enables flexible and extensible code
- **Design Patterns** provide proven solutions to common problems

## 🤝 Contributing

This is a learning project. Feel free to:
- Add new banner types
- Implement additional decorators
- Improve documentation
- Add more tests
- Suggest new features that demonstrate OOP concepts

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as an educational project to demonstrate Object-Oriented Programming principles.

---

**Happy Learning! 🎉**

For questions or suggestions, please open an issue on GitHub.