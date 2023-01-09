import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd

metaTags = [{'name': 'viewport',
             'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5'}]
externalStylesheet = [metaTags]

app = dash.Dash(__name__, external_stylesheets=externalStylesheet)
server = app.server

app.layout = html.Div([

    dcc.Interval(id='date_time',
                 interval=1 * 1000,
                 n_intervals=0),

    html.Div([
        html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('iot.png'),
                                 className='image'),
                        html.Div('IOT Environment Monitoring',
                                 className='title_text')
                    ], className='title_image'),
        ], className='title_background twelve columns')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Sensor location:'),
                    html.Div('Walsall, England', className='location')
                ], className='location_row'),

                html.Div(id='current_time', className='location')
            ], className='location_time')
        ], className='date_time twelve columns')
    ], className='row'),

])


@app.callback(Output('current_time', 'children'),
              [Input('date_time', 'n_intervals')])
def update_graph(n_intervals):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    return [
        html.Div(dt_string),
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
