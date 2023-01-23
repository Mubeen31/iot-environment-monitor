from app import app
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd

page_two_layout = html.Div([

    dcc.Interval(id='update_value2',
                 interval=1 * 16000,
                 n_intervals=0),

    html.Div([
        html.Div([
            html.Div(id='temp2')
        ], className='tabs_page twelve columns')
    ], className='row')

])


@app.callback(Output('temp2', 'children'),
              [Input('update_value2', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/2/last.csv'
    df = pd.read_csv(url)
    current_temp = df['field2'].iloc[0]

    url = 'https://api.thingspeak.com/channels/2007583/fields/2.csv?days=1'
    df1 = pd.read_csv(url)
    df1['created_at'] = pd.to_datetime(df1['created_at'])
    df1['created_at'] = pd.to_datetime(df1['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df1['Date'] = pd.to_datetime(df1['created_at']).dt.date
    unique_date = df1['Date'].unique()
    today_max = df1[df1['Date'] == unique_date[-1]]['field2'].max()
    today_min = df1[df1['Date'] == unique_date[-1]]['field2'].min()

    url = 'https://api.thingspeak.com/channels/2007583/fields/2.csv?days=2'
    df2 = pd.read_csv(url)
    df2['created_at'] = pd.to_datetime(df2['created_at'])
    df2['created_at'] = pd.to_datetime(df2['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df2['Date'] = pd.to_datetime(df2['created_at']).dt.date
    yesterday_unique_date = df2['Date'].unique()
    yesterday_max = df2[df2['Date'] == yesterday_unique_date[-2]]['field2'].max()
    yesterday_min = df2[df2['Date'] == yesterday_unique_date[-2]]['field2'].min()

    return [
        html.Div([
            html.Div([
                html.Div([
                    html.Div('Current'),
                    html.Div('{0: .1f}°C'.format(current_temp))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),

        html.Div([
            html.Div([
                html.Div([
                    html.Div('Today Max'),
                    html.Div('{0: .1f}°C'.format(today_max))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),

        html.Div([
            html.Div([
                html.Div([
                    html.Div('Today Min'),
                    html.Div('{0: .1f}°C'.format(today_min))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),

        html.Div([
            html.Div([
                html.Div([
                    html.Div('Yesterday Max'),
                    html.Div('{0: .1f}°C'.format(yesterday_max))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row'),

        html.Div([
            html.Div([
                html.Div([
                    html.Div('Yesterday Min'),
                    html.Div('{0: .1f}°C'.format(yesterday_min))
                ], className='tab_temp_row')
            ], className='bg_container twelve columns')
        ], className='row')
    ]
