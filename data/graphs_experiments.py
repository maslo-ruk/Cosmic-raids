import random
import sqlite3

con = sqlite3.connect("../db/characters_and_achievements.sqlite")
cur = con.cursor()
result = cur.execute("""SELECT achievement FROM achievements
WHERE completed = 0""").fetchall()
result2 = []
for i in result:
    result2.append(i[0])
print(result2)
cur.close()
con.commit()