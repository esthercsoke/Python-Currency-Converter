import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # args (array)

    Pseudo-code
    ----------
    # check if length of args is equal to 3
    # return args if true
    # else print error message and sys.exit()

    Returns
    -------
    # list of arguments if equal to 3
    """
    if len(args) == 3:
        return args
    else:
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit(0)


def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => date

    Pseudo-code
    ----------
    # check date is in correct format of e.g 2020-01-01
    # if correct date format return True
    # if incorrect -  system exit and print error message
    
    Returns
    -------
    # boolean (true)
    """
    
    try:
        date_check = datetime.datetime.strptime(date, '%Y-%m-%d')  
    except ValueError:
        print("Provided date is invalid")
        sys.exit(0)
    else:
        return True
 
    