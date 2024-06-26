DROP TABLE IF EXISTS words CASCADE;

DROP TABLE IF EXISTS users_words CASCADE;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(50),
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (email_address, username, password) 
VALUES 
('Joe1234@gmail.com', 'Joe1234', 'password1'),
('Anna1234@gmail.com', 'Anna1234', 'password2'),
('Joseph5678@hotmail.com', 'Joseph5678', 'password3'),
('Sophie1234@outlook.com', 'Sophie1234', 'password4');

CREATE TABLE IF NOT EXISTS words (
    id SERIAL PRIMARY KEY,
    source_language VARCHAR(50),
    target_language VARCHAR(50),
    word_source_language VARCHAR(50),
    word_target_language VARCHAR(50),
    time_stamp VARCHAR(50),
    user_id INT,
    constraint fk_user foreign key(user_id)
    references users(id) 
    on delete cascade
);

INSERT INTO words (source_language, target_language, word_source_language, word_target_language, time_stamp, user_id) 
VALUES 
('English', 'French', 'Apple', 'Pomme', '06/26/24 15:38:38', '1'),
('English', 'Italian', 'Apple', 'Mela', '06/26/24 15:38:38', '2'),
('French', 'English', 'Pomme', 'Apple', '06/26/24 15:38:38', '1'),
('French', 'Italian', 'Pomme', 'Mela', '06/26/24 15:38:38', '2');