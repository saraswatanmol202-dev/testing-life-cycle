# Epic Title: Maintain Separate Database

CREATE TABLE local_data (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    data_type VARCHAR(50),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);