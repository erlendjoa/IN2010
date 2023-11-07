-- 1

SELECT DISTINCT filmtype FROM filmitem;

"""
 filmtype 

 C
 E
 TV
 TVS
 V
 VG
 mini
(7 rows)
"""

-- 2

SELECT s.maintitle, s.firstprodyear, count(e.episodeid) AS episodes
FROM series as s
INNER JOIN episode as e ON s.seriesid = e.seriesid
GROUP BY e.seriesid, s.maintitle, s.firstprodyear
ORDER BY episodes DESC LIMIT 15;