

class Students : 
    
    def __init__(self, studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester) :
        self.studentName = studentName 
        self.studentAge = studentAge 
        self.studentPassportNumber = studentPassportNumber 
        self.studentIDNumber = studentIdNumber 
        self.studentGPA = studetnGPA 
        self.studentCGPA = studentCGPA 
        self.currentSemester = currentSemester
    
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
    
    # get the student's current semester.
    def semester(self) :
        return self.currentSemester 

class EngineeringStudent(Students) :
    
    totalStudents = 0
    def __init__(self, studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester, course, creditTaken, tutionFee):
        super().__init__(studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester)
        self.course = course 
        self.creditTaken = creditTaken
        self.tutionFee = tutionFee
        EngineeringStudent.totalStudents += 1
    
    # total credit taken by student
    def creditTakenByStudent(self) :
        return self.creditTaken 
    
    # course taken by student
    def studentField(self) : 
        return self.course 
    
    # total engineering students. 
    def totalNumberOfStudents(self) :
        return EngineeringStudent.totalStudents
    
    # student yearly fee
    def yearlyFee(self) :
        return self.tutionFee
    
# medical student class. 
class MedicalStudent(Students) : 
    
    totalStudent = 0
    def __init__(self, studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester, creditTaken, courseTaken, tuitionFee):
        super().__init__(studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester)
        self.creditTaken = creditTaken 
        self.courseTaken = courseTaken 
        self.tuitionFee = tuitionFee 
        MedicalStudent.totalStudent += 1 
    
    # total student in medical class. 
    def totalNumberOfStudents(self) : 
        return MedicalStudent.totalNumberOfStudents
    
    # yearly fee
    def yearlyFee(self): 
        return self.tuitionFee 
    
    # course taken 
    def courseTakenByStudent(self) :
        return self.courseTaken 
    
    # credit taken
    def totalCreditTaken(self) :
        return self.creditTaken
# bussiness student
class Bussiness(Students) :
    totalNumberOfStudents = 0
    def __init__(self, studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester, creditTaken, courseTaken, tutionFee):
        super().__init__(studentName, studentAge, studentPassportNumber, studentIdNumber, studetnGPA, studentCGPA, currentSemester)
        self.creditTaken = creditTaken
        self.courseTaken = courseTaken
        self.tutionFee = tutionFee
        Bussiness.totalNumberOfStudents
        
    # total credit taken by student
    def creditTakenByStudent(self) :
        return self.creditTaken 
    
    # course taken by student
    def studentField(self) : 
        return self.course 
    
    # total engineering students. 
    def totalNumberStudents(self) :
        return EngineeringStudent.totalNumberOfStudents
    
    # student yearly fee
    def yearlyFee(self) :
        return self.tutionFee
    
