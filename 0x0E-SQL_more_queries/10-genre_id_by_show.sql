-- This script lists all shows contained in the database 'hbtn_0d_tvshows' that
-- have at least one genre linked

-- select the TV show and the TV show genre fields
SELECT ts.title, tsg.genre_id
FROM tv_shows ts JOIN tv_show_genres tsg
	ON ts.id = tsg.show_id
-- order by the show's title, then the show id.
ORDER BY ts.title, tsg.genre_id;
