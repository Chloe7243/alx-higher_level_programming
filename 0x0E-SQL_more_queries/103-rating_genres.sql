--  lists all shows from hbtn_0d_tvshows_rate by their rating

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres, tv_show_genres, tv_show_ratings WHERE tv_show_genres.show_id = tv_show_ratings.show_id AND tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.id ORDER BY rating DESC
