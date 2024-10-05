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

    fig = px.scatter(x=matrix_data["Share of wallet"], y=100*matrix_data["EBIT-margin"], size=.02 + matrix_data["Spend"] / max_spend, log_x=True)

    fig.update_layout(
        xaxis_title="Share of wallet",
        yaxis_title="EBIT-margin (%)"
    )

    return render(request, 'matrix/matrix_scatter_plot.html', context={'plot_div': fig.to_html(full_html=False)})