from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Initialize the DataHandler
from DataHandler import DataHandler
data_handler = DataHandler()

@app.route('/api/matrix', methods=['GET'])
def get_matrix():
    return jsonify(data_handler.get_matrix().to_json(orient='split'))

if __name__ == '__main__':
    app.run(port=5000)