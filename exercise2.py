# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# static data
years = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
total_employment = [61.98799896, 61.22700119, 58.37400055, 57.4620018, 57.37599945, 57.8219986, 57.90299988, 58.36999893, 58.74000168, 59.13299942, 59.19200134]
female_employment = [55.63999939, 55.29399872, 53.46099854, 52.54999924, 52.11299896, 52.22499847, 52.30799866, 52.70800018, 52.94100189, 53.30799866, 53.33200073]
male_employment = [68.62200165, 67.42299652, 63.50299835, 62.58499908, 62.85800171, 63.64599991, 63.72000122, 64.25099945, 64.75700378, 65.17199707, 65.26300049]
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
                {'x': years, 'y': total_employment, 'type': 'line', 'name': 'Total Employment'},
                {'x': years, 'y': female_employment, 'type': 'line', 'name': 'Female Employment'}
                {'x': years, 'y': male_employment, 'type': 'line', 'name': 'Male Employment'}

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Employment Rates in the US'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



