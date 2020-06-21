CREATE TABLE mjsessions (
    id SERIAL PRIMARY KEY,
    gamedate DATE NOT NULL,
    playerone_id INTEGER NOT NULL,
    playertwo_id INTEGER NOT NULL,
    playerthree_id INTEGER NOT NULL,
    playerfour_id INTEGER NOT NULL,
    playerone_score DECIMAL(5,2),
    playertwo_score DECIMAL(5,2),
    playerthree_score DECIMAL(5,2),
    playerfour_score DECIMAL(5,2)
);

CREATE TABLE mjplayer (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

SELECT * FROM mjsession;
SELECT * FROM mjplayer;

INSERT INTO mjplayer (name) VALUES ('Jerry');
INSERT INTO mjplayer (name) VALUES ('Meihui');
INSERT INTO mjplayer (name) VALUES ('Jason');
INSERT INTO mjplayer (name) VALUES ('Ben');
INSERT INTO mjplayer (name) VALUES ('Lingwei');

URL="postgres://bjwxmuebywiexo:cbb7614809a4bba5aa0a32b18dbef509fed6732c10ca07a2b81dc2dac043d721@ec2-54-211-210-149.compute-1.amazonaws.com:5432/d2n3ohvdkibnt3"
app.config['SECRET_KEY']="OCML3BRawWEUeaxcuKHLpw"
GRRequestKey="GZ4LbC681pT1BZJO6WLQ"

git push heroku master
heroku ps:scale web=1
heroku open
heroku ps
heroku logs --tail
