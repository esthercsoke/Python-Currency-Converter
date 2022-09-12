import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """  
    # function to test if class in instanciated correclty
    def test_class_init(self):
        currency = CurrencyConverter('AUD', 'USD', '2020-02-01')
        self.assertEqual(currency.from_currency, 'AUD')
        self.assertEqual(currency.to_currency, 'USD')
        self.assertEqual(currency.date, '2020-02-01')

    
class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    # Test if system exit on invalud currency
    def test_check_currency(self):
        # iniated class
        currency = CurrencyConverter('AUD', 'NOT A CURRENCY', '2020-02-01')
        # check for system exit
        self.assertRaises(SystemExit, currency.check_currencies)
        
    # test error handling on two currency errors 
    def test_incorrect_currencies(self):
        #iniate class
        currency = CurrencyConverter('NOT A CURRENCY', 'ALSO NOT A CURRENCY', '2020-02-01')
        # check if incorrect curries return system exit in currency api check
        self.assertRaises(SystemExit, currency.check_currencies)
    
        
class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    # test if reverse rate is correct
    def test_reversed_rate(self):
        # iniate class
        self.currency_converter = CurrencyConverter('GBP', 'AUD', '2021-01-01')
        # set arguments to test against
        self.currency_converter.amount = 1
        self.currency_converter.rate = 1.8649
        # use reverse_rate function
        self.currency_converter.reverse_rate()
        # compare results
        self.assertEqual(self.currency_converter.inverse_rate, 0.5362)
    
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    # function to test if round_rate is rounding to correct 4 decimal points
    def test_round(self):
        # create testing rounding numbr
        test_number = 4.45553
        # iniated class
        currency = CurrencyConverter('AUD', 'USD', '2020-02-01')
        # use round_rate function on test_number
        test_rounding = currency.round_rate(test_number)
        # compare with function in currencyConverter
        self.assertAlmostEqual(test_rounding, 4.4555, places=4, msg=None)
        
class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
 # TO DO
    
if __name__ == '__main__':
    unittest.main()