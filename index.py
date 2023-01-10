import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
import pytz
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

    dcc.Interval(id='update_value',
                 interval=1 * 11000,
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

    html.Div([
        html.Div([
            html.Div([
                html.P('Current', style={'fontWeight': 'bold'}),
                html.Div([
                    html.Div(id='temp'),
                    html.Div(id='hum')
                ], className='image_numeric_row'),
            ], className='image_numeric_column'),
        ], className='temp_humidity twelve columns')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.P('Current', style={'fontWeight': 'bold'}),
                html.Div([
                    html.Div(id='light_intensity'),
                    html.Div(id='co2')
                ], className='image_numeric_row'),
            ], className='image_numeric_column'),
        ], className='light_co2 twelve columns')
    ], className='row')

])


@app.callback(Output('current_time', 'children'),
              [Input('date_time', 'n_intervals')])
def update_time(n_intervals):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    return [
        html.Div(dt_string),
    ]


@app.callback(Output('temp', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    temp = float(3.5)

    return [
        html.Div([
            html.Img(src=app.get_asset_url('temp.png'),
                     style={'height': '50px'}),

            html.Div([
                html.Div('{0:.1f}'.format(temp),
                         className='numeric_value'),
                html.Div('°C', className='symbol')
            ], className='temperature_row')
        ], className='image_temperature'),

        html.P('Temperature', style={'color': '#666666',
                                     'margin-top': '-7px'})
    ]


@app.callback(Output('hum', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    hum = float(90.0)

    return [
        html.Div([
            html.Img(src=app.get_asset_url('humidity.png'),
                     style={'height': '50px'}),

            html.Div([
                html.Div('{0:.1f}'.format(hum),
                         className='numeric_value'),
                html.Div('%', className='symbol')
            ], className='temperature_row')
        ], className='image_temperature'),

        html.P('Humidity', style={'color': '#666666',
                                  'margin-top': '-7px'})
    ]


@app.callback(Output('light_intensity', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    light_inten = float(71.2)

    return [
        html.Div([
            html.Img(src=app.get_asset_url('sun.png'),
                     style={'height': '50px'}),

            html.Div([
                html.Div('{0:.1f}'.format(light_inten),
                         className='numeric_value'),
                html.Div('lux', className='symbol')
            ], className='temperature_row')
        ], className='image_temperature'),

        html.P('Light Intensity', style={'color': '#666666',
                                         'margin-top': '-7px'})
    ]


@app.callback(Output('co2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    co2 = 460

    return [
        html.Div([
            html.Img(src=app.get_asset_url('co2.png'),
                     style={'height': '50px'}),

            html.Div([
                html.Div('{0:.0f}'.format(co2),
                         className='numeric_value'),
                html.Div('PPM', className='symbol')
            ], className='temperature_row')
        ], className='image_temperature'),

        html.P('CO2', style={'color': '#666666',
                             'margin-top': '-7px'})
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
