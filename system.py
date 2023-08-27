
import student_managment_system_model as manSystem
import sqlite3    # import database. 

def CollectInfo(engineering_courses) :
    print('************************************')
    print('Welcome to Student Managment System.')
    print('************************************\n')
    
    
    try : 
        student_db = sqlite3.connect('student.db') # create and connect to database. 
        cr = student_db.cursor()
        # create a Engineering table in the database .
        cr.execute('CREATE TABLE if not exists `Enginnering` (name text, age integer, passport text, ID_Card text, GPA float, CGPA float, smester integer)')
        cr.execute('CREATE TABLE if not exists `Medical` (name text, age integer, passport text, ID_Card text, GPA float, CGPA float, smester integer)')
        cr.execute('CREATE TABLE if not exists `Bussiness` (name text, age integer, passport text, ID_Card text, GPA float, CGPA float, smester integer)')
        
        
        while True: 
             
            title = input('Do you want to (add/delete/show/update) student info ? ').strip().lower() 
            if title == "" : 
                print('please enter a valid option (add/delete/show/update) or \'q\' to quite the system.') 
            elif title == 'q' : 
                break 
            elif title == 'add' : 
                course = input('Student Course ? ').strip().title()
                
                if course not in engineering_courses : 
                    print('\nYou need to select one of the avilable course')
                    print('*********************************************')
                    print(*engineering_courses, sep='\n')
                    print('*********************************************\n')
                    
                else :
                    if 'Engineering' in course: 
                        engineering_student =  manSystem.EngineeringStudent() 
                        cr.execute('INSERT INTO Enginnering (name text, age integer, passport text, ID_Card text, GPA float, CGPA float, smester integer)')
            # print( 'well')
    except : 
        print('enter a valid input' )
    finally : 
        student_db.close()
    
engineering_courses = ['Material Engineering', 'Mechatronics Engineering', 'Mechanical Engineering', 'Electrical Engineering', 'Electronics Engineering', 'Computer Engineering']
CollectInfo(engineering_courses)