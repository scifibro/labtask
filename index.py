from dash import dcc, html
from dash.dependencies import Input, Output


from app import app
from apps import task_app, additional_app
# main page

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Task Visualization|', href='/apps/task_app'),
        dcc.Link('Additional Visualization', href='/apps/additional_app', style={"margin-left": "15px"}),
    ]),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/task_app':
        return task_app.layout
    if pathname == '/apps/additional_app':
        return additional_app.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)