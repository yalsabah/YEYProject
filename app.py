from flask import Flask, jsonify, request
from alpha_vantage.timeseries import TimeSeries

app = Flask(__name__)

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_stock_data(self, symbol):
        ts = TimeSeries(key=self.api_key, output_format='json')
        data, meta_data = ts.get_quote_endpoint(symbol=symbol)

        return data

@app.route('/stock_data', methods=['GET'])
def get_stock_data():#lol
    symbol = request.args.get('symbol')

    if not symbol:
        return jsonify({"error": "Symbol is required."}), 400 # the 400 is just a HTTP status code for error responses 

    api_key = "IFPFVXYN60X0PEQW"  # API key allows us to acess the api Aplha vantage is just one api that allows us to acess stocks for free 
    api = AlphaVantageAPI(api_key)
    stock_data = api.get_stock_data(symbol)

    if stock_data:
        return jsonify(stock_data)
    else:
        return jsonify({"error": "Failed to fetch data for the given symbol."}), 404

if __name__ == '__main__':
    app.run(debug=True)
