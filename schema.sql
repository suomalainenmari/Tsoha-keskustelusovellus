CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    subject_name TEXT UNIQUE
);


CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
    subject_id INTEGER REFERENCES subjects

);


