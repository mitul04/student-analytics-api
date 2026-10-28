CREATE DATABASE student_analytics;

CREATE TABLE Branches (
    code VARCHAR(3) PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    id_prefix CHAR(2) UNIQUE NOT NULL /*or NOT NULL UNIQUE*/
);

INSERT INTO Branches VALUES
('CSE', 'Computer Science and Engineering', 'CS'),
('ECE', 'Electronics and Communication Engineering', 'EC'),
('EEE', 'Electrical and Electronics Engineering', 'EE'),
('CE',  'Civil Engineering', 'CE'),
('ME',  'Mechanical Engineering', 'ME'),
('RAI', 'Robotics and Artificial Intelligence', 'RA');

CREATE TABLE Students (
	id CHAR(7) PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	branch VARCHAR(3) NOT NULL,
	cgpa NUMERIC(4, 2) NOT NULL
		CHECK (cgpa BETWEEN 0 AND 10),
    FOREIGN KEY (branch) REFERENCES Branches(code)
);

INSERT INTO Students
(id, name, branch, cgpa)
VALUES
('26CS001', 'Mitul', 'CSE', 8.11),
('26CS002', 'Alice', 'CSE', 9.20),
('26EC001', 'Dell', 'ECE', 7.89),
('26EE001', 'Bob', 'EEE', 8.50),
('26RA001', 'Charlie', 'RAI', 9.10),
('26CE001', 'Diana', 'CE', 7.20),
('26ME001', 'Ethan', 'ME', 6.80),
('26CS003', 'Fiona', 'CSE', 9.50),
('26EC002', 'George', 'ECE', 8.30),
('26EE002', 'Hannah', 'EEE', 7.90),
('26RA002', 'Ian', 'RAI', 8.70),
('26CE002', 'Julia', 'CE', 8.10),
('26ME002', 'Kevin', 'ME', 7.40),
('26CS004', 'Laura', 'CSE', 9.00),
('26EC003', 'Michael', 'ECE', 8.80),
('26EE003', 'Nina', 'EEE', 8.20),
('26RA003', 'Oscar', 'RAI', 9.20),
('26CE003', 'Penelope', 'CE', 7.50),
('26ME003', 'Quentin', 'ME', 6.90),
('26CS005', 'Rachel', 'CSE', 8.60),
('26EC004', 'Sam', 'ECE', 7.70),
('26EE004', 'Tina', 'EEE', 8.40),
('26RA004', 'Uma', 'RAI', 9.60),
('26CE004', 'Victor', 'CE', 7.10),
('26ME004', 'Wendy', 'ME', 8.00),
('26CS006', 'Xander', 'CSE', 9.60),
('26EC005', 'Yara', 'ECE', 9.60);

/*
Test queries -----------------------------------------------------------------

SELECT
s.id, s.name, s.cgpa, b.full_name
FROM Students s
JOIN Branches b
ON s.branch = b.code
WHERE s.branch = 'CSE'
ORDER BY s.cgpa DESC
;

SELECT b.code, b.full_name,
COUNT(s.id) AS student_count, AVG(s.cgpa) AS average_cgpa
FROM Branches b
JOIN Students s ON b.code = s.branch
GROUP BY b.code, b.full_name
ORDER BY average_cgpa DESC
;

SELECT s1.id, s1.name, s1.cgpa
FROM Students s1
WHERE s1.cgpa >= (
	SELECT AVG(cgpa) FROM Students s2
	WHERE s2.branch = s1.branch
)
ORDER BY s1.cgpa DESC
;

SELECT
id, name, branch, cgpa, RANK() OVER (
	PARTITION BY branch
	ORDER BY cgpa DESC
) AS rank_in_branch
FROM Students
;

SELECT id, name, branch, cgpa,
ROUND(AVG(cgpa) OVER (PARTITION BY branch), 2) as branch_average,
RANK() OVER (PARTITION BY branch ORDER BY cgpa DESC) as branch_rank
FROM students
ORDER BY branch, branch_rank
;

WITH branch_stats AS (
	SELECT id, name, branch, cgpa,
	ROUND(AVG(cgpa) OVER (PARTITION BY branch), 2) as branch_average,
	RANK() OVER (PARTITION BY branch ORDER BY cgpa DESC) as branch_rank
	FROM students
	ORDER BY branch, branch_rank
)
SELECT * FROM branch_stats
WHERE branch_rank <=3 AND cgpa >= branch_average
ORDER BY branch, branch_rank
;

CREATE VIEW student_performance AS
SELECT name, branch, cgpa,
CASE
	WHEN cgpa >= 9 THEN 'Excellent'
	WHEN cgpa >= 8 THEN 'Good'
	WHEN cgpa >= 7 THEN 'Average'
	ELSE 'Below Average'
	END
AS performance
FROM students
ORDER BY branch, name, cgpa DESC
;

SELECT branch, COUNT(*) AS student_count,
COUNT(CASE WHEN cgpa >= 9 THEN 1 END) AS excellent_count,
COUNT(CASE WHEN cgpa >= 8 AND cgpa < 9 THEN 1 END) AS good_count,
COUNT(CASE WHEN cgpa >= 7 AND cgpa < 8 THEN 1 END) AS average_count,
COUNT(CASE WHEN cgpa < 7 THEN 1 END) AS below_average_count
FROM students
GROUP BY branch

CREATE INDEX idx_students_branch ON students(branch);
			

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name IN ('branches', 'students', 'alembic_version')
ORDER BY table_name;


SELECT
    tc.table_name,
    tc.constraint_name,
    tc.constraint_type
FROM information_schema.table_constraints AS tc
WHERE tc.table_schema = 'public'
  AND tc.table_name IN ('branches', 'students')
ORDER BY tc.table_name, tc.constraint_type, tc.constraint_name;


*/