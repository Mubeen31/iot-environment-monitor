import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
from app import app

layout_tab_two = html.Div([
    dcc.Interval(id='update_value2',
                 interval=1 * 11000,
                 n_intervals=0),
    html.Div([
        html.Div([
            html.Div(id='temp1')
        ], className='tab_page twelve columns')
    ], className='row')
])


@app.callback(Output('temp1', 'children'),
              [Input('update_value2', 'n_intervals')])
def update_value(n_intervals):
    current_temp = float(2.3)
    return [
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Current', style={'line-height': '1'}),
                    html.Div('{0:.1f}°C'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Today Max', style={'line-height': '1'}),
                    html.Div('{0:.1f}°C'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Today Min', style={'line-height': '1'}),
                    html.Div('{0:.1f}°C'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Yesterday Max', style={'line-height': '1'}),
                    html.Div('{0:.1f}°C'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Yesterday Min', style={'line-height': '1'}),
                    html.Div('{0:.1f}°C'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row')
    ]
