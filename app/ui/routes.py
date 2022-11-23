from flask import Blueprint, render_template, request, redirect
from app.models import db, Player
import pandas as pd

ui_bp = Blueprint(
   'ui_bp', __name__,
   template_folder='templates',
   static_folder='static'
)


@ui_bp.route('/')
def home():
    return render_template("home.html")


@ui_bp.route('/players', methods=['GET', 'POST'])
def players_list():
    if request.method == 'POST':
        name = request.form.get('name')
        height = request.form.get('height')
        weight = request.form.get('weight')
        avgscore = request.form.get('avgscore')
        tsp = request.form.get('tsp')
        assists = request.form.get('assists')
        player1 = Player(
            name=name,
            height=height,
            weight=weight,
            avgscore=avgscore,
            tsp=tsp,
            assists=assists
        )
        db.session.add(player1)
        db.session.commit()
    return render_template('players.html', players=players)


@ui_bp.route('/players/add_player')
def add_player():
    title = 'Create New Player'
    return render_template('add_player.html', title=title)


@ui_bp.route('/players/import/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv_players(uploaded_file.filename)
    return redirect('/players/import')


@ui_bp.route('/players/import', methods=['GET', 'POST'])
def import_players():
    return render_template('upload_players.html')


def parse_csv_players(file_path):
    # Use Pandas to parse the CSV file
    csv_data = pd.read_csv(file_path)
    # Loop through the rows and create a Student object for each row
    for i, row in csv_data.iterrows():
        player = Player(
            name=row['Name'],
            height=row['Height'],
            weight=row['Weight'],
            avgscore=row['AvgScore'],
            tsp=row['TSP'],
            assists=row['Assists'],
        )
        db.session.add(player)
    db.session.commit()


@ui_bp.route('/api/players')
def players():
    return {'data': [player.to_dict() for player in Player.query]}


@ui_bp.route("/select_player", methods=['GET', 'POST'])
def select_player():
    player_list = [r.name for r in db.session.query(Player.name)]
    return render_template('select_player.html', dropdown_list=player_list,)


@ui_bp.route("/game", methods=['GET', 'POST'])
def game():
    p1_name = request.form["p1"]
    p2_name = request.form["p2"]
    print(p1_name)
    p1 = Player.query.filter_by(name=p1_name).first()
    p2 = Player.query.filter_by(name=p2_name).first()
    Player_1 = p1.name
    p1_height = float(p1.height)
    p1_weight = float(p1.weight)
    p1_avgscore = float(p1.avgscore)
    p1_tsp = float(p1.tsp)
    p1_assists = float(p1.assists)
    Player_2 = p2.name
    p2_height = float(p2.height)
    p2_weight = float(p2.weight)
    p2_avgscore = float(p2.avgscore)
    p2_tsp = float(p2.tsp)
    p2_assists = float(p2.assists)
    print(p2_assists)
    print(p2_weight)

    return render_template("game.html", p1=p1, p2=p2, Player_1=Player_1, p1_height=p1_height, p1_weight=p1_weight,
                           p1_avgscore=p1_avgscore, p1_tsp=p1_tsp, p1_assists=p1_assists,
                           Player_2=Player_2, p2_height=p2_height, p2_weight=p2_weight,
                           p2_avgscore=p2_avgscore, p2_tsp=p2_tsp, p2_assists=p2_assists)

