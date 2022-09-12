import unittest
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """
#  
    def test_base_url(self):
        # initiate class
        frank = Frankfurter()
        # set base url
        base = 'https://www.frankfurter.app/'
        # set currencies url
        currencies = 'https://www.frankfurter.app/currencies'
        # check if base variable is equal to attribute base_url
        self.assertEqual(base, frank.base_url)
        # check if currencies variable is equal to attribute currencies_url
        self.assertEqual(currencies, frank.currencies_url)
        
       
class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """
   
   # Test whether currencies atrtribute is of type list
    def test_currencies_type(self):
        # initalise frankfurther() class
        frankfurter_test = Frankfurter()
        # create fake list and check type
        test_list = ['wrong input', 'wrong input']
        # check if currencies is list type
        self.assertEqual(type(frankfurter_test.currencies), type(test_list)) 
        # test is currencies attribute is not empty
        self.assertIsNotNone(frankfurter_test.currencies)
        
     

class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    
    # check for invalid currency
    def test_invalid_currency(self):
        frankfurter_test = Frankfurter()
        # create invalud currency input for check_currency method
        wrong_currency = frankfurter_test.check_currency('wrong_currency')
        # check if returns false
        self.assertFalse(wrong_currency)


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    # test if get_historical rate method returns api response 200
    def test_histroy_rate_api(self):
        # iniated class
        frankfurter_class = Frankfurter()
        # assign class arguments
        from_currency = 'GBP'
        to_currency = 'AUD'
        date = '2021-01-01'
        # check if status code of get_historical rate API GEt request = 200
        self.assertEqual(frankfurter_class.get_historical_rate(from_currency, to_currency, date).status_code, 200)
               
if __name__ == '__main__':
    unittest.main()