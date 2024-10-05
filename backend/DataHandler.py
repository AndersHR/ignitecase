import json
import pandas as pd

import os


class DataHandler:
        
    def __init__(self):
        self.data_json = self.read_data()

    def read_data(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/data.json') as f:
            data_json = json.load(f)
        return data_json

    def get_matrix(self):
        return pd.DataFrame(self.data_json['rows'][0]['values'], columns=["EBIT-margin", "Share of wallet", "Spend"])
