import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
es = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=es)
df=pd.read_parquet("eventpayload.parquet")
fig1 = px.histogram(df,'event')
fig2 = px.histogram(df,'manufacturer')
fig1.show()
fig1.update_layout(xaxis_title='Type Of Events', yaxis_title='Count')
app.layout = html.Div(children=[html.Div(children=[
    html.H1(children='Events Trend'),
    dcc.Graph(figure=fig1)]),
    html.Div(children=[
    html.H1(children='Manufacturing'),
    dcc.Graph(figure=fig2)])
])
if __name__ == '__main__':
    app.run_server(debug=True)