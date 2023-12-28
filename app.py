import random
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from urllib.parse import unquote_plus, quote_plus
from Game import Game
import firebase_admin
from firebase_admin import credentials, db

# Replace 'path/to/your/credentials.json' with the path to your Firebase service account key JSON file
cred = credentials.Certificate('planningpocker-f092a-firebase-adminsdk-9rql6-1a6e5c9448.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://planningpocker-f092a-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Reference to your Firebase Realtime Database
ref = db.reference('/')

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Kanit:wght@300&family=Oswald&display=swap',
    'https://fonts.gstatic.com',
    'https://fonts.googleapis.com'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div(id='container',
                      children=[
                          dcc.Location(id='url'),
                          html.Div(id='page-content'),
                      ]
                      )


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname=='/':
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
        dcc.Input(id='player-1', type='text', placeholder='Player 1'),
    ]),
    
    # Add and Delete Buttons
    html.Button('+ Add Player', id='add-button', n_clicks=0),
    html.Button('- Delete Player', id='delete-button', n_clicks=0),
    html.A(id='gotoGame', children="Go to the game",href='#',n_clicks=0)
]),
        
        ])
        return layout
    elif str(pathname).split('/')!='':
        layout = html.Div([
            html.Div(id="Header", children=[
                html.Img(),
                html.H1(id="Titleeofgame",children="Pocker App"),
                html.Div(id="Players",children=[
                html.H1(id="p1",children="player1",n_clicks=0),
                html.H1(id="p2",children="player1",n_clicks=0),
                html.H1(id="p3",children="player1",n_clicks=0),
                html.H1(id="p4",children="player1",n_clicks=0),
                html.H1(id="p5",children="player1",n_clicks=0),
            ])
            ]),
            
            html.Div(id="Taches",children=[
                dcc.Input(id="tache",placeholder="Ajouter une tâche"),
                html.Button(id="add-tache",children="Ajouter tache +",n_clicks=0),
                html.Ul(id='task-list')
            ]),
            html.H1("choisir votre carte 👇",style={'font-size':'20px','position':'relative','width':'fit-content',
                                                    'left':'35%','top':'340px'}),
            html.Div(id="cartes",children=[
               html.Img(id="0",src="/assets/0.png"),
               html.Img(id="1",src="/assets/1.png"),
               html.Img(id="2",src="/assets/2.png"),
               html.Img(id="3",src="/assets/3.png"),
               html.Img(id="5",src="/assets/5.png"),
               html.Img(id="8",src="/assets/8.png"),
               html.Img(id="13",src="/assets/13.png"),
               html.Img(id="20",src="/assets/20.png"),
               html.Img(id="40",src="/assets/40.png"),
               html.Img(id="100",src="/assets/100.png"),
               html.Img(id="coffee",src="/assets/coffee.png"),
               html.Img(id="INTERO",src="/assets/INTERO.png"),
            ]),
            html.H1(id="whichplayerisvoting",children="Player i c'est à votre tour !"),
            html.Button(id="Voter",children="Voter et voir les cartes"),
            html.Div(id="votecards", children=[
    html.Div([
        html.Img(id="c1",src="/assets/cardback.png"),
        html.H1(id="v1",children="player1"),
    ], className='votecard-container'),
    html.Div([
        html.Img(id="c2",src="/assets/cardback.png"),
        html.H1(id="v2",children="player1"),
    ], className='votecard-container'),
    html.Div([
        html.Img(id="c3",src="/assets/cardback.png"),
        html.H1(id="v3",children="player1"),
    ], className='votecard-container'),
    html.Div([
        html.Img(id="c4",src="/assets/cardback.png"),
        html.H1(id="v4",children="player1"),
    ], className='votecard-container'),
    html.Div([
        html.Img(id="c5",src="/assets/cardback.png"),
        html.H1(id="v5",children="player1"),
    ], className='votecard-container'),
])

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
    

# Callback to update player inputs and save to Firebase
@app.callback(
    [Output('player-container', 'children'),Output('gotoGame','href')],
    [Input('add-button', 'n_clicks'),
     Input('delete-button', 'n_clicks'),
     Input('gotoGame', 'n_clicks')],
    [State('player-container', 'children'),State('url','pathname')]
)
def update_and_save_players(add_clicks, delete_clicks, save_clicks, player_container,pathname):
    # Determine which button was clicked
    global mygame
    ctx = dash.callback_context
    clicked_button_id = ctx.triggered_id if ctx.triggered_id else 'add-button'
    
    if 'add-button' in clicked_button_id:
        # Add a new player input
        player_container.append(dcc.Input(id=f'player-{len(player_container)+1}', type='text', placeholder=f'Player {len(player_container)+1}'))
        
    elif 'delete-button' in clicked_button_id and len(player_container) > 1:
        # Delete the last added player (excluding the first one)
        player_container.pop()
        
    elif 'gotoGame' in clicked_button_id:
        
        # Split the input string by '/' and '+'
        split_parts = str(pathname).split('/')

        # Extract game name and mode game
        gamename = split_parts[-1].split('+')[0]
        modegame = split_parts[-1].split('+')[1] if len(split_parts[-1].split('+')) > 1 else None
        
        # Convert player_container data to a list of player names
        player_names = [player['props']['value'] for player in player_container]
        id = random.randint(0, 99999)
        
        mygame=Game(gamename,modegame,id)
        
           # Reference to your Firebase Realtime Database
        ref = db.reference('/game')
                         
           # Example: Set data with a custom key
        ref.child(str(mygame.id)).set({
                'id':mygame.id,
            'name':mygame.name,
            'mode':mygame.mode,
             'players':player_names
                        })
        myid=mygame.id
        
        return [player_container,f'/{myid}']
    
    return [player_container,'#']

@app.callback(
    [Output('gotoGame', 'style'), Output('gotoGame', 'disabled')],
    [Input('player-1', 'value')]
)
def go_to_game(player1):
    if player1 :
        return [{}, True]
    else:
        return [{'background-color': '#e7eaf6'}, False]


@app.callback(Output('Titleeofgame','children'),Input('url','pathname'))
def Game_layout(pathname):
    if str(pathname).split('/')!='' and str(pathname).split('/')!='/Start' and str(pathname).split('/')!='/Game':
        ref = db.reference('/game')
        key=str(pathname).split('/')[1]
        data = ref.child(key).get()
        user_name = data.get('name', 'Name not found')

        return user_name
        
@app.callback([Output('p1','children'),Output('p2','children'),Output('p3','children'),Output('p4','children'),Output('p5','children')],Input('url','pathname'))
def get_Players_Names(pathname):
    ref = db.reference('/game')
    key=str(pathname).split('/')[1]
    data = ref.child(key).get()
    players = data.get('players', 'Name not found')
    if len(players)==2:
       return[players[0],players[1],"","",""]
    elif len(players)==3:
        return[players[0],players[1],players[2],"",""]
    elif len(players)==4:
        return[players[0],players[1],players[2],players[3],""]
    elif len(players)==5:
        return[players[0],players[1],players[2],players[3],players[4]]
    else: return ["","","","",""]
    

@app.callback([Output('v1','children'),Output('v2','children'),Output('v3','children'),Output('v4','children'),Output('v5','children')],Input('url','pathname'))
def get_Players_Names(pathname):
    ref = db.reference('/game')
    key=str(pathname).split('/')[1]
    data = ref.child(key).get()
    players = data.get('players', 'Name not found')
    if len(players)==2:
       return[players[0],players[1],"","",""]
    elif len(players)==3:
        return[players[0],players[1],players[2],"",""]
    elif len(players)==4:
        return[players[0],players[1],players[2],players[3],""]
    elif len(players)==5:
        return[players[0],players[1],players[2],players[3],players[4]]
    else: return ["","","","",""]
    
@app.callback([Output('c1','style'),Output('c2','style'),Output('c3','style'),Output('c4','style'),Output('c5','style')],Input('url','pathname'))
def get_Players_Names(pathname):
    ref = db.reference('/game')
    key=str(pathname).split('/')[1]
    data = ref.child(key).get()
    players = data.get('players', 'Name not found')
    if len(players)==2:
       return[{'display':'100%'},{'display':'100%'},{'opacity':'50%'},{'opacity':'50%'},{'opacity':'50%'}]
    elif len(players)==3:
        return[{'display':'100%'},{'display':'100%'},{'display':'100%'},{'opacity':'50%'},{'opacity':'50%'}]
    elif len(players)==4:
        return[{'display':'100%'},{'display':'100%'},{'display':'100%'},{'display':'100%'},{'opacity':'50%'}]
    elif len(players)==5:
        return[{'display':'100%'},{'display':'100%'},{'display':'100%'},{'display':'100%'},{'display':'100%'}]
    else: return ["","","","",""]

@app.callback([Output('p1','style'),Output('whichplayerisvoting','children'),Output('p2','style')],[Input('p1','n_clicks'),Input('p1','children'),Input('p2','n_clicks'),Input('p2','children')])
def Chose_Player_To_Vote(button1_clicks,value1,button2_clicks,value2):
    button_styles = [{'border-bottom': '#3993FF'}, {'border-bottom': '#3993FF'}]
    print('kawther is clicked',button1_clicks)
    print('manar is clicked',button2_clicks)
    ctx = dash.callback_context
    if not ctx.triggered_id:
        # None of the buttons were clicked, return default styles
        return [{}, "",{}]

    clicked_button_id = ctx.triggered_id.split('.')[0]

    if clicked_button_id == 'p1':
        return [button_styles[0], f"{value1} c'est à votre tour !",{}]
    elif clicked_button_id == 'p2':
        return [{}, f"{value2} c'est à votre tour !",button_styles[1]]


@app.callback(
    [dash.dependencies.Output('task-list', 'children'),dash.dependencies.Output('task-list', 'style'),
     dash.dependencies.Output('add-tache', 'disabled'),dash.dependencies.Output('add-tache', 'style')],
    [dash.dependencies.Input('add-tache', 'n_clicks')],
    [dash.dependencies.State('tache', 'value')]
)
def update_task_list(n_clicks, new_task):
    if n_clicks > 0 and new_task:
        task_list = [html.Li('Votez sur la tache : '+new_task)]
        return task_list,{'display':'block'}, True,{'background-color':'#e7eaf6'}  # Désactiver le bouton après l'ajout
    else:
        return dash.no_update, {'display':'none'},False ,{}
    
@app.callback(Output('c1','src'),[Input('0','n_clicks'),Input('1','n_clicks'),Input('13','n_clicks'),Input('20','n_clicks'),Input('coffee','n_clicks'),Input('p1','n_clicks')])
def show_vote(button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks,p1):
    button1_clicks = button1_clicks or 0
    button2_clicks = button2_clicks or 0
    button3_clicks = button3_clicks or 0
    button4_clicks = button4_clicks or 0
    button5_clicks = button5_clicks or 0
    if p1!=0:
     if any([button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks]):
        max_clicks = max(button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks)
        if max_clicks == button1_clicks:
            return "/assets/0.png"
        elif max_clicks == button2_clicks:
            return "/assets/1.png"
        elif max_clicks == button3_clicks:
            return "/assets/13.png"
        elif max_clicks == button4_clicks:
            return "/assets/20.png"
        elif max_clicks == button5_clicks:
            return "/assets/coffee.png"
    return "/assets/cardback.png"

@app.callback(Output('c2','src'),[Input('0','n_clicks'),Input('1','n_clicks'),Input('13','n_clicks'),Input('20','n_clicks'),Input('coffee','n_clicks'),Input('p2','n_clicks')])
def show_vote(button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks,p2):
    button1_clicks = button1_clicks or 0
    button2_clicks = button2_clicks or 0
    button3_clicks = button3_clicks or 0
    button4_clicks = button4_clicks or 0
    button5_clicks = button5_clicks or 0
    if p2!=0:
     if any([button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks]):
        max_clicks = max(button1_clicks, button2_clicks, button3_clicks, button4_clicks, button5_clicks)
        if max_clicks == button1_clicks:
            return "/assets/0.png"
        elif max_clicks == button2_clicks:
            return "/assets/1.png"
        elif max_clicks == button3_clicks:
            return "/assets/13.png"
        elif max_clicks == button4_clicks:
            return "/assets/20.png"
        elif max_clicks == button5_clicks:
            return "/assets/coffee.png"
    return "/assets/cardback.png"

if __name__ == "__main__":
    app.run_server(debug=True)
