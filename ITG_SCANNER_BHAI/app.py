from flask import Flask, render_template, request
from flask_netlify import Netlify

app = Flask(__name__)
netlify = Netlify(app)

# Load stock symbols from CSV file
with open('sc_stocks.csv', 'r') as file:
    stock_symbols = set(row[0] for row in csv.reader(file))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_stock', methods=['POST'])
def check_stock(): 
    stock_name = request.form['stock_name'].upper()

    if stock_name in stock_symbols:
        result = f"The stock '{stock_name}' is Complaint"
    else:
        result = f"The stock '{stock_name}' is NoN Complaint"

    return render_template('index.html', result=result)

# Required for Flask-Netlify
if __name__ == '__main__':
    netlify.run(debug=True)
