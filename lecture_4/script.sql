-- 1. Create tables
CREATE TABLE students (
	id INTEGER PRIMARY KEY,
	full_name TEXT NOT NULL,
	birth_year INTEGER
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK(grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Create indexes for table 'students'
CREATE INDEX idx_students_full_name ON students(full_name);

CREATE INDEX idx_students_birth_year ON students(birth_year);

-- Create indexes for table 'grades'
CREATE INDEX idx_grades_student_id ON grades(student_id);

CREATE INDEX idx_grades_subject ON grades(subject);

CREATE INDEX idx_grades_student_subject ON grades(student_id, subject);

-- 2. Insert data into table 'students'
INSERT INTO students (full_name, birth_year) VALUES 
('Alice Johnson', 2005),
('Brain Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert data into table 'grades'
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2 ,'History', 83),
(2 ,'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- 3. Find all grades for specific student(Alice Johnson)
SELECT g.id, g.subject, g.grade from grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 4. Calculate the average grade per student
SELECT s.id, s.full_name, ROUND(AVG(g.grade), 1) AS avg_grade
FROM students s 
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.full_name;

-- 5. List all students born after 2004
SELECT id, full_name, birth_year FROM students
WHERE  birth_year > 2004;

-- 6. List all subject and their average grade
SELECT g.id, g.subject, ROUND(AVG(g.grade), 1) AS avg_grade
FROM grades g
GROUP BY g.id, g.subject;

-- 7. Find top 3 students with the highest average grades
SELECT s.id, s.full_name, ROUND(AVG(g.grade), 1) as avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id 
GROUP BY s.id, s.full_name 
ORDER BY avg_grade DESC
LIMIT 3;

-- 8. Show all students who have scored below 80 in any subject
SELECT DISTINCT s.id, s.full_name
FROM students s
JOIN grades g on g.student_id = s.id
WHERE g.grade < 80;

-- 8. Same but with subjects names and scores below 80
SELECT s.id, s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON g.student_id = s.id
WHERE g.grade < 80;
