import unittest

from design_patterns.structural.composite import Composite


class CompositeTestCase(unittest.TestCase):

    def test_00_init_composite(self):
        CompositeTestCase.composite = Composite()


if __name__ == '__main__':
    unittest.main()
