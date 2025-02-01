from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers import coins, health
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Crypto API</title>
        </head>
        <body>
            <h1>Welcome to Crypto API</h1>
            <button onclick="window.location.href='/api/v1/coins'">Go to Coins</button>
        </body>
    </html>
    """

app.include_router(health.router)
app.include_router(coins.router, prefix="/api/v1", tags=["coins"])