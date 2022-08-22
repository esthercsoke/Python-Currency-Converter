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
        self.api = Frankfurter()
        self.rate : float = None
        self.inverse_rate : float = None
        self.amount : float = 0



    def check_currencies(self):
        self.api.get_currencies_list()
        self.api.check_currency(self.from_currency)
        self.api.check_currency(self.to_currency)
        
        
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

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

    def reverse_rate(self):
        self.inverse_rate = 1/self.amount
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
        
       

    def round_rate(self, rate):
        self.rate = round(rate, 4)
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

       

    def get_historical_rate(self):
        # call API _ get historical conversion rate for currencies
        resp = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date)
        # get json
        resp_json = resp.json()

        
        ## GET NESTED RATE VALUE
        # help https://stackoverflow.com/questions/64551176/dictionary-values-inside-an-unknown-key
        for x in resp_json['rates']:
            self.amount = resp_json['rates'][x]
            break
        
        self.reverse_rate()
        
        self.round_rate(self.inverse_rate)
        

        print(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.amount}. The inverse rate was {self.rate}")
        

    
        
        # round currencies
        
        
        # calcuate inverse rate
        

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

        # => To be filled by student
        
        
        # EXAMPLE: The conversion rate on 2021-07-16 from GBP to AUD was 1.8649. The inverse rate was 0.5362