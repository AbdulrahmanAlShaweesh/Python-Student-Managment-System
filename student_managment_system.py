

class Students : 
    
    def __init__(self, studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA) :
        self.studentName = studentName 
        self.studentAge = studentAge 
        self.studentPassportNumber = studentPassportNumber 
        self.studentIDNumber = studentIdNumber 
        self.studentGPA = studetnGPA 
        self.studentCGPA = studentCGPA 
    
    # return name and age of the student.
    def studentInfo(self) : 
        return self.studentName, self.studentAge
    
    # student ID number
    def IDCard(self) :
        return self.studentIDNumber 
    
    # student's passport number. 
    def studentPassport(self) :
        return self.studentPassportNumber
    
    # student GPA. 
    def GPA(self) :
        return self.studentGPA 
    
    # student's CGPA. 
    def CGPA(self) :
        return self.studentCGPA
 
student1 = Students('Mohammed', 23, 23342123, 'BE12234C', 3.5, 3.1)

print(student1.studentInfo())
    