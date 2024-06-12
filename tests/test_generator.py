import unittest
from createPassGenerator.generator import strongPass
from createPassGenerator.exceptions import GetErrorPass

class TestValidation(unittest.TestCase):

    def test_generate_random_string_non_empty(self):
        length = 5  # Esempio di lunghezza non valida
        with self.assertRaises(GetErrorPass) as context:
            strongPass(length)
        
        self.assertEqual(context.exception.message, "La lunghezza della password deve essere almeno 10 caratteri")

if __name__ == '__main__':
    unittest.main()
