import datetime
import sys

def check_arguments(args):
 if len(args) != 3:
    print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
    sys.exit(0)
    
    # check if 3 arguments
    # check if arguments are in correct order
    

def check_date(date):
    try:
        date_check = datetime.datetime.strptime(date, '%Y-%m-%d')  
        # print(date_check)
    except:
        print("Provided date is invalid")
        sys.exit(0)

    