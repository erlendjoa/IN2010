-- Oppgave 1 - Oppvarming

SELECT count(p.PersonID) FROM filmparticipation as fp
INNER JOIN film AS f ON f.FilmID = fp.FilmID
INNER JOIN person AS p ON p.PersonID = fp.PersonID
WHERE f.title LIKE 'Star Wars%' AND fp.parttype = "cast";

-- Oppgave 2 - Land

SELECT Country, count(*) AS Countrycount
FROM filmcountry GROUP BY Country ORDER BY Countrycount DESC;

-- Oppgave 3 - Spilletider

SELECT rt.country, avg(cast(rt.time AS int)) FROM runningtime AS rt 
INNER JOIN film as f
ON rt.filmid = f.FilmID
WHERE time ~ '^\d+$' AND cast(rt.time AS int) > 200
GROUP BY rt.country;

-- Oppgave 4 - Komplekse mennesker

SELECT f.title, newTable.c FROM film AS f INNER JOIN 
(SELECT fg.filmid, count(fg.filmid) AS c FROM filmgenre AS fg
GROUP BY fg.filmid ORDER BY c DESC LIMIT 10) AS newTable 
ON f.filmid = newTable.filmid;


-- Oppgave 5 - Land og filmvaner

SELECT fc.country, count(fc.country) AS antallfilmer, avg(fr.rank) as averagerank
FROM film AS f
JOIN filmrating AS fr ON f.filmid = fr.filmid
JOIN filmcountry AS fc ON f.filmid = fc.filmid
GROUP BY fc.country;


    SELECT fc.country, count(fc.country) AS antallfilmer, avg(fr.rank) as averagerank, fg.genre
    FROM film AS f
    JOIN filmrating AS fr ON f.filmid = fr.filmid
    JOIN filmcountry AS fc ON f.filmid = fc.filmid
    JOIN filmgenre AS fg ON f.filmid = fg.filmid
    GROUP BY fc.country, fg.genre;