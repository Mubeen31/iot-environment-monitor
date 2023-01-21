import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
from app import app
from tabsContent.tab_one import layout_tab_one
from tabsContent.tab_two import layout_tab_two
from tabsContent.tab_three import layout_tab_three

tabs_styles = {'display': 'flex', 'flex-direction': 'row'}
tab_style = {
    'border-top': 'none',
    'border-left': 'none',
    'border-right': 'none',
    'border-bottom': 'none',
    'backgroundColor': 'rgba(255, 255, 255, 0)',
    'height': '35px',
    'width': 'auto',
    'padding': '7.5px'
}
selected_tab_style = {
    'border-top': 'none',
    'border-bottom': '2px solid blue',
    'border-right': 'none',
    'border-left': 'none',
    'backgroundColor': 'rgba(255, 255, 255, 0)',
    'fontWeight': 'bold',
    'height': '35px',
    'width': 'auto',
    'padding': '7.5px'

}
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
    ], className='row'),

    html.Div([
        html.Div([
            dcc.Tabs(id='tabs', value='content_tab_one', children=[
                dcc.Tab(label='Real Time',
                        value='content_tab_one',
                        style=tab_style,
                        selected_style=selected_tab_style,
                        className='font_family'),
                dcc.Tab(label='Temperature',
                        value='content_tab_two',
                        style=tab_style,
                        selected_style=selected_tab_style,
                        className='font_family'),
                dcc.Tab(label='Humidity',
                        value='content_tab_three',
                        style=tab_style,
                        selected_style=selected_tab_style,
                        className='font_family')
            ], style=tabs_styles)
        ], className='tabs_container twelve columns')
    ], className='row'),

    html.Div(id='return_tab_content', children=[])

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
                                     'margin-top': '0px'})
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

        html.P('Humidity', style={'color': '#666666'})
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

        html.P('Light Intensity', style={'color': '#666666'})
    ]


@app.callback(Output('co2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_value(n_intervals):
    co2 = 1120

    return [
        html.Div([
            html.Img(src=app.get_asset_url('co2.png'),
                     style={'height': '50px'}),

            html.Div([
                html.Div('{0:,.0f}'.format(co2),
                         className='numeric_value'),
                html.Div('ppm', className='symbol')
            ], className='temperature_row')
        ], className='image_temperature'),

        html.P('CO2 Level in Air', style={'color': '#666666'})
    ]


@app.callback(Output('return_tab_content', 'children'),
              Input('tabs', 'value'))
def render_content(value):
    if value == 'content_tab_one':
        return layout_tab_one
    elif value == 'content_tab_two':
        return layout_tab_two
    elif value == 'content_tab_three':
        return layout_tab_three


if __name__ == '__main__':
    app.run_server(debug=True)
