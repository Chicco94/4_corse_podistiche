-- SQL Script per creare le tabelle del progetto Corse Podistiche
-- Database: Chicco94$corse_podistiche
-- Eseguire questo script su MySQL PythonAnywhere

-- Tabella Utenti
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabella Corse Podistiche
CREATE TABLE IF NOT EXISTS races (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    date DATETIME NOT NULL,
    creator_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (creator_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_creator (creator_id),
    INDEX idx_date (date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabella Recensioni
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content LONGTEXT NOT NULL,
    rating INT DEFAULT 5,
    race_id INT NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (race_id) REFERENCES races(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_race (race_id),
    INDEX idx_user (user_id),
    INDEX idx_created (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Vincoli di integrità aggiuntivi
ALTER TABLE reviews ADD CONSTRAINT check_rating CHECK (rating >= 1 AND rating <= 5);

-- Query di verifica (eseguire dopo la creazione)
-- SELECT * FROM users;
-- SELECT * FROM races;
-- SELECT * FROM reviews;

-- Query di esempio per popolare il DB
-- INSERT INTO users (username) VALUES ('Mario');
-- INSERT INTO users (username) VALUES ('Enrico');
-- INSERT INTO races (name, date, creator_id) VALUES ('Maratona Cittadina', '2026-05-15 09:00:00', 1);
-- INSERT INTO reviews (content, rating, race_id, user_id) VALUES ('Bellissima esperienza!', 5, 1, 2);
