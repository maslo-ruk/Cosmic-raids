import sqlite3

def persons():
    con = sqlite3.connect("../db/characters_and_achievements.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT character FROM characters
    WHERE avaibility = 1""").fetchall()
    return result

print(persons())
