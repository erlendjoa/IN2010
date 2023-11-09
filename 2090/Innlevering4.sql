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

WITH genrepop AS (
    SELECT DISTINCT ON (country) country, genre, count(*) as countg
    FROM filmcountry AS fc
    JOIN filmgenre AS fg ON fc.filmid = fg.filmid
    GROUP BY country, genre
    ORDER BY country, genre DESC
)
SELECT fc.country, count(fc.country) AS antallfilmer, avg(fr.rank) as averagerank, gp.genre
FROM film AS f
JOIN filmrating AS fr ON f.filmid = fr.filmid
JOIN filmcountry AS fc ON f.filmid = fc.filmid
JOIN genrepop AS gp ON gp.country = fc.country
GROUP BY fc.country, gp.genre
ORDER BY fc.country;

-- Oppgave 6 - Vennskap

SELECT fc2.country, fc1.country
FROM filmcountry AS fc1, filmcountry AS fc2
WHERE fc1.filmid = fc2.filmid AND fc1.country < fc2.country
GROUP BY fc1.country, fc2.country
HAVING count(fc2.country) > 150;

-- Oppgave 7 - Mot

SELECT f.title, f.prodyear
FROM film AS f
JOIN filmcountry AS fc ON f.filmid = fc.filmid
JOIN filmgenre AS fg ON f.filmid = fg.filmid
WHERE (f.title LIKE '%Dark%' OR f.title LIKE '%Night%')
AND (fg.genre = 'Horror' OR fc.country = 'Romania');

-- Oppgave 8 - Lunsj

WITH cf AS (
    SELECT fp.filmid, count(fp.personid) AS countid
    FROM filmparticipation AS fp
    GROUP BY fp.filmid
)
SELECT f.title, cf.countid
FROM film AS f
JOIN cf ON f.filmid = cf.filmid
WHERE f.prodyear >= 2010 AND cf.countid <= 2;

-- Oppgave 9 - Introspeksjon

SELECT count(f.filmid)
FROM filmgenre as fg
JOIN film AS f ON f.filmid = fg.filmid
WHERE genre != 'Sci-Fi' AND genre!= 'Horror';

-- Oppgave 10 - Kompetanseheving

WITH intf AS (
    SELECT fr.filmid
    FROM filmrating AS fr
    WHERE fr.rank >= 8 AND fr.votes > 1000
),
rf AS (
    SELECT fr.filmid, fr.rank, fr.votes
    FROM filmrating AS fr
    JOIN intf ON intf.filmid = fr.filmid
    ORDER BY fr.rank, fr.votes DESC
    LIMIT 10
),
hf AS (
    SELECT fp.filmid
    FROM filmparticipation AS fp
    JOIN person AS p ON p.personid = fp.personid
    JOIN intf ON intf.filmid = fp.filmid
    WHERE p.firstname = 'Harrison' AND p.lastname = 'Ford'
),
cr AS ( 
    SELECT fg.filmid
    FROM filmgenre AS fg
    JOIN intf ON intf.filmid = fg.filmid
    WHERE fg.genre = 'Comedy' OR fg.genre = 'Romance'
)
SELECT intf.filmid
FROM intf
FULL JOIN rf ON intf.filmid = rf.filmid
FULL JOIN hf ON intf.filmid = hf.filmid
FULL JOIN cr ON intf.filmid = cr.filmid
WHERE intf.filmid = rf.filmid
OR intf.filmid = hf.filmid
OR intf.filmid = cr.filmid;