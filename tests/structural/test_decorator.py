import unittest

from design_patterns.structural.decorator import Decorator


class DecoratorTestCase(unittest.TestCase):

    def test_00_init_decorator(self):
        DecoratorTestCase.decorator = Decorator()


if __name__ == '__main__':
    unittest.main()
