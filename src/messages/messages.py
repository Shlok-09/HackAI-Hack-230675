from uagents import Model
from uagents import Model
from typing import List, Dict, Tuple


'''
The Below FetchRequest is a Message model which will be used for sending the parameteres for fetching from the API.

It contains two parameters, i.e., base_currency: Code of currency whose value is to be converted. Example: INR
target_currencies: Code of currency to whom the value is to be converted. Example: [USD,EUR]

'''

class FetchRequest(Model):

    base_currency: str
    target_currencies: list


'''

This Below FetchResponse is a Message model created for fetching the response.

There are two variables considered i.e., success: Boolean. If fetched successfully then True, Else False. rates: Which returns a dictionary of the name target currency and its value with respect to base currency.

'''
class FetchResponse(Model):

    success: bool
    rates: dict



"""

This Below Notification Model is a Message Model for sending notifcation via Email.
        
"""
class Notification(Model):


    name: str
    email: str
    base_currency: str
    notif: List[Tuple[str, float, float]]

