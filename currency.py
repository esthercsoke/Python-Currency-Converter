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
        self.rate : float()
        self.inverse_rate : float()
        self.amount : float()
        self.api = Frankfurter()


    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        # self

        Pseudo-code
        ----------
        # initiate get_currencies_list()
        # if statement to check whether both currencies are in the list of currencies from the API
        # if incorrect - return error message and sys.ext()
        # check if either currency is not in the list of currencies
        # sys.exit and display error message if false

        Returns
        -------
        # => returns boolean (true)
        """
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
        # self

        Pseudo-code
        ----------
        # calculate the inverse rate of self.rate and assign it to a variable
        # round the inverse rate using round_rate()
        # assign to self.inverse_rate attribute

        Returns
        -------
        # attribute self.inverse_rate is updated
        """
 
        inverse_currency = self.amount / self.rate
    
        rounded_inverse = self.round_rate(inverse_currency)

        self.inverse_rate = rounded_inverse
        

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        # => self, rate

        Pseudo-code
        ----------
        # round the argument rate to 4 decimals and return it.

        Returns
        -------
        # => float (4 dec)
        """
        return round(rate, 4)


    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        # => self

        Pseudo-code
        ----------
        # call API _ get historical conversion rate for currencies
        # Once returned, extract json from requests.models.Response object
        # extract value from amount key and assign it to self.amount
        # extract the value from the rates key
        # rount the extracted rate and assign it to self.rate
        # use the reverse_rate() function
        # print out results 
        
        Returns
        -------
        # => string
        """
    
        resp = self.api.get_historical_rate(self.from_currency, self.to_currency, self.date)
        
        resp_json = resp.json()
     
        self.amount = resp_json.get('amount')
        
        extract_rate = resp_json['rates'][self.to_currency]
        
        self.rate = self.round_rate(extract_rate)
      
        self.reverse_rate()
        
        print(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. The inverse rate was {self.inverse_rate}")
        



       
