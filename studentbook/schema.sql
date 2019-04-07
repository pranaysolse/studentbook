DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS comitteehead;
DROP TABLE IF EXISTS teacher;
DROP TABLE IF EXISTS admin;
CREATE TABLE student (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	names TEXT NOT null,
	email TEXT ,
	mobile TEXT,
	asddress TEXT ,
	class TEXT NOT NULL,
	branch TEXT NOT NULL ,
	divison TEXT NOT NULL
);

CREATE TABLE comitteehead (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT ,
	asddress TEXT ,
	names TEXT,
	position TEXT ,
	comittee_name TEXT ,
	mobile TEXT ,
	email TEXT ,
	class TEXT ,
	branch TEXT 
);

CREATE TABLE teacher (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	names TEXT ,
	asddress TEXT ,
	qualification TEXT ,
	branch TEXT,
	password TEXT NOT NULL
);

CREATE TABLE admin (
	id INTEGER PRIMARY KEY,
	adminname TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);

INSERT INTO admin VALUES (1,'pranay','pranay');
INSERT INTO admin VALUES (2,'mayank','mayank');
INSERT INTO admin VALUES (3,'aman','aman');