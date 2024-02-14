-- This script list all genres from the 'hbtn_0d_tvshows' database and
-- displays the number of shows linked to each

-- retrieve the genre and get the number of shows for that genre
SELECT tg.name AS genre, count(tsg.genre_id) AS number_of_shows
FROM tv_genres tg JOIN tv_show_genres tsg
	ON tg.id = tsg.genre_id
-- group the results by the genre name
GROUP BY tg.name
-- order the results by the genre with the most TV shows
ORDER BY number_of_shows DESC;
