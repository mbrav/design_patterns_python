import unittest

from design_patterns.structural.proxy import Proxy


class ProxyTestCase(unittest.TestCase):

    def test_00_init_proxy(self):
        ProxyTestCase.proxy = Proxy()


if __name__ == '__main__':
    unittest.main()
