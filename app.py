import os
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bootstrap import Bootstrap
import requests
import json
from datetime import datetime
from decimal import Decimal

os.environ.get('TIMES')

app = Flask(__name__)
URL = os.environ.get('DATABASE_URL2')
SECRETKEY = os.environ.get('SECRET_KEY')
GRRequestKey = os.environ.get('GRRequestKey')
engine = create_engine(URL)
db = scoped_session(sessionmaker(bind=engine))
bootstrap = Bootstrap(app)


class SessionRecord:

    def __init__(self, players,session):
        self.date = date
        self.players = players
        self.session = session

@app.route("/allsessions")
def allsessions():
    allsessions = []

    sessions = db.execute("SELECT * FROM mjsessions")
    #players = db.execute("SELECT * FROM players")
    x = 1
    for session in sessions:
        playeroneid = session.playerone_id
        playerOneCommand = "SELECT * FROM mjplayer WHERE id = " + str(playeroneid)
        playerone = db.execute(playerOneCommand).fetchone()
        playeronename = playerone.name
        playeronescore = session.playerone_score

        playertwoid = session.playertwo_id
        playerTwoCommand = "SELECT * FROM mjplayer WHERE id = " + str(playertwoid)
        playertwo = db.execute(playerTwoCommand).fetchone()
        playertwoname = playertwo.name
        playertwoscore = session.playertwo_score

        playerthreeid = session.playerthree_id
        playerThreeCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerthreeid)
        playerthree = db.execute(playerThreeCommand).fetchone()
        playerthreename = playerthree.name
        playerthreescore = session.playerthree_score

        playerfourid = session.playerfour_id
        playerFourCommand = "SELECT * FROM mjplayer WHERE id = " + str(playerfourid)
        playerfour = db.execute(playerFourCommand).fetchone()
        playerfourname = playerfour.name
        playerfourscore = session.playerfour_score
        dateString = str(session.gamedate)
        dateString = dateString[:10]


        scores = {
            x : dateString,
            playeronename : playeronescore,
            playertwoname : playertwoscore,
            playerthreename : playerthreescore,
            playerfourname : playerfourscore
        }
        allsessions.append(scores)
        x = x + 1
    return render_template("allsessions.html", allsessions=allsessions)

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
    return render_template("players.html", players=mjplayers)


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

    return render_template("allsessions.html")
#@app.route("/createnewplayer", methods=["GET", "POST"])
#def createnewplayer()


#@app.route("/searchforbookbyisbn", methods=["GET", "POST"])

#@app.route("/createnewplayer")
