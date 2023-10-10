import os
import requests


"""
    The following convert function converts the user input.

"""

def convert(secondary, min_threshold, max_threshold):
    s = secondary.split()
    tmin = min_threshold.split()
    tmax = max_threshold.split()

    tmin = [float(i) for i in tmin]
    tmax = [float(i) for i in tmax]

    dmin = dict(zip(s, tmin))
    dmax = dict(zip(s, tmax))

    return s, dmin, dmax


API_KEY = 'YOUR_API_KEY_HERE' # ENTER YOUR API KEY HERE


'''
    The Below rate_convert Function has been created which extracts and fetches the data and the conversion rates from the API.

    It takes in two parameters, i.e., BASE_CURRENCY : Source Currency and CURRENCIES : The Target Currency to which the base currency has to be converted.

'''

def rate_convert(target_currencies,base_currency):
    
    url = f'https://api.currencyapi.com/v3/latest?apikey={API_KEY}&'

    url+=f"base_currency={base_currency}&currencies="
    for i in target_currencies:
        url+=i + ","
    url = url[:-1]
    # print(url)

    """ Fetching the Rates using GET method from the API. """

    response = requests.request("GET", url) 
    print(response.json())

    status_code = response.status_code
    
    assert status_code==200 

    result = response.json()

    """ Returning the results in a specific format. """

    result_dict = {}
    for i in target_currencies:
        result_dict[i] = result["data"][i]["value"]
    return result_dict
    

if __name__=="__main__":
    print(rate_convert(["INR"],"USD"))