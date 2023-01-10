import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
from app import app

layout_tab_three = html.Div([
    dcc.Interval(id='update_value3',
                 interval=1 * 11000,
                 n_intervals=0),
    html.Div([
        html.Div([
            html.Div(id='hum1')
        ], className='tab_page twelve columns')
    ], className='row')
])


@app.callback(Output('hum1', 'children'),
              [Input('update_value3', 'n_intervals')])
def update_value(n_intervals):
    current_temp = float(90.0)
    return [
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Current', style={'line-height': '1'}),
                    html.Div('{0:.1f}%'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Today Max', style={'line-height': '1'}),
                    html.Div('{0:.1f}%'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Today Min', style={'line-height': '1'}),
                    html.Div('{0:.1f}%'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Yesterday Max', style={'line-height': '1'}),
                    html.Div('{0:.1f}%'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Yesterday Min', style={'line-height': '1'}),
                    html.Div('{0:.1f}%'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row')
    ]
