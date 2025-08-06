import asyncio
import ccxt.pro
from crypto_pandas.ccxt.async_ccxt_pandas_exchange import AsyncCCXTPandasExchange

ex = AsyncCCXTPandasExchange(exchange=ccxt.pro.binance())


async def main():
    try:
        while True:
            df = await ex.watchLiquidationsForSymbols()
            print(df)
    except KeyboardInterrupt:
        await ex.close()
        print("Stopped by user.")
    except Exception as e:
        await ex.close()
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
