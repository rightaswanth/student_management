DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS grads;
DROP TABLE IF EXISTS standards;
DROP TABLE IF EXISTS Parant;

CREATE TABLE student (
    id INTEGER  NOT NULL PRIMARY KEY ,
    adm_no TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
    class_id INTEGER,
    parant_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES standards(id),
    FOREIGN KEY (parant_id) REFERENCES Parant(id)
);

CREATE TABLE grads (
    id INTEGER NOT NULL PRIMARY KEY,
    grade TEXT,
    student_id INTEGER,
    class_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (class_id) REFERENCES standards(id)
);

CREATE TABLE standards (
    id INTEGER NOT NULL PRIMARY KEY,
    teacher_name TEXT,
    phone_number INTEGER UNIQUE,
    email TEXT UNIQUE
);

CREATE TABLE Parant (
    id INTEGER NOT NULL PRIMARY KEY,
    parant_name TEXT,
    phone_number INTEGER UNIQUE,
    email TEXT UNIQUE
);
