
CREATE DATABASE practice_db
USE practice_db
SHOW DATABASES;
CREATE TABLE students(
	student_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);    
ALTER TABLE students
ADD phone_number VARCHAR(15);
ALTER TABLE students
MODIFY last_name VARCHAR(50) NOT NULL
CREATE TABLE courses(
	course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL UNIQUE,
    credits INT CHECK (credits BETWEEN 1 AND 5)
);    
_
 CREATE TABLE enrollment (
	enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT, 
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
 );   
 INSERT INTO students(first_name,last_name,email,enrollment_date)
 VALUES('john','doe','john.doe@example.com','2024-11-21');
 ALTER TABLE students
 DROP COLUMN student_id;
 INSERT INTO students(first_name,last_name,email,enrollment_date)
 VALUES
 ('jane','smith','janesmith@example.com','2024-11-20'),
 ('alice','johnson','alicejohnson@example.com','2024-11-19')
 SELECT * from students;
 ALTER TABLE students
 DROP COLUMN phone_number;
 UPDATE students
 SET email='john.newemail@example.com'
 WHERE student_id=1;
 SET SQL_SAFE_UPDATES=0;
 UPDATE students
 SET last_name='brown',email='jane.brown@example.com'
 WHERE first_name='jane';

UPDATE students
SET enrollment_date='2024-11-20';
CREATE TABLE archieved_students(
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);   

INSERT INTO archieved_students(student_id,first_name,last_name,email,enrollment_date)
SELECT student_id,first_name,last_name,email,enrollment_date FROM students
WHERE enrollment_date='2024-11-20';

START TRANSACTION;
INSERT INTO students(first_name,last_name,email,enrollment_date)
VALUES('anna','taylor','anna.taylor@example.com','2024-11-16');
select * from students
SAVEPOINT before_update;
UPDATE students
SET email='invalid.email@example.com'
WHERE student_id=2;
ROLLBACK TO before_update;

SELECT first_name,email
FROM students;
SELECT first_name,last_name,enrollment_date
FROM students
WHERE enrollment_date>'2024-01-01';
SELECT first_name,last_name,enrollment_date
FROM students
WHERE enrollment_date BETWEEN '2024-01-01' AND '2024-12-31' AND last_name='taylor';
SELECT first_name,last_name,enrollment_date
FROM students
ORDER BY enrollment_date DESC;
SELECT first_name,last_name
FROM students
LIMIT 2;
 ALTER TABLE students
 ADD MARKS VARCHAR(3);
 ALTER TABLE students
 modify MARKS INT;
 SELECT * FROM students
 UPDATE students
 SET MARKS=CASE
	when student_id=2 then 35
    when student_id=3 then 45
    when student_id=4 then 75
    else MARKS
END
WHERE student_id IN(2,3,4); 
SELECT sum(MARKS) AS sumofmarks
from students;   

select
	sum(MARKS) AS total_marks,
    AVG(MARKS) AS AVERAGE_MARKS,
    MIN(MARKS) AS MIN_MARKS,
    MAX(MARKS) AS MAX_MARKS
FROM students
group by student_id;   
 
select * from students
select * from courses
select * from enrollment
Insert into courses (course_id,course_name,credits)
values (101,"AI",3),
(102,"ML",2),
(103,"DL",3);
insert into enrollment(enrollment_id,student_id,course_id)
values(001,1, 101),  -- John Doe enrolls in Mathematics
       (002,2, 102),  -- Jane Smith enrolls in Science
       (003,3, 103);  -- Alice Johnson enrolls in Computer Science
SELECT students.first_name, students.last_name,enrollment.course_id,students.student_id
from students
inner join enrollment on students.student_id=enrollment.student_id;    

SELECT students.first_name, courses.course_name 
FROM students 
LEFT JOIN enrollment ON students.student_id = enrollment.student_id 
LEFT JOIN courses ON enrollment.course_id = courses.course_id;