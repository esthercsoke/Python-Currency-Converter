import requests
import sys
    
    
def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    # => To be filled by student

    Pseudo-code
    ----------
    # Send a GET request to the API url paramater
    # return API response as request.modes.response object
    
    Returns
    -------
    # => To be filled by student
    """
    
    # Send a GET request to the API url paramater
    # return resp as request.modes.response object
    # if error - exit and display error message
    
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp 
    except (requests.exceptions.RequestException,
        ConnectionResetError) as err:
        print("There is an error with Frankfurter API")
        sys.exit(0)
    return {}
        
    



# https://stackoverflow.com/questions/52181161/handling-exceptions-from-python-requests