CREATE TABLE user_account (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    is_admin BOOLEAN,
    password TEXT,
    created TIMESTAMP
);

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    category_name TEXT UNIQUE,
    category_description TEXT,
    created TIMESTAMP,
    creator INTEGER,
    FOREIGN KEY (creator) REFERENCES user_account(id)
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    thread_subject TEXT,
    starting_message TEXT,
    created TIMESTAMP,
    category_id INTEGER,
    user_account_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (user_account_id) REFERENCES user_account (id)
);



CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    messages_subject TEXT,
    content TEXT,
    sent_at TIMESTAMP,
    thread_id INTEGER,
    category_id INTEGER,
    user_account_id INTEGER,
    FOREIGN KEY (thread_id) REFERENCES threads(id),
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (user_account_id) REFERENCES user_account(id)
);
