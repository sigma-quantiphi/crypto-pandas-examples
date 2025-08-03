import os

import ccxt
from crypto_pandas.ccxt.ccxt_pandas_exchange import CCXTPandasExchange
from dotenv import load_dotenv

load_dotenv()
bybit = ccxt.bybit({
    'apiKey': os.getenv("BYBIT_DEMO_API_KEY"),
    'secret':  os.getenv("BYBIT_DEMO_API_SECRET"),
})
bybit = CCXTPandasExchange(exchange=bybit)
bybit_currencies = bybit.fetch_currencies()
print(bybit_currencies)

okx = ccxt.okx({
    'apiKey': os.getenv("OKX_DEMO_API_KEY"),
    'secret':  os.getenv("OKX_DEMO_API_SECRET"),
    'password':  os.getenv("OKX_DEMO_API_PASSWORD"),
})
okx = CCXTPandasExchange(exchange=okx)
okx_currencies = okx.fetch_currencies()
print(okx_currencies)