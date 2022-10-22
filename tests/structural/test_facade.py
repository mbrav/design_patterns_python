import unittest

from design_patterns.structural.facade import Facade


class FacadeTestCase(unittest.TestCase):

    def test_00_init_facade(self):
        FacadeTestCase.facade = Facade()


if __name__ == '__main__':
    unittest.main()
