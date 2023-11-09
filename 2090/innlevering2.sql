BEGIN;

-- OPPGAVE 1

CREATE TABLE stjerne (
	navn text PRIMARY KEY,
	avstand int,
	masse float
);

CREATE TABLE planet (
	navn text PRIMARY KEY,
	masse float,
	oppdaget date,
	stjerne text REFERENCES stjerne(navn)
);

CREATE TABLE materie (
	planet text REFERENCES planet(navn),
	molekyl int NOT NULL,
	CONSTRAINT m_pk PRIMARY KEY (planet, molekyl)
);


-- OPPGAVE 2


-- a)

SELECT navn FROM planet WHERE stjerne LIKE 'Proxima Centauri';

-- b)

SELECT DISTINCT oppdaget FROM planet WHERE stjerne LIKE 'TRAPPIST-1' OR stjerne LIKE 'Kepler-154';

-- c)

SELECT COUNT(*) FROM planet WHERE masse IS NULL;

-- d)

SELECT navn, masse FROM planet WHERE oppdaget = '2020' AND masse >= (SELECT AVG(masse) FROM planet);

-- e)

SELECT MAX(oppdaget)-MIN(oppdaget) FROM planet;


-- OPPGAVE 3


--a)

SELECT p.navn FROM planet AS p INNER JOIN materie AS m 
ON p.navn = m.planet WHERE p.masse < 10 
AND p.masse > 3 AND m.molekyl = 'H2O';

-- b)

SELECT p.navn FROM planet AS p INNER JOIN stjerne AS s 
ON p.stjerne = s.navn INNER JOIN materie AS m 
ON p.navn = m.planet 
WHERE s.avstand < p.masse*12 AND m.molekyl = '%H%';

-- c)

SELECT p.navn FROM planet as p INNER JOIN stjerne AS s 
ON p.stjerne = s.navn WHERE p.masse > 10 AND s.avstand < 50;


-- Oppgave 4.

/*
Ved bruken av NATURAL JOIN vil tabellene stjerne og planet joines ved attributtene navn, men også ved attributtene masse, noe vi ikke ønsker. 

En fungerende spørring med ønsket resultat kunne vært:
*/

SELECT p.oppdaget FROM planet AS p INNER JOIN stjerne AS s 
ON p.stjerne = s.navn WHERE s.avstand > 5000;


-- OPPGAVE 5


-- a)

INSERT INTO stjerne VALUES ('Sola', 0, 1);

-- b)

INSERT INTO planet VALUES ('Jorda', 0.003146, Null, 
(SELECT navn FROM stjerne WHERE navn LIKE 'Sola'));


-- OPPGAVE 6


CREATE TABLE observasjon (
	observasjon_id int PRIMARY KEY,
	tidspunkt timestamp,
	planet text REFERENCES planet(navn),
	kommentar text
);

-- jeg er usikker på om jeg burde gjøre noe for å
-- referere tidspunkt til planet(oppdaget), isåfall hvordan?

COMMIT;