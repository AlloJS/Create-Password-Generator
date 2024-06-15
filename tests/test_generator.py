import sys
sys.path.append('insert path absolute')
from createPassGenerator.generator import (
                                        strong_pass,
                                        get_user_data,
                                        save_user_data_to_file,
                                        create_file_excel,
                                        write_to_excel,
                                        read_excel
                                    )
from createPassGenerator.exceptions import GetErrorPass
import openpyxl
import os
import string

import unittest
from unittest.mock import patch



class TestValidation(unittest.TestCase):

    def test_generate_random_string_non_empty(self):
        length = 5 
        with self.assertRaises(GetErrorPass) as context:
            strong_pass(length)
        
        self.assertEqual(context.exception.message, "La lunghezza della password deve essere almeno 10 caratteri")
        
@patch('builtins.input', side_effect=['Twitter', 'user123', '12'])
def test_get_user_data(self, mock_input):
    data = get_user_data()
    self.assertEqual(data['platform'], 'Twitter')
    self.assertEqual(data['username'], 'user123')
    self.assertTrue(len(data['password']) == 12)
    self.assertTrue(all(c in (string.ascii_letters + string.digits + string.punctuation) for c in data['password']))

def test_save_user_data_to_file(self):
    data = {
        "platform": "Twitter",
        "username": "user123",
        "password": "strongP@ssw0rd!"
    }
    filename = "test_account_data.txt"
    save_user_data_to_file(data, filename)

    with open(filename, 'r') as file:
        lines = file.readlines()
        self.assertEqual(lines[0].strip(), "platform: Twitter")
        self.assertEqual(lines[1].strip(), "username: user123")
        self.assertEqual(lines[2].strip(), "password: strongP@ssw0rd!")

    os.remove(filename)

def test_strong_pass(self):
    password = strong_pass(12)
    self.assertEqual(len(password), 12)
    self.assertTrue(all(c in (string.ascii_letters + string.digits + string.punctuation) for c in password))

    with self.assertRaises(ValueError):
        strong_pass(8)
        
def test_create_file_excel(self):
        create_file_excel()
        self.assertTrue(os.path.exists('platforms_account.xlsx'))

def test_write_to_excel(self):
       
    write_to_excel()
    wb = openpyxl.load_workbook('platforms_account.xlsx', data_only=True)
    sheet = wb.active
    last_row = sheet.max_row
    self.assertEqual(last_row, 2)  # Verifica che ci sia una nuova riga aggiunta

def test_read_excel(self):
    read_excel()        


if __name__ == '__main__':
    unittest.main()
