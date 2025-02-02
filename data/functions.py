import pygame, sqlite3


def generate(size):
    pass

def get_character():
    con = sqlite3.connect('db/characters_and_achievements.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM character
                WHERE year = 2010""").fetchall()
