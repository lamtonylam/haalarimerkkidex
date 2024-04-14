DROP TABLE IF EXISTS Patches CASCADE;
DROP TABLE IF EXISTS Images CASCADE;
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS UsersToPatches CASCADE;
DROP TABLE IF EXISTS Comments CASCADE;

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE Patches (
    id SERIAL PRIMARY KEY, 
    name TEXT UNIQUE,
    created_by_user SERIAL REFERENCES Users(id)
);

CREATE TABLE Images (
    id SERIAL PRIMARY KEY,
    patch_id INTEGER REFERENCES Patches(id) ON DELETE CASCADE,
    data BYTEA
);

CREATE TABLE UsersToPatches (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    patch_id INTEGER REFERENCES Patches(id) ON DELETE CASCADE,
    sent_at TIMESTAMP 
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    patch_id INTEGER REFERENCES Patches(id) ON DELETE CASCADE,
    comment TEXT,
    sent_at TIMESTAMP
);