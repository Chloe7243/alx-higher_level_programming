-- uses the hbtn_0d_tvshows database to lists all shows of the comedy genre.
SELECT title from tv_shows
WHERE title NOT IN (
SELECT tv_shows.title FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id AND tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC
