# Class Hierarchy Diagram

```
                                    Banner (ABC)
                                        |
                    +-------------------+-------------------+
                    |                                       |
            Concrete Banners                        BannerDecorator (ABC)
                    |                                       |
        +-----------+-----------+               +-----------+-----------+
        |           |           |               |           |           |
  SimpleBanner  BorderedBanner  |         PaddedDecorator   |    NumberedDecorator
                           FramedBanner              PrefixDecorator
                                 |
                    +------------+------------+
                    |            |            |
            DoubleBorderedBanner |     ReversedBanner
                          CenteredBanner
                                 |
                          UpperCaseBanner
```

## Detailed Class Structure

### Abstract Base Class
- **Banner** (ABC)
  - Abstract method: `display()`
  - Protected attributes: `_text`, `_width`
  - Properties: `text` (getter/setter), `width` (getter)
  - Private method: `_calculate_width()`

### Concrete Banner Classes (Inheritance)
1. **SimpleBanner**
   - Displays plain text
   - Minimal implementation

2. **BorderedBanner**
   - Adds customizable borders around text
   - Additional parameter: `border_char`

3. **FramedBanner**
   - Decorative Unicode frame
   - Uses box-drawing characters

4. **DoubleBorderedBanner**
   - Nested borders with different characters
   - More complex display logic

5. **CenteredBanner**
   - Centers text within specified width
   - Additional parameter: `total_width`

6. **UpperCaseBanner**
   - Transforms text to uppercase
   - Text transformation example

7. **ReversedBanner**
   - Reverses text
   - String manipulation example

### Decorator Classes (Composition)
- **BannerDecorator** (ABC)
  - Wraps another Banner object
  - Maintains Banner interface
  
  1. **PaddedDecorator**
     - Adds blank lines around banner
     - Parameter: `padding` (number of lines)
  
  2. **PrefixDecorator**
     - Adds prefix to each line
     - Parameter: `prefix` (string)
  
  3. **NumberedDecorator**
     - Adds line numbers
     - No additional parameters

### Factory Class
- **BannerFactory**
  - Static registry of banner types
  - `create_banner()` - Factory method
  - `get_available_types()` - Lists available types
  - `register_banner_type()` - Adds custom types

## Relationships

### Inheritance (IS-A)
- SimpleBanner IS-A Banner
- BorderedBanner IS-A Banner
- BannerDecorator IS-A Banner
- PaddedDecorator IS-A BannerDecorator

### Composition (HAS-A)
- BannerDecorator HAS-A Banner (wrapped)
- PaddedDecorator HAS-A Banner (through BannerDecorator)

### Association
- BannerFactory CREATES Banner instances
- Main application USES Banner instances

## Method Resolution Order (MRO) Examples

### SimpleBanner
```
SimpleBanner -> Banner -> ABC -> object
```

### PaddedDecorator
```
PaddedDecorator -> BannerDecorator -> Banner -> ABC -> object
```

## Design Pattern Usage

### Factory Pattern
```
Client Code
     |
     v
BannerFactory.create_banner()
     |
     v
Concrete Banner Instance
```

### Decorator Pattern
```
Base Banner
     |
     v
Decorator 1 (wraps Base)
     |
     v
Decorator 2 (wraps Decorator 1)
     |
     v
Final Decorated Banner
```

## Polymorphic Usage Example

```python
# All these objects can be used interchangeably
banners: List[Banner] = [
    SimpleBanner("Hello"),
    BorderedBanner("Hello"),
    FramedBanner("Hello"),
    PaddedDecorator(SimpleBanner("Hello"))
]

# Same interface, different behaviors
for banner in banners:
    print(banner.display())  # Polymorphism in action!
```

## Extension Points

### Adding New Banner Types
1. Inherit from `Banner`
2. Implement `display()` method
3. Optionally register with `BannerFactory`

### Adding New Decorators
1. Inherit from `BannerDecorator`
2. Override `display()` method
3. Can access wrapped banner via `self._wrapped_banner`

### Custom Factory Extensions
1. Use `BannerFactory.register_banner_type()`
2. Or create a new factory class inheriting from `BannerFactory`
