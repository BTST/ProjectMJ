import os
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bootstrap import Bootstrap
import requests
import json
from datetime import datetime
from decimal import Decimal
from flask_socketio import SocketIO, emit

app = Flask(__name__)

URL = os.environ.get('DATABASE_URL2')
SECRETKEY = os.environ.get('SECRET_KEY')
GRRequestKey = os.environ.get('GRRequestKey')
NASAAPIKEY = os.environ.get('NASAAPIKEY')


engine = create_engine(URL)
db = scoped_session(sessionmaker(bind=engine))
bootstrap = Bootstrap(app)
socketio = SocketIO(app)

@socketio.on("submit message")
def message (data):
      selection = data["selection"]
      emit("announce message", {"selection": selection}, broadcast=True)

@app.route("/chat")
def chat():
    return render_template("chat.html")

class SessionRecord:
    def __init__(self, players,session):
        self.date = date
        self.players = players
        self.session = session

class Players:
    def __init__(self, numberOf, names):
        self.numberOf = numberOf
        self.names = names

@app.route("/drawrandommjtiles")
def drawrandommjtiles():
    # Suits 1 = Dragon (Wan), 2 = Bamboos (Su), 3 = Stones (tong),  4 = (Honours)
    # 5 =  flowers 6 = animals
    Suits = [1, 2, 3, 4, 5, 6]



@app.route("/deletesession", methods = ["GET", "POST"])
def deletesession():
    realSessions = db.execute("SELECT * FROM mjsessions")
    req = request.form
    sessionToDelete = req.get("sessiontodelete")
    if not sessionToDelete == None:
        deleteSessionCommand = "DELETE FROM mjsessions WHERE id = " + str(sessionToDelete)
        db.execute(deleteSessionCommand)
    db.commit()
    return render_template("deletesession.html", realsessions=realSessions)

@app.route("/")
def index():
    return redirect(url_for("allsessions"))

@app.route("/allsessions")
def allsessions():
    allsessions = []
    players = db.execute("SELECT * FROM mjplayer")
    sessions = db.execute("SELECT * FROM mjsessions")
    x = 1
    for session in sessions:
        playerlist = [1, 2, 3, 4, 5]
        playeroneid = session.playerone_id
        playerOneCommand = "SELECT * FROM mjplayer WHERE id = " + str(playeroneid)
        playerone = db.execute(playerOneCommand).fetchone()
        playeronename = playerone.name
        playeronescore = session.playerone_score

        if playerone.id == 1:
            playonename = playeronename
            playonescore = playeronescore
            playerlist.remove(1)

        if playerone.id == 2:
            playtwoname = playeronename
            playtwoscore = playeronescore
            playerlist.remove(2)

        if playerone.id == 3:
            playthreename = playeronename
            playthreescore = playeronescore
            playerlist.remove(3)

        if playerone.id == 4:
            playfourname = playeronename
            playfourscore = playeronescore
            playerlist.remove(4)

        if playerone.id == 5:
            playfivename = playeronename
            playfivescore = playeronescore
            playerlist.remove(5)

