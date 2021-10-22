
CREATE TABLE CREDENTIALS (
  	userID 		VARCHAR2(128) UNIQUE,
  	email   VARCHAR2(128) UNIQUE,
    PRIMARY KEY (userID),
    FOREIGN Key(userID) references STUDENT (userID)
);

-- DROP TABLE STUDENT cascade constraints;

CREATE TABLE STUDENT (
  	userID 		VARCHAR2(128) PRIMARY KEY,
  	firstName   VARCHAR2(15),
  	lastName 	VARCHAR2(15),
    email       VARCHAR2(50),
    totalGPA    DECIMAL(3,2)
);

-- DROP TABLE SEMESTER cascade constraints;

create table SEMESTER (
    semesterID      NUMBER(64),
	semesterName 	VARCHAR2(20),
    gpa             DECIMAL(3,2),
    userID          VARCHAR2(128),
    FOREIGN KEY (userID) references STUDENT (userID)
    ON DELETE CASCADE,
    PRIMARY KEY (semesterID, userID)
);

-- DROP TABLE CURRENT_COURSE cascade constraints;

create table CURRENT_COURSE(
    courseID    NUMBER(64),
    courseName  VARCHAR2(20),
    creditHours NUMBER(12),
    isOnline    NUMBER(2),
    grade       DECIMAL(5, 2),
    semesterID    NUMBER(64),
    userID      VARCHAR2(128),
    foreign key (semesterID, userID) references SEMESTER (semesterID, userID)
    ON DELETE CASCADE,
    PRIMARY KEY (courseID, semesterID, userID)
);

-- DROP TABLE FUTURE_COURSE cascade constraints;

create table FUTURE_COURSE(
    courseID    NUMBER(64),
    courseName  VARCHAR2(20),
    creditHours NUMBER(12),
    plannedSemester VARCHAR2(20),
    userID      VARCHAR2(128),
    foreign key (userID) references STUDENT (userID)
    ON DELETE CASCADE,
    PRIMARY KEY (courseID, userID)
);

-- DROP TABLE CATEGORIES cascade constraints;

create table CATEGORIES(
    categoryID  NUMBER(64),
    categoryName  VARCHAR2(20),
    weight  DECIMAL(5, 2),
    categoryGrade   DECIMAL(5,2),
    courseID  NUMBER(64),
    semesterID    NUMBER(64),
    userID      VARCHAR2(128),
    foreign key (courseID, semesterID, userID) references CURRENT_COURSE (courseID, semesterID, userID)
    ON DELETE CASCADE,
    PRIMARY KEY (categoryID, courseID, semesterID, userID)
);

-- DROP TABLE ASSIGNMENTS cascade constraints;

create table ASSIGNMENTS(
    assignmentID    NUMBER(64),
    assignmentName  VARCHAR2(20),
    pointsReceived  DECIMAL(5, 2),
    totalPoints   DECIMAL(5,2),
    percentGrade   DECIMAL(5,2),
    dueDate     DATE,
    isDone  NUMBER(2),
    categoryID    NUMBER(64),
    courseID  NUMBER(64),
    semesterID    NUMBER(64),
    userID      VARCHAR2(128),
    foreign key (categoryID, courseID, semesterID, userID) references CATEGORIES (categoryID, courseID, semesterID, userID)
    ON DELETE CASCADE,
    PRIMARY KEY (assignmentID, categoryID, courseID, semesterID, userID)
);


-- Uncomment out the lines below to see how inserting into the table works and how to query results from the tables
-- INSERT INTO STUDENT VALUES ('abcdef', 'Eric', 'Deck', 'eadeck@ilstu.edu', 3.89);
-- INSERT INTO STUDENT VALUES ('jklmno', 'Chris', 'Moore', 'cmoor@ilstu.edu', 4.0);

-- INSERT INTO SEMESTER VALUES (5555, 'Fall-2019', 3.5, 'abcdef');
-- INSERT INTO SEMESTER VALUES (2222, 'Fall-2020', 3.6, 'abcdef');
-- INSERT INTO SEMESTER VALUES (5654, 'Fall-2019', 3.5, 'jklmno');
-- INSERT INTO SEMESTER VALUES (1233, 'Fall-2020', 3.78, 'jklmno');

-- INSERT INTO CURRENT_COURSE VALUES (1234, 'IT-279', 3, 1, 94.6, 5555, 'abcdef');
-- INSERT INTO CURRENT_COURSE VALUES (1522, 'IT-279', 3, 1, 97, 2222, 'abcdef');
-- INSERT INTO CURRENT_COURSE VALUES (1010, 'IT-378', 3, 1, 83.6, 5555, 'abcdef');
-- INSERT INTO CURRENT_COURSE VALUES (5678, 'IT-279', 3, 1, 94.6, 5654, 'jklmno');
-- INSERT INTO CURRENT_COURSE VALUES (1684, 'IT-378', 3, 1, 94.6, 1233, 'jklmno');

