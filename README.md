## Task
Create a JSON API response that provides Bitcoin's USD price from 3 exchanges live.

## API GET URL: 
```
./fetch_all_exchanges/
```

## Requirements:
Fetch live BTC-USD prices from the following exchanges:
1. Coinbase: https://api.coinbase.com/v2/prices/spot?currency=USD
2. Coindesk: https://api.coindesk.com/v1/bpi/currentprice.json
3. Coincap: https://api.coincap.io/v2/assets

## Output:
A sorted JSON list of all exchanges, ordered by USD price. A second part of the JSON output specifies the exchange with the highest price and the exchange with the lowest price by name.

## Bonus:
Optimize for clean and readable code with comments explaining each function. Use a Key-Value Array to sort the prices in a scalable manner, allowing easy addition of more exchanges without rewriting the sort function.

## Steps to Execute:
1. Clone the repository:
```
git clone https://github.com/MohapatraShibu/bitcoin_price_exchange.git
cd bitcoin_price_exchange
```
2. Create a virtual environment:
```
python -m venv env
```
3. Activate the environment:
* On Windows:
  ```
  .\env\Scripts\activate
  ```
* On macOS/Linux:
  ```
  source env/bin/activate
  ```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Run the application:
```
python -m uvicorn demo:app --reload
```
6. Test the API: Use the following curl command to fetch live Bitcoin prices:
```
curl http://127.0.0.1:8000/fetch_all_exchanges/
```