#Jerry[0], Meihui[1], Jason[2], Ben[3], Lingwei[4]

        playertwoid = session.playertwo_id
        playerTwoCommand = "SELECT * FROM mjplayer WHERE id = " + str(playertwoid)
        playertwo = db.execute(playerTwoCommand).fetchone()
        playertwoname = playertwo.name
        playertwoscore = session.playertwo_score
        if playertwo.id == 1:
            playeronename = playertwoname
            playeronescore = playertwoscore
            playerlist.remove(1)
        if playertwo.id == 2:
            playtwoname = playertwoname
            playtwoscore = playertwoscore
            playerlist.remove(2)
        if playertwo.id == 3:
            playthreename = playertwoname
            playthreescore = playertwoscore
            playerlist.remove(3)
        if playertwo.id == 4:
            playfourname = playertwoname
            playfourscore = playertwoscore
            playerlist.remove(4)
        if playertwo.id == 5:
            playfivename = playertwoname
            playfivescore = playertwoscore
            playerlist.remove(5)

        playerthreeid = session.playerthree_id
        playerThreeCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerthreeid)
        playerthree = db.execute(playerThreeCommand).fetchone()
        playerthreename = playerthree.name
        playerthreescore = session.playerthree_score
        if playerthree.id == 1:
            playonename = playerthreename
            playonescore = playerthreescore
            playerlist.remove(1)
        if playerthree.id == 2:
            playtwoname = playerthreename
            playtwoscore = playerthreescore
            playerlist.remove(2)
        if playerthree.id == 3:
            playthreename = playerthreename
            playthreescore = playerthreescore
            playerlist.remove(3)
        if playerthree.id == 4:
            playfourname = playerthreename
            playfourscore = playerthreescore
            playerlist.remove(4)
        if playerthree.id == 5:
            playfivename = playerthreename
            playfivescore = playerthreescore
            playerlist.remove(5)

        playerfourid = session.playerfour_id
        playerFourCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerfourid)
        playerfour = db.execute(playerFourCommand).fetchone()
        playerfourname = playerfour.name
        playerfourscore = session.playerfour_score
        if playerfour.id == 1:
            playonename = playerfourname
            playonescore = playerfourscore
            playerlist.remove(1)
        if playerfour.id == 2:
            playtwoname = playerfourname
            playtwoscore = playerfourscore
            playerlist.remove(2)
        if playerfour.id == 3:
            playthreename = playerfourname
            playthreescore = playerfourscore
            playerlist.remove(3)
        if playerfour.id == 4:
            playfourname = playerfourname
            playfourscore = playerfourscore
            playerlist.remove(4)
        if playerfour.id == 5:
            playfivename = playerfourname
            playfivescore = playerfourscore
            playerlist.remove(5)

        playerWhoDidNotPlay = playerlist[0]
        playerFiveCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerWhoDidNotPlay)
        playerfive = db.execute(playerFiveCommand).fetchone()

        playerfivename = playerfive.name
        playerfivescore = "Did Not Play"
        if playerfive.id == 1:
            playonename = playerfivename
            playonescore = playerfivescore
        if playerfive.id == 2:
            playtwoname = playerfivename
            playtwoscore = playerfivescore
        if playerfive.id == 3:
            playthreename = playerfivename
            playthreescore = playerfivescore
        if playerfive.id == 4:
            playfourname = playerfivename
            playfourscore = playerfivescore
        if playerfive.id == 5:
            playfivename = playerfivename
            playfivescore = playerfivescore

        dateString = str(session.gamedate)
        dateString = dateString[:10]

        scores = {
            x : dateString,
            playonename : playonescore,
            playtwoname : playtwoscore,
            playthreename : playthreescore,
            playfourname : playfourscore,
            playfivename : playfivescore
        }
        allsessions.append(scores)
        x = x + 1
    return render_template("allsessions.html", allsessions=allsessions, players=players)

class MahjongPlayer:
    def __init__(self, name, id, gamesplayed, averagescore, lifetime):
        self.name = name
        self.id = id
        self.gamesplayed = gamesplayed
        self.averagescore = averagescore
        self.lifetime = lifetime



@app.route("/players")
def players():
    players = db.execute("SELECT * FROM mjplayer")
    mjplayers = []
    for mjplayer in players:
        nameOfPlayer = mjplayer.name
        idOfPlayer = mjplayer.id
        lifetime = Decimal(00.00)
        firstCount = db.execute("SELECT COUNT(playerone_id) " + "FROM mjsessions WHERE playerone_id =" + str(idOfPlayer))
        secondCount = db.execute("SELECT COUNT(playertwo_id) " + "FROM mjsessions WHERE playertwo_id =" + str(idOfPlayer))
        thirdCount = db.execute("SELECT COUNT(playerthree_id) " + "FROM mjsessions WHERE playerthree_id =" + str(idOfPlayer))
        fourthCount = db.execute("SELECT COUNT(playerfour_id) " + "FROM mjsessions WHERE playerfour_id =" + str(idOfPlayer))

        #Learn this proxty result access
        gamesplayed = firstCount.fetchone()[0] + secondCount.fetchone()[0] + thirdCount.fetchone()[0] + fourthCount.fetchone()[0]

        firstpositiongames = db.execute("SELECT * " + "FROM mjsessions WHERE playerone_id =" + str(idOfPlayer)).fetchall()
        for game in firstpositiongames:
            lifetime = lifetime + game.playerone_score

        secondpositiongames = db.execute("SELECT * " + "FROM mjsessions WHERE playertwo_id =" + str(idOfPlayer)).fetchall()
        for game in secondpositiongames:
            lifetime = lifetime + game.playertwo_score

        thirdpostitiongames = db.execute("SELECT * " + "FROM mjsessions WHERE playerthree_id =" + str(idOfPlayer)).fetchall()
        for game in thirdpostitiongames:
            lifetime = lifetime + game.playerthree_score

        fourthpositiongames = db.execute("SELECT * " + "FROM mjsessions WHERE playerfour_id =" + str(idOfPlayer)).fetchall()
        for game in fourthpositiongames:
            lifetime = lifetime + game.playerfour_score
        if gamesplayed > 0:
            averagescore = lifetime / gamesplayed
        else:
            averagescore = 0
        mjplayers.append(MahjongPlayer (nameOfPlayer, mjplayer.id, gamesplayed,averagescore,lifetime))
    sorted_mjplayers = sorted(mjplayers, key=lambda x: x.lifetime)
    winner = sorted_mjplayers[-1].name
    sorted_mjplayers2 = sorted(mjplayers, key=lambda x: x.averagescore)
    winner2 = sorted_mjplayers2[-1].name

    winner3 = sorted_mjplayers[-2].name
    return render_template("players.html", players=mjplayers, winner=winner, winner2=winner2, winner3=winner3)


