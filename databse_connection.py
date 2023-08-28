import sqlite3


class DatabaseConnection : 
    
    def __init__(self,) :
        self.conn = sqlite3.connect('school.db')
        self.cursor = self.conn.cursor()
    
    def createTables(self) :
        try :  
            # create a table for lectures in the database. 
            self.cursor.execute('CREATE TABLE IF NOT EXISTS lectures (name TEXT, ID_number TEXT, age INtEGER , role TEXT, year_exerince FLOAT)')
            # create a table for engineering students in the database. 
            self.cursor.execute('CREATE TABLE IF NOT EXISTS engineering (name TEXT,ID_number TEXT, age INtEGER, course TEXT, outstanding FLOAT, credit_taken INTEGER, current_smester INEGER, CGPS FLOAT)')
            # create a table for medical students. 
            self.cursor.execute('CREATE TABLE IF NOT EXISTS medical (name TEXT,ID_number TEXT, age INtEGER, course TEXT, outstanding FLOAT, credit_taken INTEGER, current_smester INEGER, CGPS FLOAT)')
            # create a table for bussiness students. 
            self.cursor.execute('CREATE TABLE IF NOT EXISTS bussiness (name TEXT,ID_number TEXT, age INtEGER, course TEXT, outstanding FLOAT, credit_taken INTEGER, current_smester INEGER, CGPS FLOAT)')
            self.conn.commit()
        except : 
            print('error connection to database') 
         
        