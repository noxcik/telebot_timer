--
-- Файл сгенерирован с помощью SQLiteStudio v3.2.1 в Пт июн 26 23:47:55 2020
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: user
CREATE TABLE user (ID INTEGER PRIMARY KEY NOT NULL UNIQUE, stat TEXT, ord TEXT, random_code INTEGER, time TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
