-- Makes a list with columns involving 3 fields
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows_genres
WHERE tv_shows.id = tv_show_genres.show_id
