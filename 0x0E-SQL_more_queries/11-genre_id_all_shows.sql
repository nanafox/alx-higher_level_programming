-- This script list all showws contained in the database 'htbn_0d_tvshows' that
-- have a genre or none


-- select the TV show and the TV show genre fields
SELECT ts.title, tsg.genre_id
-- bring in everything from the TV show table 
FROM tv_shows ts LEFT JOIN tv_show_genres tsg
	ON ts.id = tsg.show_id
-- order by the show's title, then the show id.
ORDER BY ts.title, tsg.genre_id;
