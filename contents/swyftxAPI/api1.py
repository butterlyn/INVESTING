import requests as rq
import pandas as pd

response_assets = rq.get('https://api.swyftx.com.au/markets/assets/')
response_liverates = rq.get('https://api.swyftx.com.au/live-rates/1/')

print(response_assets.json())

#df_assets = pd.read_json(response_assets.text.json())
#print(df_assets.to_string())
