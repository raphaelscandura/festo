from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app) 

@app.route('/api/data')
def get_data():
    df = pd.read_csv('products-2000000.csv')
    summary = df.groupby('Category').sum(numeric_only=True).reset_index()
    return jsonify(summary.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5050)