# Vetty Crypto API 

# URL: https://vetty-crypto-api.onrender.com/

Vetty Crypto API is a FastAPI-based application that provides cryptocurrency market data using the CoinGecko API.

## Features

- Fetch cryptocurrency market data
- Pagination support
- Environment-based configuration

## Requirements

- Python 3.8+
- Docker
- Docker Compose

## Installation

### Using Docker

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/vetty-crypto-api.git
   cd vetty-crypto-api
   ```
2. **Create a .env file in the root directory with the following content**:
```
ENVIRONMENT=development
SECRET_KEY=supersecretkey
COINGECKO_API_URL=https://api.coingecko.com/api/v3
```
3. **Build and start the services**:
```
docker-compose up --build
```
4. **Access the application**:

Open your browser and navigate to http://127.0.0.1:8000.

## Local Development

1. **Clone Repo**

```
git clone https://github.com/rpkumar09/vetty-crypto-api.git
cd vetty-crypto-api
```

2. **Create a Virtual Environment**:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies**:
```
pip install -r requirements.txt
```

4. **Create a .env file in the root directory with the following content**:

```
ENVIRONMENT=development
SECRET_KEY=your-secret-key
COINGECKO_API_URL=https://api.coingecko.com/api/v3
```
5. **Run the application**:

```
uvicorn app.main:app --reload
```

6. **Access the App**:
Open your browser and navigate to http://127.0.0.1:8000.# vetty-crypto-api
