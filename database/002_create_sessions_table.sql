# Epic Title: Create Secure User Sessions

CREATE TABLE IF NOT EXISTS sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    last_activity DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);