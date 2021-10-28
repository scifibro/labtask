import numpy as np

from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as obj

from app import app
from data.dataframes import regions, get_data_by_region, view_processed


stock_data = view_processed


layout = html.Div(
    children=[
        html.H1(children="Stock Data Charts ", style={'textAlign': 'center'}),
        html.P('Select Region'),
        dcc.Dropdown(
        id='regions-dropdown',
        options=[{"label": x.strip(), "value": x}
                 for x in regions],
         value=regions[0]
         ),
        dcc.Graph(id="temp-plot")

    ]
)


@app.callback(Output("temp-plot", "figure"),
             [Input('regions-dropdown', 'value')])
def add_graph(region):
    df = get_data_by_region(stock_data, region)
    slider_max = df['year'].max()
    slider_min = df['year'].min()
    customdata = np.stack((df['currency'].str.strip(), df['exchange'].str.strip(), df['ind'].str.strip()), axis=-1)

    hovertemplate = 'Price: %{y}<br>Currency:%{customdata[0]}<br>Exchange:%{customdata[1]}<br>Index:%{customdata[2]}<br>Date: %{x}'

    title = {'text': f'Maximum and minimum price graphs for month in {region.strip()} between {slider_min} and {slider_max} years',
             'y': 0.93, 'x': 0.5,
             'xanchor': 'center', 'yanchor': 'top'}

    trace_high = obj.Scatter(x=df["date"], y=df["max_open"], mode="markers", name=f"Maximum price",
                             customdata=customdata,
                             hovertemplate=hovertemplate
                             )
    trace_low = obj.Scatter(x=df["date"], y=df["min_low"], mode="markers", name=f"Minimum price",
                            customdata=customdata,
                            hovertemplate=hovertemplate
                            )

    layout_obj = obj.Layout(xaxis=dict(range=[slider_min, slider_max], title='Year'), yaxis={'title': 'Stock Price'},
                         height=900, width=1450, hovermode='closest', title=title, legend={'title': 'Values'}, font={'size': 15})
    figure = obj.Figure(data=[trace_high, trace_low], layout=layout_obj)
    return figure

