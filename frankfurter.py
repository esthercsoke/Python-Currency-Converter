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
        self.base_url : str = 'https://www.frankfurter.app/'
        self.currencies_url = 'https://www.frankfurter.app/currencies'
        self.historical_url = ''
        self.currencies =  self.get_currencies_list()
       
     
    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        # self

        Pseudo-code
        ----------
        # Send a GET request to Frankfurter /currencies 
        # Extract the json currencies into a list. 

        Returns
        -------
        # A List populated with the available currencies 
    """

        currency_call = call_get(self.currencies_url)
        currency_json = currency_call.json()
        self.currencies = [key for key in currency_json]
        return self.currencies
      
      
    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        # => currency

        Pseudo-code
        ----------
        # Check if currency (string) is in a list of currencies
        # If the currency is present, return true, elese return false. 

        Returns
        -------
        # Boolean of TRUE
        
        """
        if currency in self.currencies:
            return True
        else:
            return False
            
           
    def get_historical_rate(self, from_currency, to_currency, date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. 
        It will return an requests.models.Response object.

        Parameters
        ----------
        # => from_currency, to_currency, from_date, amount

        Pseudo-code
        ----------
        # use call_get function to call the API GET request
        # return as a requests.models.Response object.

        Returns
        -------
        # requests.models.Response object.
        """
        # make api call using custom date and return requests.models.response object
        self.historical_url = self.base_url+date+"?amount="+str(amount)+"&from="+from_currency+"&to="+to_currency
        try:
            call = call_get(self.historical_url)
            return call
        except:
            print("There is an error with Frankfurter API")
    
    