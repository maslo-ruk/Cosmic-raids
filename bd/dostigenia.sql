--
-- ���� ������������ � ������� SQLiteStudio v3.4.4 � �� ��� 25 23:18:14 2025
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: Dostigenia
CREATE TABLE IF NOT EXISTS Dostigenia (
    ���������� TEXT,
    ��������   INT
)
STRICT;

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '�������_I',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '�������_II',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '�������_III',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '����_����',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '"�� ����"',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '":3"',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '����� ��� ����',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '��� �������',
                           0
                       );

INSERT INTO Dostigenia (
                           ����������,
                           ��������
                       )
                       VALUES (
                           '������ ���� ���� � ����',
                           0
                       );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