-- INSERT INTO FUTURE_COURSE VALUES (7777, 'IT-340', 4, 'Fall-2021', 'abcdef');
-- INSERT INTO FUTURE_COURSE VALUES (7878, 'IT-340', 4, 'Fall-2021', 'jklmno');

-- INSERT INTO CATEGORIES VALUES (666, 'Exams', 20, 92.3, 1234, 5555, 'abcdef');
-- INSERT INTO CATEGORIES VALUES (444, 'Homework', 20, 85.2, 1234, 5555, 'abcdef');
-- INSERT INTO CATEGORIES VALUES (999, 'Exams', 30, 95, 1522, 2222, 'abcdef');
-- INSERT INTO CATEGORIES VALUES (725, 'Exams', 20, 96.3, 5678, 5654, 'jklmno');

-- INSERT INTO CATEGORIES VALUES (3215, 'Exams', 20, 92.3, 1010, 5555, 'abcdef');
-- INSERT INTO CATEGORIES VALUES (8846, 'Exams', 20, 96.3, 1684, 1233, 'jklmno');

-- INSERT INTO ASSIGNMENTS VALUES (6978, 'Exam1', 54.5, 100, 54.5, '11-01-2019', 0, 666, 1234, 5555, 'abcdef'); 
-- INSERT INTO ASSIGNMENTS VALUES (9456, 'Exam1', 60, 100, 60, '11-01-2019', 0, 725, 5678, 5654, 'jklmno'); 
-- INSERT INTO ASSIGNMENTS VALUES (7898, 'Exam2', 62.5, 100, 62.5, '11-20-2019', 0, 666, 1234, 5555, 'abcdef'); 
-- INSERT INTO ASSIGNMENTS VALUES (8888, 'Homework1', 9, 10, 90, '11-30-2019', 1, 666, 1234, 5555, 'abcdef'); 

-- Below is some examples of how to get certain data. you only need to change a few things to make it work for most situations. I only did what I could think of now, can add more later.

----Get semesters for specific user
--select semesterName, gpa
--from SEMESTER
--where userID = 'abcdef';
--
----Get courses for all semesters for a specific user
--select SEMESTER.semesterName, SEMESTER.gpa, CURRENT_COURSE.courseName, CURRENT_COURSE.grade
--from SEMESTER join CURRENT_COURSE on SEMESTER.semesterID = CURRENT_COURSE.semesterID
--where SEMESTER.userID = 'abcdef'
--ORDER BY SEMESTER.semesterName desc;
--
----Get Categories for a specific course for a specific semester and specific user
--select categoryName, weight, categoryGrade
--from CATEGORIES join CURRENT_COURSE on CATEGORIES.courseID = CURRENT_COURSE.courseID
--join SEMESTER on SEMESTER.semesterID = CATEGORIES.semesterID
--where CURRENT_COURSE.courseName = 'IT-279' and CATEGORIES.userID = 'abcdef' and SEMESTER.semesterName = 'Fall-2020';
--
----Get all assignments for all categories for a specific course in a specific semester for a specific user
--select SEMESTER.semesterName, SEMESTER.gpa, CURRENT_COURSE.courseName, CURRENT_COURSE.grade, ASSIGNMENTS.assignmentName
--from ASSIGNMENTS join CURRENT_COURSE on ASSIGNMENTS.courseID = CURRENT_COURSE.courseID
--join SEMESTER on SEMESTER.semesterID = ASSIGNMENTS.semesterID
--where SEMESTER.semesterName = 'Fall-2019' and CURRENT_COURSE.courseName = 'IT-279' and ASSIGNMENTS.userID = 'abcdef';

--UPDATE CURRENT_COURSE
--SET courseName = 'IT-388'
--where courseID = 1234 and semesterID = 5555;
--
--select SEMESTER.semesterName, SEMESTER.gpa, CURRENT_COURSE.courseName, CURRENT_COURSE.grade, ASSIGNMENTS.assignmentName
--from ASSIGNMENTS join CURRENT_COURSE on ASSIGNMENTS.courseID = CURRENT_COURSE.courseID
--join SEMESTER on SEMESTER.semesterID = ASSIGNMENTS.semesterID
--where SEMESTER.semesterName = 'Fall-2019' and CURRENT_COURSE.courseID = 1234 and ASSIGNMENTS.userID = 'abcdef';
