from pydantic import BaseModel, Field, AnyUrl
from typing import Optional, List, Generic, TypeVar

T = TypeVar('T')

class CoinBase(BaseModel):
    id: str = Field(..., example="bitcoin")
    symbol: str = Field(..., example="btc")
    name: str = Field(..., example="Bitcoin")

class CoinMarketData(CoinBase):
    current_price: float = Field(..., example=45000.50)
    market_cap: float = Field(..., example=800_000_000_000)
    price_change_percentage_24h: Optional[float] = Field(None, example=2.5)
    image: Optional[AnyUrl] = Field(None, example="https://assets.coingecko.com/coins/images/1/large/bitcoin.png")
    last_updated: str = Field(..., example="2023-09-20T00:00:00Z")

    class Config:
        from_attributes = True

class Category(BaseModel):
    id: str = Field(..., example="decentralized-exchange")