# app/routers/coins.py
from fastapi import APIRouter, Depends, Query
from app.services.coingecko import CoinGeckoClient
from app.models.schemas import CoinMarketData

router = APIRouter()
client = CoinGeckoClient()

@router.get("/coins", response_model=list[CoinMarketData])
async def list_coins(
    page_num: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    all_coins = await client.get_market_data(vs_currency="cad")
    start = (page_num - 1) * per_page
    end = start + per_page
    return all_coins[start:end]