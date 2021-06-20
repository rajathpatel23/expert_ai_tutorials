import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)
app.layout = html.Div(
    [cyto.Cytoscape(
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

if __name__ == '__main__':
    app.run_server(debug=True)