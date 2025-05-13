CREATE DATABASE IF NOT EXISTS calender_db;
USE calender_db;

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(50) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `is_administrator` TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`)
);

INSERT INTO `users` (`email`, `password`, `is_administrator`) VALUES
('admin@example.com', 'admin', 1),
('student@example.com', 'student', 0);