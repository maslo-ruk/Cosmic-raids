--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Сб янв 25 23:18:14 2025
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Dostigenia
CREATE TABLE IF NOT EXISTS Dostigenia (
    Достижение TEXT,
    Получено   INT
)
STRICT;

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'охотник_I',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'охотник_II',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'охотник_III',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'динь_динь',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           '"не беси"',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           '":3"',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'герой без щита',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'вся команда',
                           0
                       );

INSERT INTO Dostigenia (
                           Достижение,
                           Получено
                       )
                       VALUES (
                           'каждый день одно и тоже',
                           0
                       );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
