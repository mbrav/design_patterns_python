import unittest

from design_patterns.creational.prototype import Prototype


class PrototypeTestCase(unittest.TestCase):

    def test_00_init_prototype(self):
        PrototypeTestCase.prototype = Prototype()


if __name__ == '__main__':
    unittest.main()
