"""
Unit tests for the OOPS Banner App
"""
import unittest
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
from src.banner_factory import BannerFactory
from src.decorators import PaddedDecorator, PrefixDecorator, NumberedDecorator


class TestBannerBase(unittest.TestCase):
    """Test the base Banner class"""
    
    def test_cannot_instantiate_abstract_class(self):
        """Test that Banner abstract class cannot be instantiated"""
        with self.assertRaises(TypeError):
            Banner("test")
    
    def test_text_property(self):
        """Test text property getter"""
        banner = SimpleBanner("Hello")
        self.assertEqual(banner.text, "Hello")
    
    def test_text_setter(self):
        """Test text property setter"""
        banner = SimpleBanner("Hello")
        banner.text = "World"
        self.assertEqual(banner.text, "World")
    
    def test_width_property(self):
        """Test width property"""
        banner = SimpleBanner("Hello")
        self.assertEqual(banner.width, 5)
        banner.text = "Hello World"
        self.assertEqual(banner.width, 11)


class TestSimpleBanner(unittest.TestCase):
    """Test SimpleBanner class"""
    
    def test_display(self):
        """Test simple banner display"""
        banner = SimpleBanner("Test")
        self.assertEqual(banner.display(), "Test")
    
    def test_empty_text(self):
        """Test with empty text"""
        banner = SimpleBanner("")
        self.assertEqual(banner.display(), "")


class TestBorderedBanner(unittest.TestCase):
    """Test BorderedBanner class"""
    
    def test_display_default_border(self):
        """Test bordered banner with default border"""
        banner = BorderedBanner("Hi")
        expected = "******\n* Hi *\n******"
        self.assertEqual(banner.display(), expected)
    
    def test_display_custom_border(self):
        """Test bordered banner with custom border"""
        banner = BorderedBanner("Hi", border_char='#')
        expected = "######\n# Hi #\n######"
        self.assertEqual(banner.display(), expected)


class TestFramedBanner(unittest.TestCase):
    """Test FramedBanner class"""
    
    def test_display(self):
        """Test framed banner display"""
        banner = FramedBanner("OK")
        expected = "╔════╗\n║ OK ║\n╚════╝"
        self.assertEqual(banner.display(), expected)


class TestDoubleBorderedBanner(unittest.TestCase):
    """Test DoubleBorderedBanner class"""
    
    def test_display(self):
        """Test double bordered banner display"""
        banner = DoubleBorderedBanner("Go")
        result = banner.display()
        self.assertIn("| Go |", result)
        self.assertIn("=", result)
        self.assertIn("-", result)


class TestCenteredBanner(unittest.TestCase):
    """Test CenteredBanner class"""
    
    def test_display_centered(self):
        """Test centered banner display"""
        banner = CenteredBanner("Hi", total_width=10)
        result = banner.display()
        # Text should be centered
        self.assertIn("Hi", result)
        self.assertTrue(result.startswith(" "))
    
    def test_text_longer_than_width(self):
        """Test when text is longer than specified width"""
        banner = CenteredBanner("Hello World", total_width=5)
        result = banner.display()
        self.assertEqual(result, "Hello World")


class TestUpperCaseBanner(unittest.TestCase):
    """Test UpperCaseBanner class"""
    
    def test_display_uppercase(self):
        """Test uppercase banner display"""
        banner = UpperCaseBanner("hello")
        self.assertEqual(banner.display(), "HELLO")


class TestReversedBanner(unittest.TestCase):
    """Test ReversedBanner class"""
    
    def test_display_reversed(self):
        """Test reversed banner display"""
        banner = ReversedBanner("hello")
        self.assertEqual(banner.display(), "olleh")


class TestBannerFactory(unittest.TestCase):
    """Test BannerFactory class"""
    
    def test_create_simple_banner(self):
        """Test creating simple banner via factory"""
        banner = BannerFactory.create_banner('simple', 'Test')
        self.assertIsInstance(banner, SimpleBanner)
        self.assertEqual(banner.display(), 'Test')
    
    def test_create_bordered_banner(self):
        """Test creating bordered banner via factory"""
        banner = BannerFactory.create_banner('bordered', 'Hi')
        self.assertIsInstance(banner, BorderedBanner)
    
    def test_create_bordered_with_kwargs(self):
        """Test creating bordered banner with kwargs"""
        banner = BannerFactory.create_banner('bordered', 'Hi', border_char='@')
        result = banner.display()
        self.assertIn('@', result)
    
    def test_invalid_type(self):
        """Test creating banner with invalid type"""
        banner = BannerFactory.create_banner('invalid', 'Test')
        self.assertIsNone(banner)
    
    def test_get_available_types(self):
        """Test getting available banner types"""
        types = BannerFactory.get_available_types()
        self.assertIn('simple', types)
        self.assertIn('bordered', types)
        self.assertIn('framed', types)
    
    def test_register_banner_type(self):
        """Test registering a new banner type"""
        class CustomBanner(Banner):
            def display(self):
                return f"CUSTOM: {self._text}"
        
        BannerFactory.register_banner_type('custom', CustomBanner)
        banner = BannerFactory.create_banner('custom', 'Test')
        self.assertEqual(banner.display(), "CUSTOM: Test")


class TestDecorators(unittest.TestCase):
    """Test Decorator classes"""
    
    def test_padded_decorator(self):
        """Test padded decorator"""
        banner = SimpleBanner("Test")
        decorated = PaddedDecorator(banner, padding=1)
        result = decorated.display()
        self.assertTrue(result.startswith("\n"))
        self.assertTrue(result.endswith("\n"))
        self.assertIn("Test", result)
    
    def test_prefix_decorator(self):
        """Test prefix decorator"""
        banner = SimpleBanner("Test")
        decorated = PrefixDecorator(banner, prefix=">> ")
        result = decorated.display()
        self.assertEqual(result, ">> Test")
    
    def test_numbered_decorator(self):
        """Test numbered decorator"""
        banner = BorderedBanner("Hi")
        decorated = NumberedDecorator(banner)
        result = decorated.display()
        self.assertIn("1.", result)
        self.assertIn("2.", result)
        self.assertIn("3.", result)
    
    def test_decorator_chaining(self):
        """Test chaining multiple decorators"""
        banner = SimpleBanner("Test")
        decorated = PrefixDecorator(PaddedDecorator(banner), prefix="-> ")
        result = decorated.display()
        self.assertIn("Test", result)
        self.assertIn("->", result)


class TestPolymorphism(unittest.TestCase):
    """Test polymorphic behavior"""
    
    def test_polymorphic_display(self):
        """Test that all banner types can be used polymorphically"""
        banners = [
            SimpleBanner("Test"),
            BorderedBanner("Test"),
            FramedBanner("Test"),
            UpperCaseBanner("Test"),
        ]
        
        # All should have display method that returns string
        for banner in banners:
            result = banner.display()
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()
