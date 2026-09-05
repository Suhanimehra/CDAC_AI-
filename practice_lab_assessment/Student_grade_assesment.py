import json

students = [
{"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
{"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"},
]

id_counter=len(students)
filename='students_record.json'
def menu():
    print('*'*100)
    menu_text=''' 
    Student Grade & Assessment Module
    [1] Enroll Student 
    [2] Cohort Directory 
    [3] Query Records 
    [4] Revise Evaluation 
    [5] Purge Record 
    [6] Save to JSON 
    [7] Load from JSON 
    [8] Terminate
    '''
    print(menu_text)
    print('*'*100)
def grade_generator(marks):
    if marks>=85:
        grade='A'
        return grade

    elif marks>=70:
        grade='B'
        return grade

    elif marks>=50:
        grade='C'
        return grade

    else:
        grade='F(Fail)'
        return grade


def enroll_student():
    global id_counter
    try:
        name=input("Enter your name: ")
        if name.strip().lower()=='':
            print("Name cannot be empty")
            return
        course=input("Enter enrolled course: ")
        if course.strip().lower()=='':
            print("Course cannot be empty")
            return
        marks=float(input("Enter the marks obtained: "))
        if not 0<=marks<=100:
            print("Marks cannot be less than 0 or more than 100.")
            return
        
        students.append(dict(id=id_counter+1,name=name,course=course,marks=marks,grade=grade_generator(marks)))
        id_counter+=1
    except:
        print("Enter valid integer value.")

def cohort_directory():

    if len(students)==0:
        print("No Records Found")
    elif len(students)==1:
        print_one_record(students[0])
    else:
        print_many_record(students)

def print_one_record(s): #here s will represent students[0]

    id,name,course,marks,grade=s.values()

    print("------Student Details-------")

    print(f'ID:        {id}')
    print(f'Name:      {name}')
    print(f'Course:    {course}')
    print(f'Marks:     {marks:.2f}')
    print(f'Grade:     {grade}')

    print('-'*100)

def print_many_record(students):

    print("------Student Details-------")
    print(f"{'ID':<5}{'Name':<20}{'Course':<20}{'Marks':>10}{'Grade':>10}")

    print('-'*65)

    for s in students:
        id,name,course,marks,grade=s.values()

        print(f'{id:<5}{name:<20}{course:<20}{marks:>10.2f}{grade:>10}')

    print('-'*65)
    
def search_records():

    try:
        print(" Enter 1 to search by Student ID.\n Enter 2 to search by Student Name. \n Enter 3 to search by Course Name.")
        search_choice=int(input())

        if search_choice==1:
    
            search_by_student_id()

        elif search_choice==2:
            search_by_name()
        elif search_choice==3:
            search_by_course_name()
        else:
            print("Enter a Valid Input Choice.")
    except:
      print("Value Error")

def search_by_student_id():
    try:
        student_id=int(input("Enter the Student ID you want to search."))
        found=False

        for student in students:
            if student['id'] == student_id:
                print_one_record(student)
                print("Student Found")
                found=True
                break

        if not found:
            print(f"Student Not Found. ID: {student_id}")
    except:
        print("Enter a Valid Number")

def search_by_name():
    try:
        student_name=input("Enter the Student Name you want to search.")
        # res = [s for s in students if s["name"].strip().lower() == student_name.lower()]
        res = []
        for s in students:
            if s["name"].strip().lower()== student_name:
                res.append(dict(s))
        
        if len(res) == 0:
            print(f"Student Not Found. Name: {student_name}")
        elif len(res) == 1:
            print_one_record(res[0])
        else:
            print_many_record(res)
    except:
        print("Enter a Valid Name")

def search_by_course_name():
    try:
        course_name=input("Enter the Course Name you want to search.")
        # res = [s for s in students if s["name"].strip().lower() == student_name.lower()]
        res = []
        for s in students:
            if s["course"].strip().lower() == course_name:
                res.append(dict(s))
        
        if len(res) == 0:
            print(f"Student Not Found for Course Name: {course_name}")
        elif len(res) == 1:
            print_one_record(res[0])
        else:
            print_many_record(res)
    except:
        print("Enter a Valid Course Name")

def update_record():
    
    try:
        update_choice=int(input("Enter the student ID to update."))
        
        result=[s for s in students if s['id']==update_choice]
        
        if not result:
            print(f"No Student Found For {update_choice}")
        
        else:
            name=input("Enter the update name: ")
            if name.strip().lower()=='':
                print("Invalid Input Name cannot be empty.")
                return
            
            course=input("Enter enrolled course: ")
            if course.strip().lower()=='':
                print("Course cannot be empty")
                return
            
            marks=float(input("Enter the marks obtained: "))
            if not 0<marks<100:
                print("Marks cannot be less than 0 or more than 100.")
                return
            grade=grade_generator(marks) 
            
            result[0]['name']=name
            result[0]['course']=course
            result[0]['marks']=marks
            result[0]['grade']=grade

            print_one_record(result[0])

    except:
        print("Enter a Valid Number")
        
def delete_record():
    
    try:
    
        delete_choice=int(input("Enter the Student ID you want to delete: "))
        
        result=[s for s in students if s['id']==delete_choice]
                
        if not result:
            print(f"No Student Found For {delete_choice}")
            
        else:
            choice=input("Are You Sure You Want To Delete[y/n]: ")
        
            if choice.lower()=='y':
                students.remove(result[0])
                print("record deleted successfully")
                print_many_record(students)
            else:
                print("No Record deleted")
           
    except:
        print("Enter Right Value")   
    

def save_to_json():
    global filename
    try:
        with open(filename,mode='w') as file:
            json.dump(students,file)
        print("File saved successfully")

    except:
        print("File not Saved")

def load_from_json():
    global filename
    global students
    global id_counter
    try:
        with open(filename,mode='r') as file:
            students=json.load(file)

            id_counter=len(students)

        print("File Loaded successfully")

        
    except:
        print("File not loaded")

def main():
    while True:
        menu()

        user_choice=int(input("Enter your choice: "))

        match user_choice:
            case 1:
                enroll_student()
            case 2:
                cohort_directory()
            case 3:
                search_records()
            case 4:
                update_record()
            case 5:
                delete_record()
            case 6:
                save_to_json()
            case 7:
                load_from_json()
            case 8:
                break
            case _:
                print("Enter a valid input: ")
    

if __name__=='__main__':
    main()