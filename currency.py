import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):
        self.from_currency : str = from_currency
        self.to_currency : str = to_currency
        self.date : str = date
        self.rate : float = None
        self.inverse_rate : float = None
        self.amount : float = 0
        self.api = Frankfurter()


    def check_currencies(self):
        self.api.get_currencies_list()
        
 
        if self.api.check_currency(self.from_currency) is False and self.api.check_currency(self.to_currency) is False:
            print(f'{self.from_currency} and {self.to_currency} is not a valid curreny code')
            sys.exit(0)
              
        if self.api.check_currency(self.from_currency) is False:
            print(f'{self.from_currency} is not a valid curreny code')
            sys.exit(0)
        elif self.api.check_currency(self.to_currency) is False:
            print(f'{self.to_currency} is not a valid curreny code')
            sys.exit(0)
        return True
        
     
       

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """
        # => To be filled by student
        self.inverse_rate = 1/self.amount
        
       

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """
        self.rate = round(rate, 4)

       

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """
        # call API _ get historical conversion rate for currencies
        resp = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date)
        # get json
        resp_json = resp.json()
        
        self.amount = resp_json['rates'][self.to_currency]
        
        self.reverse_rate()
        
        self.round_rate(self.inverse_rate)
        
        print(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.amount}. The inverse rate was {self.rate}")
        

 
        ## GET NESTED RATE VALUE
        # help https://stackoverflow.com/questions/64551176/dictionary-values-inside-an-unknown-key
        # for x in resp_json['rates']:
        #     self.amount = resp_json['rates'][x]
        #     print(self.amount)
        #     break
        

       
