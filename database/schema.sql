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
    place VARCHAR(120) NOT NULL,
    creator_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (creator_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_creator (creator_id),
    INDEX idx_place (place)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabella Recensioni
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    race_id INT NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Percorso valutato
    route VARCHAR(120) NOT NULL,
    
    -- Valutazione del percorso
    rating_percorso_segnaletica INT NOT NULL DEFAULT 5,
    rating_percorso_fondo INT NOT NULL DEFAULT 5,
    rating_percorso_distanza INT NOT NULL DEFAULT 5,
    
    -- Valutazione ristori
    rating_ristori_numero INT NOT NULL DEFAULT 5,
    rating_ristori_varieta INT NOT NULL DEFAULT 5,
    rating_ristoro_abusivo INT NOT NULL DEFAULT 5,
    rating_ristoro_finale INT NOT NULL DEFAULT 5,
    
    -- Valutazione extra
    rating_extra_organizzazione INT NOT NULL DEFAULT 5,
    
    -- Note dell'utente
    content LONGTEXT NOT NULL,
    
    FOREIGN KEY (race_id) REFERENCES races(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_race (race_id),
    INDEX idx_user (user_id),
    INDEX idx_created (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Vincoli di integrità per i rating (1-5)
ALTER TABLE reviews ADD CONSTRAINT check_percorso_segnaletica CHECK (rating_percorso_segnaletica >= 1 AND rating_percorso_segnaletica <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_percorso_fondo CHECK (rating_percorso_fondo >= 1 AND rating_percorso_fondo <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_percorso_distanza CHECK (rating_percorso_distanza >= 1 AND rating_percorso_distanza <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_ristori_numero CHECK (rating_ristori_numero >= 1 AND rating_ristori_numero <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_ristori_varieta CHECK (rating_ristori_varieta >= 1 AND rating_ristori_varieta <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_ristoro_abusivo CHECK (rating_ristoro_abusivo >= 1 AND rating_ristoro_abusivo <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_ristoro_finale CHECK (rating_ristoro_finale >= 1 AND rating_ristoro_finale <= 5);
ALTER TABLE reviews ADD CONSTRAINT check_extra_organizzazione CHECK (rating_extra_organizzazione >= 1 AND rating_extra_organizzazione <= 5);

-- Query di verifica (eseguire dopo la creazione)
-- SELECT * FROM users;
-- SELECT * FROM races;
-- SELECT * FROM reviews;

-- Query di esempio per popolare il DB
-- INSERT INTO users (username) VALUES ('Mario');
-- INSERT INTO users (username) VALUES ('Enrico');
-- INSERT INTO races (name, place, creator_id) VALUES ('Maratona Cittadina', 'Milano', 1);
-- INSERT INTO reviews (race_id, user_id, route, rating_percorso_segnaletica, rating_percorso_fondo, rating_percorso_distanza, rating_ristori_numero, rating_ristori_varieta, rating_ristoro_abusivo, rating_ristoro_finale, rating_extra_organizzazione, content) 
-- VALUES (1, 2, 'Percorso A', 5, 5, 4, 5, 4, 5, 5, 5, 'Bellissima esperienza!');
