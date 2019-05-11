import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output


app = dash.Dash(__name__)
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


df = pd.DataFrame({"time": [1, 2, 4], "values": [10, 20, 15]})

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dash_table.DataTable(
                            id="table-editing-simple",
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df.to_dict("records"),
                            editable=True,
                        )
                    ],
                    style={"width": "150px"},
                    className="six columns",
                ),
                html.Div(
                    [dcc.Graph(id="table-editing-simple-output")],
                    className="six columns",
                    style={"width": "800px"},
                ),
            ],
            className="row",
        )
    ],
    style={"width": "800px"},
)


@app.callback(
    Output("table-editing-simple-output", "figure"),
    [Input("table-editing-simple", "data"), Input("table-editing-simple", "columns")],
)
def display_output(rows, columns):
    df = pd.DataFrame(rows, columns=[c["name"] for c in columns])
    return {"data": [{"x": df[df.columns[0]], "y": df[df.columns[1]], "type": "line"}]}


if __name__ == "__main__":
    app.run_server(debug=True)
