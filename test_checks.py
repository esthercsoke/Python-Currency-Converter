import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    def test_incorrect_arg(self):
        expected = ['1', '2', '3']
        wrong_input = ['1', '2', '3']
        result = check_arguments(expected) 
        self.assertEqual(result, len(wrong_input))
    

class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    # => To be filled by student
    def test_date_arg(self):
        expected = '2022-01-01'
        wrong_date = '2022/01/01'
        result = check_date(expected) 
        self.assertNotEqual(result, wrong_date)
    

if __name__ == '__main__':
    unittest.main()