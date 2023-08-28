from databse_connection import DatabaseConnection


class Person : 
    def __init__(self, name, id, age, ): 
        self.name = name 
        self.age = age 
        self.id = id 
    
class Teacher(Person) : 
    db = DatabaseConnection() 
    db.createTables()
    def __init__(self, name,id, age, role, year_experinces):
        super().__init__(name, age, id)
        self.role = role 
        self.year_experinces = year_experinces
        Teacher.db.createTables()
    
    def save(self) : 
        
        Teacher.db.cursor.execute('INSERT INTO lectures (name, ID_number, age, role, year_exerince) values(?, ?, ?, ?, ?)', (self.name, self.id, self.age, self.role, self.year_experinces))
        Teacher.db.conn.commit() 

class EnginneringStudent(Person) :
      
    db = DatabaseConnection() 
     
    def __init__(self, name, id, age, course, outstanding, credit_taken, smester, cgps, ):
        super().__init__(name, id, age)
        self.course = course 
        self.outsanding = outstanding 
        self.credit = credit_taken 
        self.smester = smester 
        self.cgps = cgps 
        
    def save(self, role) : 
         
            EnginneringStudent.db.cursor.execute(f'INSERT INTO {role} (name,ID_number,age,course,outstanding,credit_taken,current_smester,CGPS) values(?, ?, ?, ?, ?, ?, ?, ?)', (self.name, self.id, self.age, self.course, self.outsanding, self.credit, self.smester, self.cgps))
            EnginneringStudent.db.conn.commit()
    
def avaCourses() : 
    engi_course = ['Mechanical Engineering', 'Material Engineering', 'Mechatromics Engineering', 'Electrical Engineering', 'Electronic Engineering', 'Computer Engineering', 'SoftWare Engineering']
    medical_course = ['Doctor', 'Dential', 'Nursing', 'Surgary'] 
    bus_course = ['Bussiness Administration', 'Markting', 'Accounting', 'International Bussiness']
    return engi_course, medical_course, bus_course