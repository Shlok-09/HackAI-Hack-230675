from uagents import Agent,Context
from utils import rate_convert
from messages import *


fetcher = Agent(name="Fetcher Agent")

@fetcher.on_message(FetchRequest,replies={FetchResponse})
async def fetch_rates(ctx: Context,sender: str,msg: FetchRequest):
    '''

    Defining the working and operation of the Fetcher Agent.

    '''
    try:
        rates = rate_convert(msg.target_currencies,msg.base_currency)
        await ctx.send(sender, FetchResponse(success=True,rates=rates))
    except:
        ctx.send(sender,FetchResponse(success=False,rates={}))
    
