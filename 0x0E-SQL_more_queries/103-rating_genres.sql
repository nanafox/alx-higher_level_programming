-- This script lists all the genres in the database 'hbtn_0d_tvshows_rate' by
-- their rating

SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres tg
	JOIN tv_show_genres tsg
		ON tg.id = tsg.genre_id
	JOIN tv_show_ratings tsr
		ON tsg.show_id = tsr.show_id
GROUP BY tg.id
ORDER BY rating DESC;
