import sys
# from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    print("Launching App")
    args = sys.argv[1:]
    check_arguments(args)
    # Check the validity of the input date is YYYY-MM-DD
    date = args[0]
    check_date(date)
    
   
   
    """
    Main logics of the program.
    
    

    Pseudo-code
    ----------
    Extract the input arguments
    Remove the first argument (name of Python script)
    Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
    Check the validity of the input date (using your defined check_date() function)
    Instantiate an objet from your defined CurrencyConverter class with the verified 2 currency codes and date
    Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
    Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
    """
    
    # => To be filled by student
