# app/services/coingecko.py
import httpx
from app.core.config import settings

class CoinGeckoClient:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
    
    async def get_coins_list(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/coins/list")
            return response.json()
    
    async def get_market_data(self, vs_currency: str = "cad", **params):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/coins/markets",
                params={"vs_currency": vs_currency, **params}
            )
            return response.json()