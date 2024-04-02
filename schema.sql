DROP TABLE IF EXISTS Patches CASCADE;
DROP TABLE IF EXISTS Images CASCADE;
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS UsersToPatches CASCADE;


CREATE TABLE Patches (
    id SERIAL PRIMARY KEY, 
    name TEXT
);

CREATE TABLE Images (
    id SERIAL PRIMARY KEY,
    patch_id INTEGER REFERENCES Patches(id),
    data BYTEA
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE UsersToPatches (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    patch_id INTEGER REFERENCES Patches(id),
    sent_at TIMESTAMP 
);