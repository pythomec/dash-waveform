import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("Waveform editor"))),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dash_table.DataTable(
                                id="table-editing-simple",
                                columns=[
                                    {"name": i, "id": i} for i in ["time", "values"]
                                ],
                                data=[
                                    {"time": 1, "values": 10},
                                    {"time": 2, "values": 20},
                                    {"time": 4, "values": 15},
                                ],
                                editable=True,
                            )
                        ]
                    ),
                    style={"width": "150px"},
                ),
                dbc.Col(html.Div([dcc.Graph(id="table-editing-simple-output")])),
            ]
        ),
    ]
)


app.layout = dbc.Container([row])


@app.callback(
    Output("table-editing-simple-output", "figure"),
    [Input("table-editing-simple", "data"), Input("table-editing-simple", "columns")],
)
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c["name"] for c in columns])
    return {"data": [{"x": df[df.columns[0]], "y": df[df.columns[1]], "type": "line"}]}


if __name__ == "__main__":
    app.run_server(debug=True)