@app.route("/sessions", methods = ["GET", "POST"])
def sessions():
    players = db.execute("SELECT * FROM mjplayer")
    return render_template("sessions.html", players=players)


@app.route("/createsession", methods = ["GET", "POST"])
def createsessions():
    req = request.form
    dateOfSession = req.get("sessiondate")
    format = '%Y-%m-%d'
    date = datetime.strptime(dateOfSession, format)
    playeronename = req.get("firstplayername")
    playertwoname = req.get("secondplayername")
    playerthreename = req.get("thirdplayername")
    playerfourname = req.get("fourthplayername")
    playerOneCommand = "SELECT * FROM mjplayer WHERE name LIKE" + " '%" + playeronename + "%'"
    playerTwoCommand = "SELECT * FROM mjplayer WHERE name LIKE" + " '%" + playertwoname + "%'"
    playerThreeCommand = "SELECT * FROM mjplayer WHERE name LIKE" + " '%" + playerthreename + "%'"
    playerFourCommand = "SELECT * FROM mjplayer WHERE name LIKE" + " '%" + playerfourname + "%'"

    playerone = db.execute(playerOneCommand).fetchone()
    playertwo = db.execute(playerTwoCommand).fetchone()
    playerthree = db.execute(playerThreeCommand).fetchone()
    playerfour = db.execute(playerFourCommand).fetchone()

    playerone_id = int(playerone.id)
    playertwo_id = int(playertwo.id)
    playerthree_id = int(playerthree.id)
    playerfour_id = int(playerfour.id)

    playerone_score = Decimal(req.get("firstplayerscore"))
    playertwo_score = Decimal(req.get("secondplayerscore"))
    playerthree_score = Decimal(req.get("thirdplayerscore"))
    playerfour_score = Decimal(req.get("fourthplayerscore"))

    sessionInsertCommand = "INSERT INTO mjsessions (gamedate, playerone_id, playertwo_id, playerthree_id, playerfour_id, playerone_score, playertwo_score, playerthree_score, playerfour_score) VALUES ('%s', '%d', '%d', '%d', '%d','%d', '%d', '%d', '%d')" % (date, playerone_id, playertwo_id, playerthree_id, playerfour_id, playerone_score, playertwo_score, playerthree_score, playerfour_score)
    db.execute(sessionInsertCommand)
    db.commit()

    return redirect(url_for("allsessions"))
#@app.route("/createnewplayer", methods=["GET", "POST"])
#def createnewplayer()

@app.route('/allsessions/<gamedate>')
def session(gamedate):
    gamedate2 = gamedate +  " 00:00:00"
    session = db.execute("SELECT * FROM mjsessions WHERE gamedate = :gamedate", {"gamedate": gamedate2}).fetchone()
    x = 1#session = db.execute("SELECT * FROM mjsessions WHERE id = :id", {"id": session_id}).fetchone()
    players = db.execute("SELECT * FROM mjplayer")
    playerlist = [1, 2, 3, 4, 5]
    playeroneid = session.playerone_id
    playerOneCommand = "SELECT * FROM mjplayer WHERE id = " + str(playeroneid)
    playerone = db.execute(playerOneCommand).fetchone()
    playeronename = playerone.name
    playeronescore = session.playerone_score
    if playerone.id == 1:
        playonename = playeronename
        playonescore = playeronescore
        playerlist.remove(1)
    if playerone.id == 2:
        playtwoname = playeronename
        playtwoscore = playeronescore
        playerlist.remove(2)

    if playerone.id == 3:
        playthreename = playeronename
        playthreescore = playeronescore
        playerlist.remove(3)

    if playerone.id == 4:
        playfourname = playeronename
        playfourscore = playeronescore
        playerlist.remove(4)

    if playerone.id == 5:
        playfivename = playeronename
        playfivescore = playeronescore
        playerlist.remove(5)

