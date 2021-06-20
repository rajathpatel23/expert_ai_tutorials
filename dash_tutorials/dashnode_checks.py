import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import sqlite3 as sql

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1(children='SpotDot'),

    html.Div(["Keyword Input: ",
              dcc.Input(id='user_input', value='#tesla', type='text')]),



    cyto.Cytoscape(
        id = 'cytoscape-two-nodes',
        layout = {'name':'preset'},
        style = {'width' : '100%', 'height': '400px'},
        elements = [
            {'data': {'id': 'one', 'label': 'Apple Inc'}, 'position': {'x': 75, 'y':75}},
            {'data': {'id': 'two', 'label': 'Microsoft'}, 'position': {'x': 200, 'y': 200}},
            {'data': {'id': 'three', 'label': 'Tim Cook'}, 'position': {'x': 125, 'y': 125}},
            {'data': {'id': 'four', 'label': 'Steve Jobs'}, 'position': {'x': 450, 'y': 125}},
             {'data': {'source': 'one', 'target': 'two'}}, 
             {'data': {"source": 'one', 'target': 'three'}},
             {'data': {"source": 'one', 'target': 'four'}}
        ]
    )])

@app.callback(
    Input(component_id='user_input', component_property='value')
)
def update_search_keyword(search_keyword):
    """ Get keywords or hashtags to search twitter. """
    db_connect = sql.connect('tweets.db')
    db_cursor = db_connect.cursor()

    # Insert a row of data
    db_cursor.execute("""INSERT INTO tweets (search_keywords) VALUES (?)""", (search_keyword,))
    db_connect.commit()

if __name__ == '__main__':
    app.run_server(debug=True)