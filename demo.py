from fastapi import FastAPI
from routers import exchange_router
import httpx
from typing import Dict, List

app = FastAPI()
@app.get("/fetch_all_exchanges/")
async def fetch_all_exchanges():
    endpoints={
        "Coinbase": "https://api.coinbase.com/v2/prices/spot?currency=USD",
        "Coindesk": "https://api.coindesk.com/v1/bpi/currentprice.json",
        "Coincap": "https://api.coincap.io/v2/assets"
    }
    prices=[]
    
    async with httpx.AsyncClient() as client:
        for name, url in endpoints.items():
            try:
                response=await client.get(url)
                response.raise_for_status()
                data=response.json()

                if name=="Coindesk":
                    price=float(data["bpi"]["USD"]["rate"].replace(",", ""))
                elif name=="Coincap":
                    price=float(data["data"]["priceUSD"])
                elif name=="Coinbase":
                    price=float(data["data"]["amount"])
                
                prices.append({"exchange":name,"price_usd":price})
            except Exception as e:
                prices.append({"exchange":name,"price_usd":None})
                #print(f"error fetching data from {name}:{e}")

    
    prices=[p for p in prices if p["price_usd"] is not None]
    sorted_prices=sorted(prices, key=lambda x: x["price_usd"])
    highest_price=sorted_prices[-1] if sorted_prices else None
    lowest_price=sorted_prices[0] if sorted_prices else None

    response={
        "sorted_prices": sorted_prices,
        "highest_price": highest_price,
        "lowest_price": lowest_price
    }

    return response
