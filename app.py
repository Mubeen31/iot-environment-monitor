import dash

metaTags = [{'name': 'viewport',
             'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5'}]
externalStylesheet = [metaTags]

app = dash.Dash(__name__, external_stylesheets=externalStylesheet,
                suppress_callback_exceptions=True)
server = app.server