#Jerry[0], Meihui[1], Jason[2], Ben[3], Lingwei[4]

    playertwoid = session.playertwo_id
    playerTwoCommand = "SELECT * FROM mjplayer WHERE id = " + str(playertwoid)
    playertwo = db.execute(playerTwoCommand).fetchone()
    playertwoname = playertwo.name
    playertwoscore = session.playertwo_score
    if playertwo.id == 1:
        playeronename = playertwoname
        playeronescore = playertwoscore
        playerlist.remove(1)
    if playertwo.id == 2:
        playtwoname = playertwoname
        playtwoscore = playertwoscore
        playerlist.remove(2)
    if playertwo.id == 3:
        playthreename = playertwoname
        playthreescore = playertwoscore
        playerlist.remove(3)
    if playertwo.id == 4:
        playfourname = playertwoname
        playfourscore = playertwoscore
        playerlist.remove(4)
    if playertwo.id == 5:
        playfivename = playertwoname
        playfivescore = playertwoscore
        playerlist.remove(5)

    playerthreeid = session.playerthree_id
    playerThreeCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerthreeid)
    playerthree = db.execute(playerThreeCommand).fetchone()
    playerthreename = playerthree.name
    playerthreescore = session.playerthree_score
    if playerthree.id == 1:
        playonename = playerthreename
        playonescore = playerthreescore
        playerlist.remove(1)
    if playerthree.id == 2:
        playtwoname = playerthreename
        playtwoscore = playerthreescore
        playerlist.remove(2)
    if playerthree.id == 3:
        playthreename = playerthreename
        playthreescore = playerthreescore
        playerlist.remove(3)
    if playerthree.id == 4:
        playfourname = playerthreename
        playfourscore = playerthreescore
        playerlist.remove(4)
    if playerthree.id == 5:
        playfivename = playerthreename
        playfivescore = playerthreescore
        playerlist.remove(5)

    playerfourid = session.playerfour_id
    playerFourCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerfourid)
    playerfour = db.execute(playerFourCommand).fetchone()
    playerfourname = playerfour.name
    playerfourscore = session.playerfour_score

    if playerfour.id == 1:
        playonename = playerfourname
        playonescore = playerfourscore
        playerlist.remove(1)
    if playerfour.id == 2:
        playtwoname = playerfourname
        playtwoscore = playerfourscore
        playerlist.remove(2)
    if playerfour.id == 3:
        playthreename = playerfourname
        playthreescore = playerfourscore
        playerlist.remove(3)
    if playerfour.id == 4:
        playfourname = playerfourname
        playfourscore = playerfourscore
        playerlist.remove(4)
    if playerfour.id == 5:
        playfivename = playerfourname
        playfivescore = playerfourscore
        playerlist.remove(5)

    playerWhoDidNotPlay = playerlist[0]
    playerFiveCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerWhoDidNotPlay)
    playerfive = db.execute(playerFiveCommand).fetchone()

    playerfivename = playerfive.name
    playerfivescore = "Did Not Play"
    if playerfive.id == 1:
        playonename = playerfivename
        playonescore = playerfivescore
    if playerfive.id == 2:
        playtwoname = playerfivename
        playtwoscore = playerfivescore
    if playerfive.id == 3:
        playthreename = playerfivename
        playthreescore = playerfivescore
    if playerfive.id == 4:
        playfourname = playerfivename
        playfourscore = playerfivescore
    if playerfive.id == 5:
        playfivename = playerfivename
        playfivescore = playerfivescore
    dateString = str(session.gamedate)
    dateString = dateString[:10]
    scores = {
        x : dateString,
        playonename : playonescore,
        playtwoname : playtwoscore,
        playthreename : playthreescore,
        playfourname : playfourscore,
        playfivename : playfivescore
    }
    return render_template("session.html", score=scores, players=players)


#@app.route("/searchforbookbyisbn", methods=["GET", "POST"])

#@app.route("/createnewplayer")
#def session(createnewplayer):
#    sessionInsertCommand = "INSERT INTO mjsessions (gamedate, playerone_id, playertwo_id, playerthree_id, playerfour_id, playerone_score, playertwo_score, playerthree_score, playerfour_score) VALUES ('%s', '%d', '%d', '%d', '%d','%d', '%d', '%d', '%d')" % (date, playerone_id, playertwo_id, playerthree_id, playerfour_id, playerone_score, playertwo_score, playerthree_score, playerfour_score)
#    db.execute(sessionInsertCommand)
#    db.commit()
