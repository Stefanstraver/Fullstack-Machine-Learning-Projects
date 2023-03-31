# importeren dependencies
from dash import Dash, html, dcc 
import plotly.express as px
import pandas as pd

# Creëer instance voor de app
app = Dash('Social Media Cluster Dashboard')

# Load data 
df = pd.read_csv('cluster_result.csv')

# Maak plots
fig1 = px.scatter(
    df,
    x='num_comments',
    y='num_reactions',
    color='cluster')

fig2 = px.scatter(
    df,
    x='num_shares',
    y='num_likes',
    color='cluster')

fig3 = px.scatter(
    df,
    x='num_angrys',
    y='num_sads',
    color='cluster')

fig4 = px.scatter(
    df,
    x='num_loves',
    y='num_wows',
    color='cluster')

# Layout
app.layout = html.Div(
    children=[
        html.H1(children='Social Media Cluster Dashboard'),
        html.Div(children='Clustergroepen in verschillende scatterplots'),
        html.Div(children=[
            html.Div(dcc.Graph(id='comments', figure=fig1), style={'display':'inline-block'}),
            html.Div(dcc.Graph(id='shares', figure=fig2), style={'display':'inline-block'})
        ]),
        html.Div(children=[
            html.Div(dcc.Graph(id='hahas', figure=fig3), style={'display':'inline-block'}),
            html.Div(dcc.Graph(id='loves', figure=fig4), style={'display':'inline-block'})
        ])
    ],
    style={'font-family':'Roboto', 'margin':'0 auto', 'width':'1400px'}
)

# Run de applicatie
if __name__ == '__main__':
    app.run_server(debug=True)

