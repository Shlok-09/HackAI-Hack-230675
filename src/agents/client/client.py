from uagents import Agent,Context,Protocol
from messages import *
from utils import convert
from agents.fetcher import fetcher
from messages import Notification
from utils.email import send_email


# User Input

base_currency = input("Enter The Base Currency: ") # Format e.g. USD
target_currencies = input("Enter The Currencies To Be Converted: ") # Format e.g. INR EUR
max_threshold = input("Enter Maximum Limit For The Given Currencies: ") # Format e.g. 45 50 70
min_threshold = input("Enter Minimum Limit For The Given Currencies: ") # Format e.g. 1 9 11

target_currencies, min_threshold, max_threshold = convert(target_currencies, min_threshold, max_threshold)

'''

    The Client Agent is responsible and will send requests at intervals to Fetcher agent after the rates are received and the rates and alerts will be displayed.

'''

client = Agent(name="Client Agent")

@client.on_interval(period=45.0, messages= FetchRequest)
async def fetch_rates(ctx: Context):

    await ctx.send(fetcher.address, FetchRequest(base_currency=base_currency, target_currencies=target_currencies)
)

@client.on_message(FetchResponse)
async def print_rates(ctx: Context,_sender: str, msg: FetchResponse):

    '''

        This is Responsible for displaying and printing the result obtained using the values from Client Agent and 
        the results fetched from the Fetcher Agent.

    '''
    if msg.success:

        '''

            This Displays the obtained results and displays it in the log for viewing the result.
        
        '''

        ctx.logger.info(f"The Rates for currencies are: {msg.rates} for the base currency of {base_currency}")
        
        for i in msg.rates.keys():
            if (msg.rates[i] >= max_threshold[i]):
                alert_msg = f"ALERT!!! ALERT!!! The Currency of {i} crossed Maximum Limit of {max_threshold[i]}."
                
                ctx.logger.critical(alert_msg)
            elif (msg.rates[i]<=min_threshold[i]):
                alert_msg = f"ALERT!!! ALERT!!! The Currency of {i} crossed Minimum Limit of {min_threshold[i]}."
                ctx.logger.critical(alert_msg)
            
    else:
        ctx.logger.error("Results Not Being Fetched.")


# Create a protocol for notifications
notify_protocol = Protocol("Notify")


# Function to handle incoming notifications requests
@notify_protocol.on_message(model=Notification)
async def send_notification(ctx: Context, sender: str, msg: Notification):
    # context = generate_context(msg)
    success, data = await send_email(msg.name, msg.email, ctx)
    if success:
        ctx.logger.info("Email sent successfully")
    else:
        ctx.logger.error(f"Error sending email: {data}")

client.include(notify_protocol)