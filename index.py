from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
import dash_bootstrap_components as dbc
from app import app
from contentTabs.tab_one import page_one_layout
from contentTabs.tab_two import page_two_layout
from contentTabs.tab_three import page_three_layout

server = app.server

tab_style = {
    'border-top': 'none',
    'border-bottom': 'none',
    'border-left': 'none',
    'border-right': 'none',
    'backgroundColor': 'rgba(255, 255, 255, 0)',
    'height': '35px',
    'padding': '7.5px',
    'width': 'auto'
}

selected_tab_style = {
    'border-top': 'none',
    'border-bottom': '2px solid blue',
    'border-left': 'none',
    'border-right': 'none',
    'backgroundColor': 'rgba(255, 255, 255, 0)',
    'height': '35px',
    'padding': '7.5px',
    'width': 'auto'
}

app.layout = html.Div([

    dcc.Interval(id='update_value',
                 interval=1 * 16000,
                 n_intervals=0),

    html.Div([
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url('iot.png'),
                         className='image'),
                html.Div('IOT Environment Monitor',
                         className='title_text')
            ], className='title_row')
        ], className='title_background twelve columns')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Sensor location:'),
                    html.Div('Walsall, England', className='location_name')
                ], className='location_row'),
                dbc.Spinner(html.Div(id='data_update_time', className='location_name'))
            ], className='location_title_time')
        ], className='date_time twelve columns')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.P('Current', style={'fontWeight': 'bold'}),
                html.Div([
                    html.Div(id='temp'),
                    html.Div(id='humi')
                ], className='temp_humidity_row')
            ], className='temp_humidity_column')
        ], className='temp_humidity twelve columns')
    ], className='row'),

    html.Div([
        html.Div([
            html.Div([
                html.P('Current', style={'fontWeight': 'bold'}),
                html.Div([
                    html.Div(id='light_intensity'),
                    html.Div(id='co2')
                ], className='temp_humidity_row')
            ], className='temp_humidity_column')
        ], className='temp_humidity twelve columns')
    ], className='row'),

    html.Div([
        html.Div([
            dcc.Tabs(id='tabs', value='content_tab_one', children=[
                dcc.Tab(label='Real Time',
                        value='content_tab_one',
                        style=tab_style,
                        selected_style=selected_tab_style),
                dcc.Tab(label='Temperature',
                        value='content_tab_two',
                        style=tab_style,
                        selected_style=selected_tab_style),
                dcc.Tab(label='Humidity',
                        value='content_tab_three',
                        style=tab_style,
                        selected_style=selected_tab_style)
            ], style={'display': 'flex', 'flex-direction': 'row'})
        ], className='tabs_container twelve columns')
    ], className='row'),

    html.Div(id='return_tab_content', children=[])

])


@app.callback(Output('return_tab_content', 'children'),
              [Input('tabs', 'value')])
def render_content(value):
    if value == 'content_tab_one':
        return page_one_layout
    elif value == 'content_tab_two':
        return page_two_layout
    elif value == 'content_tab_three':
        return page_three_layout


@app.callback(Output('data_update_time', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/1/last.csv'
    df = pd.read_csv(url)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')
    dt_string = df['created_at'].iloc[0]

    return [
        html.Div(dt_string)
    ]


@app.callback(Output('temp', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/2/last.csv'
    df = pd.read_csv(url)
    temp = df['field2'].iloc[0]

    return [
        html.Div([
            html.Img(src=app.get_asset_url('hot.png'),
                     style={'height': '50px'}),
            html.Div([
                html.Div('°C', className='symbol'),
                html.Div('{0:.1f}'.format(temp),
                         className='numeric_value')
            ], className='temp_symbol')
        ], className='image_temp_row'),

        html.P('Temperature', style={'color': '#666666',
                                     'margin-top': '-10px'})
    ]


@app.callback(Output('humi', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/1/last.csv'
    df = pd.read_csv(url)
    hum = df['field1'].iloc[0]

    return [
        html.Div([
            html.Img(src=app.get_asset_url('humidity.png'),
                     style={'height': '50px'}),
            html.Div([
                html.Div('%', className='symbol'),
                html.Div('{0:.1f}'.format(hum),
                         className='numeric_value')
            ], className='temp_symbol')
        ], className='image_temp_row'),

        html.P('Humidity', style={'color': '#666666',
                                  'margin-top': '-10px'})
    ]


@app.callback(Output('light_intensity', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/3/last.csv'
    df = pd.read_csv(url)
    light_intens = df['field3'].iloc[0]

    return [
        html.Div([
            html.Img(src=app.get_asset_url('sunny.png'),
                     style={'height': '50px'}),
            html.Div([
                html.Div('lux', className='symbol'),
                html.Div('{0:.0f}'.format(light_intens),
                         className='numeric_value')
            ], className='temp_symbol')
        ], className='image_temp_row'),

        html.P('Light Intensity', style={'color': '#666666',
                                         'margin-top': '-10px'})
    ]


@app.callback(Output('co2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/4/last.csv'
    df = pd.read_csv(url)
    co2 = df['field4'].iloc[0]

    return [
        html.Div([
            html.Img(src=app.get_asset_url('co2.png'),
                     style={'height': '50px'}),
            html.Div([
                html.Div('ppm', className='symbol'),
                html.Div('{0:.0f}'.format(co2),
                         className='numeric_value')
            ], className='temp_symbol')
        ], className='image_temp_row'),

        html.P('CO2 Level in Air', style={'color': '#666666',
                                          'margin-top': '-10px'})
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
