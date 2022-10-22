import unittest

from design_patterns.structural.adapter import Adapter


class AdapterTestCase(unittest.TestCase):

    def test_00_init_adapter(self):
        AdapterTestCase.adapter = Adapter()


if __name__ == '__main__':
    unittest.main()
