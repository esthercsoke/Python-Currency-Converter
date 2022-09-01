import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date


if __name__ == "__main__":
    print("Launching App")
    # Remove the first argument (name of Python script)
    args = sys.argv[1:]
    
   #  Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
    check_arguments(args)
    
    # Check the validity of the input date (using your defined check_date() function)
    date = args[0]
    
    check_date(date)
    
    from_currency = args[1]
    to_currency = args[2]

    # Instantiate an objet from your defined CurrencyConverter class with the verified 2 currency codes and date
    conversion = CurrencyConverter( from_currency, to_currency, date)
    
    # Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
    conversion.check_currencies()
    
    # Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
    conversion.get_historical_rate()
   