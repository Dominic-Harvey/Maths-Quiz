import sqlite3

def database(name, final_score):
    conn = sqlite3.connect('Maths Quiz/userscores.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS scores(name TEXT, score REAL)')

    def enter_score(name, final_score):
            c.execute("INSERT INTO scores (name, score) VALUES (?, ?)",(name, final_score))
            conn.commit()
    
    enter_score(name, final_score)
    conn.close()

'''
def read_from_db():
        c.execute("SELECT * FROM scores")
        for row in c.fetchall():
            print(row[1])
'''
