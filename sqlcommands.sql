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
