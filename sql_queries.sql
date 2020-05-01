-- +++++++++++++++++++++++++++++++++++++++++++
-- SQLite
-- +++++++++++++++++++++++++++++++++++++++++++
CREATE TABLE `product` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`price`	REAL
);
CREATE TABLE sqlite_sequence(name,seq);

CREATE TABLE `user` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	    DATE,
    `name`	    CHAR(50),
    `lastname`	CHAR(50),
    `nick`	    CHAR(50),
    `password`  CHAR(50),
    `birthday`  DATE,
    `address`	CHAR(50),    
    `country`	CHAR(50),
    `phone` 	CHAR(50),  
    `email`	    CHAR(50),
    `company`	CHAR(50)
);
DROP TABLE user;
ALTER TABLE user ADD COLUMN date datetime;
-- +++++++++++++++++++++++++++++++++++++++++++

SELECT datetime('now','localtime');

INSERT INTO user
VALUES( 
    NULL, datetime('now','localtime'), 
    'Pedro', 'Perez', 'Pepe', 
    '1234', '1970-01-06', 'Corrientes 432',
    'Arg', '00541188887777', 'pepe@perez.net',
    'IBM'
    );

-- +++++++++++++++++++++++++++++++++++++++++++

SELECT * FROM sqlite_master WHERE type = "table";

SELECT * FROM product;

SELECT * FROM user;

SELECT * FROM sqlite_sequence;