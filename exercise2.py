# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# static data
years = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
Employers_total = [3.684999943, 3.657999992, 3.71600008, 3.832999945, 3.767999887, 3.767999887, 3.70600009, 3.697999954, 3.703000069, 3.673000097, 3.724999905]
Employment = [49.83800125, 47.95800018, 43.65800095, 41.62200165, 41.91199875, 42.61399841, 43.18999863, 44.31999969, 45.38499832, 46.36299896, 46.59500122]

# TODO: working on this file to add more codes...

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a simple Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': years, 'y': Employers_total, 'type': 'line', 'name': 'Years'},
                {'x': years, 'y': Employment, 'type': 'line', 'name': 'Ped S'}

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Employers Total (Percentage of Population vs. Employment to Population Ratio'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



