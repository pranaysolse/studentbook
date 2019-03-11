DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS comitteehead;
DROP TABLE IF EXISTS teacher;
CREATE TABLE student (
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE NOT NULL,
	password TEXT ,
	address TEXT ,
	class TEXT ,
	branch TEXT ,
	year TEXT 
);

CREATE TABLE comitteehead (
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	address TEXT NOT NULL,
	class TEXT NOT NULL,
	branch TEXT NOT NULL,
	year TEXT NOT NULL,
	role TEXT NOT NULL
);

CREATE TABLE teacher (
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE NOT NULL,
	address TEXT NOT NULL,
	designation TEXT NOT NULL,
	qualification TEXT NOT NULL,
	subject TEXT NOT NULL
)

