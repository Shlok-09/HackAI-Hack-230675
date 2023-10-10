from agents import fetcher, client
from uagents import Bureau


if __name__ == "__main__":
    b = Bureau()
    b.add(fetcher.fetcher)
    b.add(client.client)
    b.run()