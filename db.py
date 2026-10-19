import sqlite3



class database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts(id integer primary key,fname TEXT ,lname TEXT, email TEXT, password TEXT)
        """)
        self.con.commit()
    def add_users(self,fname,lname,email,password):
        self.cur.execute("""
        INSERT INTO contacts(fname,lname,email,password)
        VALUES(?,?,?,?) 
        """,(fname,lname,email,password))
        self.con.commit()
    def find(self,email,password):
        self.cur.execute('SELECT * FROM contacts WHERE email = ? and password = ? ',(email,password))
        return self.cur.fetchall()
        
