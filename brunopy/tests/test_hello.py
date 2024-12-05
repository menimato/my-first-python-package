import brunopy
import unittest

class TestHello(unittest.TestCase):

  def test_hello(self):
    self.assertIsInstance(brunopy.hello(), str)