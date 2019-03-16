DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS comitteehead;
DROP TABLE IF EXISTS teacher;

CREATE TABLE student (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT ,
	address TEXT ,
	class TEXT ,
	branch TEXT ,
	year TEXT 
);

CREATE TABLE comitteehead (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	password TEXT ,
	address TEXT ,
	class TEXT ,
	branch TEXT ,
	year TEXT ,
	role TEXT 
);

CREATE TABLE teacher (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT UNIQUE NOT NULL,
	address TEXT ,
	designation TEXT ,
	qualification TEXT ,
	subject TEXT ,
	password TEXT NOT NULL
);

CREATE TABLE admin (
	id INTEGER PRIMARY KEY,
	adminname TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);

INSERT INTO admin VALUES (1,'pranay','pranay');
INSERT INTO admin VALUES (2,'mayank','mayank');