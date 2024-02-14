-- This script list all shows with the genre 'Comedy'


SELECT title
FROM tv_shows
-- grab the shows that are not based on comedy
WHERE title NOT IN (
    SELECT ts.title 
    FROM tv_shows ts
    LEFT JOIN tv_show_genres tsg
		ON ts.id = tsg.show_id
    LEFT JOIN tv_genres tg
		ON tsg.genre_id = tg.id
    WHERE tg.name = "Comedy"
)
GROUP BY title
ORDER BY title;
