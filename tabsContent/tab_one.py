import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
from app import app

layout_tab_one = html.Div([
   html.Div('tabs', style={'height': '100px', 'backgroundColor': 'white'})
])
