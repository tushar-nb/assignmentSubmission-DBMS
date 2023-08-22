---------------------------------------------Constraints-----------------------------------------------------------

ALTER TABLE classes 
ADD CONSTRAINT test1 FOREIGN KEY (facultyId) REFERENCES faculties(facultyId) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE students 
ADD CONSTRAINT test2 FOREIGN KEY (classCode) REFERENCES classes(classCode) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE assignments
ADD CONSTRAINT test3 FOREIGN KEY (classCode) REFERENCES classes(classCode) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT test4 FOREIGN KEY (facultyId) REFERENCES faculties(facultyId) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE submissions
ADD CONSTRAINT test5 FOREIGN KEY (srn) REFERENCES students(srn) ON DELETE CASCADE ON UPDATE CASCADE,
ADD CONSTRAINT test6 FOREIGN KEY (assignmentId) REFERENCES assignments(assignmentId) ON DELETE CASCADE ON UPDATE CASCADE;

----------------------------------------------JOIN------------------------------------------------------------------
SELECT faculties.facultyId, faculties.firstName,faculties.lastName,faculties.email,classes.className FROM faculties INNER JOIN classes on faculties.facultyId = "PES020";

SELECT classes.classCode , classes.course, classes.className , assignments.assignmentNumber, assignments.title, assignments.deadline from classes INNER JOIN assignments ON classes.classCode = "CC100";

SELECT assignments.assignmentId , assignments.title, assignments.deadline ,faculties.facultyId,faculties.firstName,faculties.lastName from assignments INNER JOIN faculties ON faculties.facultyId = "PES020";

SELECT submissions.response,submissions.status,submissions.createdAt,students.srn,students.name FROM submissions INNER JOIN students ON students.srn = "PES1UG20CS608";

------------------------------------------------AGGREGATE FUNICTIONS------------------------------------------------------
SELECT COUNT(*) FROM students WHERE classCode = "CC100" ;

SELECT sum(marks) FROM submissions WHERE srn="PES1UG20CS608";

SELECT count(classCode) FROM classes;

SELECT AVG(marks) from submissions;

---------------------------------------------SET OPERATIONS --------------------------------------------------------

SELECT * FROM assignments where classCode="CC100" UNION SELECT * FROM assignments where classCode = "fio2934";


SELECT * FROM students WHERE classCode = "CC100" INTERSECT SELECT * FROM students WHERE classCode = "fio2934";

SELECT srn FROM students EXCEPT SELECT srn FROM submissions;

SELECT name FROM students
INTERSECT
SELECT srn FROM submissions WHERE submissions.status=1;

--------------------------------------------- Functions ----------------------------------------------------------
-- function which returns number of students who belongs to that class using classCode
DELIMITER $$
CREATE FUNCTION getNumberOfStudents(classCode varchar(40))
RETURNS int
DETERMINISTIC
BEGIN
    DECLARE numberOfStudents int DEFAULT 0 ;
    set numberOfStudents = (SELECT COUNT(*) FROM students WHERE students.classCode = classCode);
    return numberOfStudents;
END
$$
DELIMITER ;

SELECT getNumberOfStudents('CC100');

-----------------------------------------------------------------
DELIMITER $$
CEATE FUNCTION getClaims(monthNum int)
RETURNS table
AS 
RETURN
SELECT
  --claim details,person details,insurance details to display
FROM claims
JOIN customer                              --check dis attributes once
  ON customer.id = claim.id
JOIN plan
  ON customer.id = plan.id;
where month(claims.date) = monthNum;
$$
DELIMITER ;

SELECT getClaims(2);
--------------------------------------------------PROCEDURE-----------------------------------------------------------
--procedure to create a student backup table 
DELIMITER $$
CREATE PROCEDURE backup_table()
 BEGIN
 DECLARE done int(11);
 DECLARE srn varchar(15);
 DECLARE name varchar(15);
 DECLARE cr varchar(10);
 DECLARE isCr int(11);
 DECLARE classCode varchar(10);
 DECLARE cur CURSOR FOR SELECT * FROM students;
 DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
 OPEN cur;
 label: LOOP
 FETCH cur INTO srn,name,cr,isCr,classCode;
 CREATE TABLE IF NOT EXISTS students_backup(srn varchar(15),name varchar(20),cr varchar(10),isCr int(10),classCode varchar(10));
 INSERT INTO students_backup VALUES(srn,name,cr,isCr,classCode);
 IF done = 1 THEN LEAVE label;
 END IF;
 END LOOP;
 CLOSE cur;
 END;$$
 DELIMITER ;

CALL backup_table();
SELECT * FROM students_backup;

-------------------------------------------Triggers----------------------------------------------------------

delimiter $$
CREATE TRIGGER  check_marks  BEFORE INSERT ON submissions 
FOR EACH ROW
BEGIN
IF NEW.marks < 0 THEN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'ERROR: 
    	     MARKS CANNOT BE NEGATIVE!'
END IF;
END; $$
delimiter;; 

delimiter $$
CREATE TRIGGER  check_marks  BEFORE UPDATE ON submissions 
FOR EACH ROW
BEGIN
IF NEW.marks <= 0 THEN
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'ERROR: 
    	     MARKS CANNOT BE NEGATIVE!';
END IF;
END; $$
delimiter ;;
