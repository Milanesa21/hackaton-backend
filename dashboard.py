import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = px.data.gapminder()

# Inicializa la aplicación Dash
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Gapminder"),
    
    # Dropdown para seleccionar el país
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='Canada'  # Valor por defecto
    ),
    
    # Gráfico de dispersión
    dcc.Graph(id='life-exp-vs-gdp'),
    
    # Gráfico de líneas
    dcc.Graph(id='life-exp-over-time')
])

# Callback para actualizar el gráfico de dispersión
@app.callback(
    Output('life-exp-vs-gdp', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_scatter(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop', color='continent',
                     hover_name='country', log_x=True, size_max=55)
    fig.update_layout(title=f'Esperanza de vida vs. PIB per cápita en {selected_country}')
    return fig

# Callback para actualizar el gráfico de líneas
@app.callback(
    Output('life-exp-over-time', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_line_chart(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='lifeExp', title=f'Esperanza de vida en {selected_country} a lo largo del tiempo')
    return fig

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
