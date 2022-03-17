from pydoc import classname
import dash
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash

app = DjangoDash("OncoPedAdminDash")

app.layout = html.Div(
    [
        html.Div([
            html.Div([
                html.H5("graphs here", className="text-center")
            ], className="col", style={'height': 250}),
            html.Div([
                html.H5("and here", className="text-center")
            ], className="col", style={'height': 250}),
        ], className="row"),
        html.Div([
            html.Div([
                html.H5("also here", className="text-center")
            ], className="col", style={'height': 250}),
            html.Div([
                html.H5("and all over the place", className="text-center")
            ], className="col", style={'height': 250}),
        ], className="row")
    ],
    className="container-fluid"
)

