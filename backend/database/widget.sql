# Epic Title: Customizable Widgets

CREATE TABLE widgets (
    widget_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    widget_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);