from api import call_get


class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints.
    It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    
    def __init__(self):
        self.base_url : str = "https://www.frankfurter.app/"
        self.currencies_url: str = 'https://www.frankfurter.app/currencies'
        self.historical_url : str = 'https://api.frankfurter.app/'
        self.currencies = None
       
     
    
 # Method that will get the list of available currencies and returns it as a Python list.

    def get_currencies_list(self):
        currency_call = call_get(self.currencies_url)
        currency_call_json = currency_call.json()
        self.currencies = [key for key in currency_call_json]
      

     # get currency string - go across list and see if vali
     # Method that will check if a provided currency code is valid and return True if that is the case.
     # Otherwise it will return False.
        
    def check_currency(self, currency):
        if currency in self.currencies:
            return True
        else:
            return False
            
           
        
    def get_historical_rate(self, from_currency, to_currency, date, amount=1):
        # make api call using custom date and return requests.models.response object
        try:
            call = call_get(self.historical_url+date+"?from="+from_currency+"&to="+to_currency)
            return call
        except:
            print("ERROR")
        