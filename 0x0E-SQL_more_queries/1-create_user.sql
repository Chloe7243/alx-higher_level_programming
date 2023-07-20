-- creates the MySQL server user user_0d_1.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT, INSERT, ... , DROP ROLE ON *.* TO `user_0d_1`@`localhost`;
GRANT APPLICATION_PASSWORD_ADMIN, ... , XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`;
