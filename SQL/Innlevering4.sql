-- Oppgave 1 - Oppvarming

SELECT COUNT(p.PersonID) FROM filmparticipation as fp
INNER JOIN film AS f ON f.FilmID = fp.FilmID
INNER JOIN person AS p ON p.PersonID = fp.PersonID
WHERE f.title LIKE 'Star Wars';

-- Oppgave 2 - Land

SELECT Country, COUNT(*) AS Countrycount
FROM filmcountry GROUP BY Country ORDER BY Countrycount DESC;

-- Oppgave 3 - Spilletider

SELECT rt.country, AVG(rt.time) FROM runningtime AS rt 
INNER JOIN film as f
ON rt.filmid = f.FilmID
WHERE time ~ '^\d+$'
GROUP BY rt.country;