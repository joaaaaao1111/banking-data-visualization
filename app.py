import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# load data
df = pd.read_csv(r'C:/DataVisualization/data/train.csv', delimiter=';')  

# Crie figuras interativas com Plotly
fig_age = px.box(df, y="age", title="Distribuição de Idade")
fig_job = px.histogram(df, x="job", title="Distribuição de Trabalho")
fig_marital = px.pie(df, names="marital", title="Distribuição de Estado Civil")
fig_education = px.pie(df, names="education", title="Distribuição de Educação")

# Calcule as porcentagens de crédito à habitação e crédito pessoal
housing_loan_pct = df['housing'].value_counts(normalize=True)['yes'] * 100
personal_loan_pct = df['loan'].value_counts(normalize=True)['yes'] * 100

# Inicialize o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Defina o layout do aplicativo
app.layout = dbc.Container([
    html.H1("Persona Dashboard for Banking", className="text-center my-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_age), md=6),
        dbc.Col(dcc.Graph(figure=fig_job), md=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_marital), md=6),
        dbc.Col(dcc.Graph(figure=fig_education), md=6),
    ]),
    dbc.Row([
        dbc.Col(html.H4(f"Porcentagem de clientes com crédito à habitação: {housing_loan_pct:.2f}%"), md=6),
        dbc.Col(html.H4(f"Porcentagem de clientes com crédito pessoal: {personal_loan_pct:.2f}%"), md=6),
    ]),
])

# Execute o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)