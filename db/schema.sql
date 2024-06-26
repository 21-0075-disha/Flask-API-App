CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    transcription TEXT NOT NULL,
    tags VARCHAR(255)
);
