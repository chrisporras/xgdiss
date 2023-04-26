#!/usr/bin/env python
# coding: utf-8
from dash import Dash, dcc, html, Input, Output
# import omnixai
#### load data ###############################################################
keys = ['predict', 'lime', 'ig', 'gradcam#0', 'gradcam#1', 'gradcam#2', 'gradcam#3']
idx_list = [0,7]
data_path = '/home/porrac01/mysite/'
# load explanations
def unpickle(file_name):
  import pickle
  # open a file, where you stored the pickled data
  file = open(file_name, 'rb')
  # dump information to that file
  exp = pickle.load(file)
  return exp
##############################################################################
app = Dash(__name__)

app.layout = html.Div([
    html.H1('XGDiss Xplainable AI'),
    dcc.Graph(id="plot"),
    html.H4("Image idx:"),
    html.Blockquote('Idx 0 is CE, Idx 7 is LAA'),
    dcc.Dropdown(idx_list, idx_list[0], id='idx_dropdown'),
    # html.P("Expression Z-score range:"),
    # dcc.RangeSlider(-1, 8, 1, count=1,
    #                 value=[-1, 8], id='range_slider'),
    html.H4("OmnixAI method:"),
    dcc.RadioItems(
        keys,
        'predict',
        id='label',
        inline=False
    ),
    dcc.Markdown(
    '''
    #### Methods include: `LIME`, `Integrated Gradients`, `GradCAM`
    **GradCAM is used 4 ways:** \n

    1. gradcam#0 = last conv of ResNet layer 4 \n

    2. gradcam#1 = first conv of ResNet layer 4 \n

    3. gradcam#2 = last conv of ResNet layer 4 & **OPPOSITE** class highlighted \n

    4. gradcam#3 = first conv of ResNet layer 4 & **OPPOSITE** class highlighted
    '''
    ),
])

@app.callback(
    Output("plot", "figure"),
    Input('idx_dropdown', 'value'),
    # Input('range_slider', 'value'),
    Input('label', 'value')
)
### update fig
def update_fig(idx_dropdown, label):
    filename = 'explanations-test-idx_'+str(idx_dropdown)+'-label.pkl'
    exp = unpickle(data_path + filename)
    fig = exp[label]._plotly_figure(index=0,class_names='CL')
    return fig
# app.run_server(debug=True, port=8049, use_reloader=False)
if __name__ == '__main__':
    app.run_server(debug=True)
