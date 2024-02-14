-- This lists all shows, and all genres linked to that show


-- select the show's title, and the genre name
SELECT ts.title, tg.name
FROM tv_shows ts
	-- grab everything from the shows and their respective show IDs
	LEFT JOIN tv_show_genres tsg
		ON ts.id = tsg.show_id
	-- grab the genre based of the show
	LEFT JOIN tv_genres tg
		ON tg.id = tsg.genre_id
-- order the results by the show name, then the genre name
ORDER BY ts.title, tg.name;
