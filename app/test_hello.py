import unittest
from hello import hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(hello.say_hello(), "Hello, world!")