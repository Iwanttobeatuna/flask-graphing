from flask import Flask, render_template
import json
import plotly
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
import investpy
import pandas as pd

import numpy as np

app = Flask(__name__)

@app.route('/')
def line():

    df = investpy.get_stock_recent_data(stock="AAPL", country='United States', as_json=False, order='descending')
    df.to_csv('file.csv',index=True, encoding='utf-8')
    csv_file = 'file.csv'
    df = pd.read_csv(csv_file)


    # Plot graph
    xscale=df["Date"]
    yscale=df["Close"]
    zscale =df["Volume"]
    # Create a trace
    fig = go.Scatter(
        x = xscale,
        y = yscale
        )

    data =[fig]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # Create a trace
    fig1 = go.Scatter(
        x = xscale,
        y = zscale
        )

    data1 =[fig1]
    graphJSON1 = json.dumps(data1, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('index.html', graphJSON=graphJSON, graphJSON1=graphJSON1)
