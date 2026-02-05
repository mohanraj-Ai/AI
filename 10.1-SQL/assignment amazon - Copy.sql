CREATE DATABASE NetflixDB;
USE NetflixDB;

CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    registration_date DATE NOT NULL,
    plan ENUM('Basic', 'Standard', 'Premium') DEFAULT 'Basic'
);

CREATE TABLE Movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    release_year YEAR NOT NULL,
    rating DECIMAL(3, 1) NOT NULL
);

CREATE TABLE WatchHistory (
    watch_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    movie_id INT,
    watched_date DATE NOT NULL,
    completion_percentage INT CHECK (completion_percentage >= 0 AND completion_percentage <= 100),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    review_text TEXT,
    rating DECIMAL(2, 1) CHECK (rating >= 0 AND rating <= 5),
    review_date DATE NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Users (name, email, registration_date, plan) 
VALUES
('John Doe', 'john.doe@example.com', '2024-01-10', 'Premium'),
('Jane Smith', 'jane.smith@example.com', '2024-01-15', 'Standard'),
('Alice Johnson', 'alice.johnson@example.com', '2024-02-01', 'Basic'),
('Bob Brown', 'bob.brown@example.com', '2024-02-20', 'Premium');

INSERT INTO Movies (title, genre, release_year, rating) 
VALUES
('Stranger Things', 'Drama', 2016, 8.7),
('Breaking Bad', 'Crime', 2008, 9.5),
('The Crown', 'History', 2016, 8.6),
('The Witcher', 'Fantasy', 2019, 8.2),
('Black Mirror', 'Sci-Fi', 2011, 8.8);

INSERT INTO WatchHistory (user_id, movie_id, watched_date, completion_percentage) 
VALUES
(1, 1, '2024-02-05', 100),
(2, 2, '2024-02-06', 80),
(3, 3, '2024-02-10', 50),
(4, 4, '2024-02-15', 100),
(1, 5, '2024-02-18', 90);

INSERT INTO Reviews (movie_id, user_id, review_text, rating, review_date) 
VALUES
(1, 1, 'Amazing storyline and great characters!', 4.5, '2024-02-07'),
(2, 2, 'Intense and thrilling!', 5.0, '2024-02-08'),
(3, 3, 'Good show, but slow at times.', 3.5, '2024-02-12'),
(4, 4, 'Fantastic visuals and acting.', 4.8, '2024-02-16');

select * from  Reviews
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