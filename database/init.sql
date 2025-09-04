CREATE DATABASE myapp;
=====================================================================================================================
USE myapp;
=====================================================================================================================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
=====================================================================================================================
INSERT INTO users (name, email) VALUES
('Ahmed Abuzaid', 'ahmed@example.com'),
('DevOps User', 'devops@example.com');
=====================================================================================================================
CREATE USER 'ahmed'@'%' IDENTIFIED BY 'ahmed';
GRANT ALL PRIVILEGES ON myapp.* TO 'ahmed'@'%';
FLUSH PRIVILEGES;
======================================================================================================================
Allow traffic from the backend VM to DB Add a rule in UFW 
sudo ufw allow from <backend-vm-ip> to any port 3306
sudo ufw enable
sudo ufw status
