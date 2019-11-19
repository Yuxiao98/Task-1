import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('try.csv')


app.layout = html.Div([
    dcc.Graph(
        id='_id',
        figure={
            'data': [
                go.Scatter(
                    x=df['btap_results.total_capital_cost'],
                    y=df['btap_results.total_end_uses_gj_per_m_sq'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Capital Cost'},
                yaxis={'title': 'End Uses'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
