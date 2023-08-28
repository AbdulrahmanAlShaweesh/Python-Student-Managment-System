from manag_system_class import EnginneringStudent, Teacher, avaCourses

###########################################################################
def headingSystem() :
    print('1. to add student') 
    print('2. to add Teacher')
    print('3. to update student') 
    print('4. to update teacher') 
    print('5. to delete student')
    print('6. to delete teacher') 
    print('7. to exit the system')

###########################################################################
def studentsInfo( ) : 
     
    name = input('Enter Student\'s Name ? ').strip().title()
    id   = input('Enter Student ID ? ').strip().upper() 
    age = int(input('Enter Student\'s Age ? ').strip()) 
    course = input('Enter Students Course ? ').strip().capitalize() 
    outstanding = float(input('Enter the outstanding ? ').strip()) 
    credit = int(input('Enter the total credit student took ? ').strip()) 
    smester = int(input('Enter the Students\'s current smester ? ').strip())
    cgpa = float(input('Enter the Student\'s CGPA ? ').strip())
    return name, id, age, course, outstanding, credit, smester, cgpa

###########################################################################
def lectureInfo() : 
    name = input('Enter Student\'s Name ? ').strip().title()
    id   = input('Enter Student ID ? ').strip().upper() 
    age = int(input('Enter Student\'s Age ? ').strip())
    role = input('Enter the role of the lecture ? ').strip().title() 
    experinces = float(input('Enter the years of experinces ? ').strip())
    
    return name, id, age, role, experinces

###########################################################################
def main() : 
    headingSystem()
    while True : 
        
        try : 
            engineering, medical, bussiness =  avaCourses()
            choise = input('Enter your choice? ').strip() 
            
            if choise == '1' : 
                name, id, age, course, outstanding, credit, smester, cgpa = studentsInfo()
                
                if  course in engineering:
                    eng = EnginneringStudent(name, id, age, course, outstanding, credit, smester, cgpa)
                    eng.save('engineering')
                elif course in medical :
                    eng = EnginneringStudent(name, id, age, course, outstanding, credit, smester, cgpa)
                    eng.save('medical')
                elif course in bussiness : 
                    eng = EnginneringStudent(name, id, age, course, outstanding, credit, smester, cgpa)
                    eng.save('bussiness')
                else :
                    print('Enter a valid course')
            elif choise == '2' : 
                name, id, age, role, experinces = lectureInfo()
                teacher = Teacher(name, id, age, role, experinces)
                teacher.save()
            elif choise == 'q' : 
                break 
            else :
                print('Please enter a valid option from the menu.')
        except : 
            print('something went wront.')
        
            
main()