import unittest
from api import call_get

        
class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    # method to test url success status code of 200
    def test_api_success(self):
        url = call_get('https://www.frankfurter.app/latest')
        self.assertEqual(200, url.status_code)
        
    # method to test if except raises error
    def test_api_system_exit(self):
     test = self.assertRaises(SystemExit, call_get, 'jibberish')
                    
if __name__ == '__main__':
    unittest.main()
    
    
