import unittest

from design_patterns.structural.flyweight import Flyweight


class FlyweightTestCase(unittest.TestCase):

    def test_00_init_flyweight(self):
        FlyweightTestCase.flyweight = Flyweight()


if __name__ == '__main__':
    unittest.main()
