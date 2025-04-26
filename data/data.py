import httpx
import polars as pl

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=aud&from=1716127200&to=1745157600"

headers = {"accept": "application/json"}

response = httpx.get(url, headers=headers)

data = response.json()

df = pl.DataFrame(data["prices"], schema=["timestamp", "price"])

df.write_parquet("raw_data.parquet")
