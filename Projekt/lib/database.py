import sqlite3

database_path = "database.db"


def create():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS stats (
                        user TEXT,
                        correct INTEGER,
                        incorrect INTEGER,
                        firsttry TEXT,
                        score REAL,
                        mode INTEGER
                    )''')
    conn.commit()
    conn.close()


def write(data):
    if data["multiplechoice"] == True:
        data_tuple = (data["user"], data["correct"], data["incorrect"], data["firsttry"], data["score"], 1)
    else:
        data_tuple = (data["user"], data["correct"], data["incorrect"], data["firsttry"], data["score"], 0)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    print(data)
    print(data_tuple)
    cursor.executemany('INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?)', [data_tuple])
    conn.commit()
    conn.close()


def read():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stats")
    data = cursor.fetchall()

    def convert(data_tuple):
        return {
            "user": data_tuple[0],
            "correct": data_tuple[1],
            "incorrect": data_tuple[2],
            "firsttry": data_tuple[3],
            "score": data_tuple[4],
            "multiplechoice": data_tuple[5] == 1
        }

    conn.close()
    return map(convert, data)
