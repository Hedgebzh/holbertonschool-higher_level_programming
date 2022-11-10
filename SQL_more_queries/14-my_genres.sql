-- Task description : Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name AS name
FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.name
WHERE tv_show_genres.show_id = 8
ORDER BY name;
