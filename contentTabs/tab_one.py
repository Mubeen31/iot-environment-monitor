from app import app
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
import plotly.graph_objs as go

page_one_layout = html.Div([

    dcc.Interval(id='update_value1',
                 interval=1 * 16000,
                 n_intervals=0),

    html.Div([
        html.Div([
            dcc.Graph(id='line_chart',
                      config={'displayModeBar': False},
                      className='six columns')
        ], className='tabs_page twelve columns')
    ], className='row')

])


@app.callback(Output('line_chart', 'figure'),
              [Input('update_value1', 'n_intervals')])
def update_value(n_intervals):
    url = 'https://api.thingspeak.com/channels/2007583/fields/2.csv?results=15'
    df = pd.read_csv(url)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')

    return {
        'data': [go.Scatter(
            x=df['created_at'],
            y=df['field2'],
            mode='markers+lines',
            line=dict(width=3, color='rgb(214, 32, 32)'),
            marker=dict(size=7, symbol='circle', color='rgb(214, 32, 32)',
                        line=dict(width=2, color='rgb(214, 32, 32)')),
            hoverinfo='text',
            hovertext=
            '<b>Date Time</b>: ' + df['created_at'].astype(str) + '<br>' +
            '<b>Temperature (°C)</b>: ' + [f'{x:.1f} °C' for x in df['field2']] + '<br>'
        )],
        'layout': go.Layout(
            title={'text': '<b>Temperature (°C)</b>',
                   'y': 0.95,
                   'x': 0.5,
                   'yanchor': 'top',
                   'xanchor': 'center'},
            titlefont={'color': 'rgb(214, 32, 32)',
                       'size': 17},
            plot_bgcolor='rgba(255, 255, 255, 0)',
            paper_bgcolor='rgba(255, 255, 255, 0)',
            hovermode='x',
            margin=dict(t=50, l=50, r=40),
            xaxis=dict(
                showline=True,
                showgrid=False,
                linecolor='#666666',
                linewidth=1,
                ticks='outside',
                color='#666666',
                tickfont=dict(family='Arial',
                              size=12,
                              color='#666666')
            ),
            yaxis=dict(
                showline=False,
                showgrid=True,
                gridcolor='#e6e6e6',
                color='#666666',
                tickfont=dict(family='Arial',
                              size=12,
                              color='#666666')
            )
        )
    }
