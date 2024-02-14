-- This script uses the 'htbn_0d_tvshows' database to lists all genre of the
-- 'Dexter'

-- select the genre name
SELECT tg.name
FROM tv_genres tg
	JOIN tv_show_genres tsg
		ON tg.id = tsg.genre_id
	JOIN tv_shows ts
		ON ts.id = tsg.show_id
-- filter for records with title 'Dexter'
WHERE ts.title = "Dexter"
-- order by the genre name
ORDER BY tg.name;
