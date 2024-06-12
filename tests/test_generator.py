import unittest
import random
from createPassGenerator.generator import strongPass
from createPassGenerator.exceptions import GetErrorPass

class TestValidation(unittest.TestCase):

    def test_strongPass(self):
        length = 10
        result = strongPass(length)
        self.assertEqual(len(result), length)
        
        
    def test_generate_random_string_non_empty(self):
        length = 5
        result = strongPass(length)
        self.assertNotEqual(result, "")

    def test_generate_random_string_invalid_length(self):
        with self.assertRaises(ValueError):
            strongPass(0)


if __name__ == "__main__":
    unittest.main()