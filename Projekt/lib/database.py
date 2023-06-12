import sqlite3

database_path = "database.db"


def create():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS score (
                        user TEXT,
                        correct INTEGER,
                        incorrect INTEGER,
                        firsttry TEXT,
                        score REAL,
                        mode INTEGER
                    )''')

    conn.commit()


def write(data):
    if data["multiplechoice"] == True:
        data_tuple = (data["user"], data["correct"], data["incorrect"], data["firsttry"], data["score"], 1)
    else:
        data_tuple = (data["user"], data["correct"], data["incorrect"], data["firsttry"], data["score"], 0)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO trueFalse VALUES (?, ?, ?, ?, ?, ?)', data_tuple)
    conn.commit()


def read():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trueFalse")
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

    return map(convert, data)
