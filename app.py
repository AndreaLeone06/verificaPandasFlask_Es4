from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_excel('/workspace/verificaPandasFlask_Es4/milano_housing_02_2_23.xlsx')

quartieri = sorted(df['neighborhood'].unique())

def prezzo_medio(quartiere):
    return round(df[df['neighborhood']==quartiere]['price'].mean(), 2)

@app.route('/')
def home():
    return render_template('home.html', quartieri=quartieri)

@app.route('/price')
def price():
    neighborhoods = list(df['neighborhood'].unique())
    return render_template('price.html', neighborhoods=neighborhoods)

@app.route('/price-result', methods=['POST'])
def price_result():
    neighborhood_selected = request.form['neighborhood']
    result = prezzo_medio(neighborhood_selected)
    return render_template('price-result.html', neighborhood_selected=neighborhood_selected, result=result)

def convert(amount, exchange_rate):
    return round(amount * exchange_rate, 2)

@app.route('/price-convert')
def price_convert():
    return render_template('priceConvertito.html')

@app.route('/price-convert-result', methods=['POST'])
def price_convert_result():
    amount = float(request.form['amount'])
    exchange_rate = float(request.form['exchange_rate'])
    currency = request.form['currency']
    result = convert(amount, exchange_rate)
    return render_template('price-convert-result.html', amount=amount, exchange_rate=exchange_rate, currency=currency, result=result)

if __name__ == '__main__':
    app.run(debug=True)