import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from urllib.parse import unquote_plus, quote_plus

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Kanit:wght@300&family=Oswald&display=swap',
    'https://fonts.gstatic.com',
    'https://fonts.googleapis.com'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div(id='container',
                      children=[
                          dcc.Location(id='url', refresh=False),
                          html.Div(id='page-content'),
                      ]
                      )


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        layout = html.Div([
            html.Div(id="Header", children=[
                html.Img(),
                html.H1("Pocker App")
            ]),
            html.Div(id='leftcontainer', children=[
                html.H1("Scrum Pocker for agile teams"),
                html.H2("Simple and fun story point estimations."),
                dcc.Link(id="start", children="Start new game", href="/Start"),

            ]),
            html.Div(id="rightcontainer", children=[
                html.Img()
            ])
        ])
        return layout
    elif pathname == '/Start':
        layout = html.Div([
            html.Div(id="Header", children=[
                html.Img(),
                html.H1("Start a game")
            ]),
            html.Div(id="gamesettings", children=[
                dcc.Input(id="gamename", placeholder="Game's name"),
                dcc.Dropdown(
                    id="Gamesmode",
                    options=[
                        {'label': 'Strict', 'value': 'Strict'},
                        {'label': 'Average', 'value': 'Average'},
                        {'label': 'Median', 'value': 'Median'},
                        {'label': 'Absolute Majority', 'value': 'Absolute Majority'},
                        {'label': 'Relative majority', 'value': 'Relative majority'}
                    ],
                    placeholder="Entrez le type",
                ),
                dcc.Link(id="Create", children="Create game", href="#"),
            ])
        ])
        return layout
    elif "Game" in str(pathname):
        layout = html.Div([
            html.Div(id="shadow"),
            html.Div(id="Header", children=[
                html.Img(),
                html.H1(id="Gametitle", children="Start a game")
            ]),
            html.Div(id="playernames",children=[
    
    # Player Inputs
    html.Div(id='player-container', children=[
        dcc.Input(id='player-1', type='text', value='Player 1'),
    ]),
    
    # Add and Delete Buttons
    html.Button('Add Player', id='add-button', n_clicks=0),
    html.Button('Delete Player', id='delete-button', n_clicks=0),
    html.Button(id='gotoGame', children="Go to the game", n_clicks=0,style={'margin-inline-end': '56px'})
]),
                
           """ html.Div(id='playernames', children=[
                html.H1("Add player's names"),
                html.H4(id="notice", children="You can add Maximum 5 players !"),
                dcc.Input(id="Player1", placeholder="Player 1"),
                dcc.Input(id="Player2", placeholder="Player 2"),
                html.Img(id='delete2', src='/assets/delete.png', n_clicks=0),
                dcc.Input(id="Player3", placeholder="Player 3"),
                html.Img(id='delete3', src='/assets/delete.png', n_clicks=0),
                dcc.Input(id="Player4", placeholder="Player 4"),
                html.Img(id='delete4', src='/assets/delete.png', n_clicks=0),
                dcc.Input(id="Player5", placeholder="Player 5"),
                html.Img(id='delete5', src='/assets/delete.png', n_clicks=0),
                html.Div([
                    html.Button(id="AddPlayer", children="+", n_clicks=0),
                    html.Button(id='gotoGame', children="Go to the game", n_clicks=0)
                ], style={'display': 'flex', 'justify-content': 'space-between'})

            ])"""
        ])
        return layout


@app.callback(Output('Create', 'href'),
              [Input('gamename', 'value'), Input('Gamesmode', 'value')])
def checkGamename(gamename, Gamesmode):
    if gamename and Gamesmode:
        urlstring = f'/Game/{gamename}+{Gamesmode}'
        return urlstring
    else:
        return "#"
# Callback to update player inputs
@app.callback(
    Output('player-container', 'children'),
    [Input('add-button', 'n_clicks'),
     Input('delete-button', 'n_clicks')],
    [State('player-container', 'children')]
)
def update_players(add_clicks, delete_clicks, player_container):
    # Determine which button was clicked
    ctx = dash.callback_context
    clicked_button_id = ctx.triggered_id if ctx.triggered_id else 'add-button'
    
    if 'add-button' in clicked_button_id:
        # Add a new player input
        player_container.append(dcc.Input(id=f'player-{len(player_container)+2}', type='text', value=f'Player {len(player_container)+1}'))
    elif 'delete-button' in clicked_button_id and len(player_container) > 1:
        # Delete the last added player (excluding the first one)
        player_container.pop()

    return player_container
    

@app.callback(
    [Output('gotoGame', 'style'), Output('gotoGame', 'disabled')],
    [Input('Player1', 'value'), Input('Player2', 'value'), Input('Player3', 'value'),
     Input('Player4', 'value'), Input('Player5', 'value')]
)
def go_to_game(player1, player2, player3, player4, player5):
    if player1 or player2 or player3 or player4 or player5:
        return [{}, True]
    else:
        return [{'background-color': '#e7eaf6'}, False]


if __name__ == "__main__":
    app.run_server(debug=True)
