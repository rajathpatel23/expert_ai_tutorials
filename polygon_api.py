import time
from polygon import WebSocketClient, STOCKS_CLUSTER
import pdb

def my_custom_process_message(message):
    print("this is my custom message processing", message)

def my_custom_error_handler(ws, error):
    print("this is the custom error handler ", error)

def my_custom_close_handler(ws):
    print("this is my custom close handler")

def main():
    key = 'lNLeiwhybLagDs2vMvZiCral9f8ijISt'
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_custom_error_handler)
    my_client.run_async()
    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(1)
    my_client.close_connection()



# from polygon import RESTClient


# def main():
#     key = "lNLeiwhybLagDs2vMvZiCral9f8ijISt"

#     # RESTClient can be used as a context manager to facilitate closing the underlying http session
#     # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
#     with RESTClient(key) as client:
#         resp = client.stocks_equities_daily_open_close("AAPL", "2021-03-04")
#         print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")




import datetime

from polygon import RESTClient


# def ts_to_datetime(ts) -> str:
#     return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


# def main():
#     key = "lNLeiwhybLagDs2vMvZiCral9f8ijISt"

#     # RESTClient can be used as a context manager to facilitate closing the underlying http session
#     # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
#     with RESTClient(key) as client:
#         from_ = "2021-05-01"
#         to = "2021-05-02"
#         resp = client.stocks_equities_aggregates("AAPL", 1, "minute", from_, to, unadjusted=False)
#         if resp:
#             print(f"Minute aggregates for {resp.ticker} between {from_} and {to}.")
#             for result in resp.results:
#                 dt = ts_to_datetime(result["t"])
#                 print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")


if __name__ == '__main__':
    main()
