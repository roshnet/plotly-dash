import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()


df = pd.read_csv('datasets/gdp-life-exp-2007.csv')

app.layout = html.Div([
		dcc.Graph(
			id = 'life-exp-vs-gdp',
			figure = {
				'data': [
					go.Scatter(
						x = df[df['continent'] == i]['gdp per capita'],
						y = df[df['continent'] == i]['life expectancy'],
						text = df[df['continent'] == i]['country'],
						mode = 'markers',
						opacity = 0.8,
						marker = {
							'size': 15,
							'line': {
								'width': 0.5,
								'color': 'white'
							}
						},
						name = i
					) for i in df.continent.unique()
				],
				'layout': go.Layout(
					xaxis = {
						'type': 'log',
						'title': 'GDP per capita'
					},
					yaxis = {
						'title': 'Life Expectancy'
					},
					margin = {
						'l': 40,
						'b': 40,
						't': 10,
						'r': 10
					},
					legend = {
						'x': 0,
						'y': 1
					},
					hovermode = 'closest'
				)
			}
		),
		dcc.Dropdown(
			options = [
				{
					'label': 'New York City',
					'value': 'NYC'
				},
				{
					'label': 'Montreal',
					'value': 'MTL'
				},
				{
					'label': 'San Francisco',
					'value': 'SF'
				}
			],
			value = 'NYC'	# default value
		)
	]
)

if __name__ == '__main__':
	app.run_server(debug=True)
