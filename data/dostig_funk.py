import sqlite3

def dostig():
    con = sqlite3.connect("db/characters_and_achievements.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT achievement FROM achievements
    WHERE completed = 1""").fetchall()
    result2 = []
    for i in result:
        result2.append(i[0])
    return result2
