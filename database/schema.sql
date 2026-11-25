-- A schema to create tables, relationships, and constraints

CREATE TABLE IF NOT EXISTS public_documents (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    content TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS private_documents (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    owner_id TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    UNIQUE (owner_id, title)
);