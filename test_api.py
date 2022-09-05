import unittest
from api import call_get

        
class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    # => To be filled by student
    
    def test_api_success(self):
        url = call_get('https://www.frankfurter.app/latest')
        self.assertEqual(200, url.status_code)
        
    def test_api_system_exit(self):
     self.assertRaises(SystemExit, call_get, 'wjshsjs')
                       
  
if __name__ == '__main__':
    unittest.main()
    
    
