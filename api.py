import requests
import sys

def call_get(url: str) -> requests.models.Response:
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp
    except:
        print("There is an error with Frankfurter API")
 
    
    
    
 # resp = requests.get(url)
    # if resp.status_code == 200:
    #     return resp.json()
    # # return {}
    
# def call_get(url):
#   resp = requests.get(url)
#   if resp.status_code == 200:
#     return resp.json()
#   return {}



    # Function that will call the API endpoint (input parameter) and
    # return its response as a requests.models.Response object
    # In case of an error, the program will exit and display
    # the relevant message provided in the assignment brief



