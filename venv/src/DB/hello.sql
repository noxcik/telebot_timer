--
-- ���� ������������ � ������� SQLiteStudio v3.2.1 � �� ��� 26 23:47:55 2020
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: user
CREATE TABLE user (ID INTEGER PRIMARY KEY NOT NULL UNIQUE, stat TEXT, ord TEXT, random_code INTEGER, time TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
