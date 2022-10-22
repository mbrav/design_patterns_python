import unittest

from design_patterns.structural.bridge import Bridge


class BridgeTestCase(unittest.TestCase):

    def test_00_init_bridge(self):
        BridgeTestCase.bridge = Bridge()


if __name__ == '__main__':
    unittest.main()
