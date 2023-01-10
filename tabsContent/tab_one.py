import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from datetime import datetime
import pandas as pd
from app import app

layout_tab_one = html.Div([
    dcc.Interval(id='update_value1',
                 interval=1 * 11000,
                 n_intervals=0),
    html.Div([
        html.Div([
            dcc.Graph(id='line_chart',
                      config={'displayModeBar': False},
                      className='six columns',
                      style={'height': '300px'})
        ], className='tab_page twelve columns')
    ], className='row')
])


@app.callback(Output('line_chart', 'figure'),
              [Input('update_value1', 'n_intervals')])
def update_value(n_intervals):
    x_axis = ['2023-01-10 14:53:18', '2023-01-10 14:53:28', '2023-01-10 14:53:38']
    y_axis = [2.3, 2.4, 2.5]

    return {
        'data': [go.Scatter(
            x=x_axis,
            y=y_axis,
            mode='markers+lines',
            line=dict(width=3, color='#1EEC11'),
            marker=dict(size=7, symbol='circle', color='#1EEC11',
                        line=dict(color='#1EEC11', width=2)
                        ),
            # hoverinfo='text',
            # hovertext=
            # '<b>Date Time</b>: ' + x_axis + '<br>' +
            # '<b>Temperature (°C)</b>: ' + [f'{x:,.2f} °C' for x in y_axis] + '<br>'
        )],

        'layout': go.Layout(
            plot_bgcolor='rgba(255, 255, 255, 0)',
            paper_bgcolor='rgba(255, 255, 255, 0)',
            title={
                'text': '<b>Temperature (°C)</b>',
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': '#1EEC11',
                'size': 17},
            margin=dict(t=50, r=40, l=50),
            hovermode='closest',
            xaxis=dict(
                color='#666666',
                showline=True,
                showgrid=False,
                linecolor='#666666',
                linewidth=1,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='#666666')

            ),

            yaxis=dict(range=[min(y_axis) - 0.05, max(y_axis) + 0.05],
                       color='#666666',
                       zeroline=False,
                       showline=False,
                       showgrid=True,
                       gridcolor='#e6e6e6',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='#666666')
                       ),

        )

    }
