-- This script lists all shows from the 'hbtn_0d_tvshows_rate' database by
-- their rating


SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_shows ts
	JOIN tv_show_ratings tsr
		ON ts.id = tsr.show_id
GROUP BY ts.id
ORDER BY rating DESC;
