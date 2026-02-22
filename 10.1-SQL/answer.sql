-- 1. List all users subscribed to the Premium plan:
select name
from Users
where plan='premium';

-- 2. Retrieve all movies in the Drama genre with a rating higher than 8.5:
select title,genre,rating
from Movies
where genre='drama' and rating>8.5;

3.3. Find the average rating of all movies released after 2015:
SELECT AVG(rating) AS average_rating 
FROM Movies 
WHERE release_year > 2015;

4. List the names of users who have watched the movie Stranger Things along with their completion percentage:
select Users.name, WatchHistory.completion_percentage 
FROM Users 
JOIN WatchHistory  ON Users.user_id = WatchHistory.user_id
JOIN Movies  ON WatchHistory.movie_id = Movies.movie_id 
WHERE Movies.title = 'Stranger Things';

 5. Find the name of the user(s) who rated a movie the highest among all reviews:
 select Users.name
 from Users
left JOIN Reviews  ON Users.user_id = Reviews.user_id 
Where Reviews.rating = (SELECT MAX(rating) FROM Reviews);
6. Calculate the number of movies watched by each user and sort by the highest count
SELECT Users.name, COUNT(WatchHistory.watch_id) AS movies_watched 
FROM Users 
JOIN WatchHistory  ON Users.user_id = WatchHistory.user_id 
GROUP BY Users.user_id 
ORDER BY movies_watched DESC;

7.List all movies watched by John Doe, including their genre, rating, and his completion percentage:
SELECT Movies.title, Movies.genre, Movies.rating, WatchHistory.completion_percentage 
FROM Movies 
JOIN WatchHistory  ON Movies.movie_id = WatchHistory.movie_id
JOIN Users  ON WatchHistory.user_id = Users.user_id
WHERE Users.name = 'John Doe';
 
 - 8.Update the movie's rating for Stranger Things:
 set sql_safe_updates=0;
 UPDATE Movies 
SET rating = 8.9 
WHERE title = 'Stranger Things';
 
 -- 9.Remove all reviews for movies with a rating below 4.0:
DELETE FROM Reviews 
WHERE movie_id IN (SELECT movie_id FROM Movies WHERE rating < 4.0);

- 10. Fetch all users who have reviewed a movie but have not watched it completely (completion percentage < 100):
SELECT Users.name, Movies.title, Reviews.review_text 
FROM Users Users
JOIN Reviews  ON Users.user_id = Reviews.user_id
JOIN Movies  ON Reviews.movie_id = Movies.movie_id
LEFT JOIN WatchHistory  ON Users.user_id = WatchHistory.user_id AND Movies.movie_id = WatchHistory.movie_id
WHERE (WatchHistory.completion_percentage IS NULL OR WatchHistory.completion_percentage < 100);

- 11. List all movies watched by John Doe along with their genre and his completion percentage:
SELECT Movies.title, Movies.genre, WatchHistory.completion_percentage 
FROM Movies 
JOIN WatchHistory  ON Movies.movie_id = WatchHistory.movie_id
JOIN Users  ON WatchHistory.user_id = Users.user_id
WHERE Users.name = 'John Doe';

-- 12.Retrieve all users who have reviewed the movie Stranger Things, including their review text and rating:
SELECT Users.name, Reviews.review_text, Reviews.rating 
FROM Users 
JOIN Reviews  ON Users.user_id = Reviews.user_id
JOIN Movies  ON Reviews.movie_id = Movies.movie_id
WHERE Movies.title = 'Stranger Things';

-- 13. Fetch the watch history of all users, including their name, email, movie title, genre, 
watched date, and completion percentage:

SELECT Users.name, Users.email, Movies.title, Movies.genre, WatchHistory.watched_date, WatchHistory.completion_percentage 
FROM Users 
JOIN WatchHistory  ON Users.user_id = WatchHistory.user_id
JOIN Movies ON WatchHistory.movie_id = Movies.movie_id;

- 14.List all movies along with the total number of reviews and average rating for each movie, 
including only movies with at least two reviews:
SELECT Movies.title, COUNT(Reviews.review_id) AS total_reviews, AVG(Reviews.rating) AS average_rating 
FROM Movies 
JOIN Reviews  ON Movies.movie_id = Reviews.movie_id
GROUP BY Movies.movie_id
HAVING COUNT(Reviews.review_id) >= 2;