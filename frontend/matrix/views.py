from django.shortcuts import render
import plotly.express as px
import pandas as pd
import requests

# Create your views here.
def index(request):
    return render(request, 'matrix/index.html')

def matrix_scatter_plot(request):

    matrix_json = requests.get('http://localhost:5000/api/matrix').json()

    matrix_data = pd.read_json(matrix_json, orient='split')

    max_spend = matrix_data["Spend"].max()

    fig = px.scatter(matrix_data["Share of wallet"], matrix_data["EBIT-margin"], size=matrix_data["Spend"] / max_spend)

    return render(request, 'matrix/matrix_scatter_plot.html', context={'plot_div': fig.to_html(full_html=False)})