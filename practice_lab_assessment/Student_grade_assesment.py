import json

students = [
{"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
{"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"}
]

id_counter=3
filename='students_record.json'
def menu():
    print('*'*50)
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
    print('*'*50)
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
        if name.strip()=='':
            print("Name cannot be empty")
            return
        course=input("Enter enrolled course: ")
        if course.strip()=='':
            print("Course cannot be empty")
        marks=float(input("Enter the marks obtained: "))
        if not 0<marks<100:
            print("Marks cannot be less than 0 or more than 100.")
            return
        
        students.append(dict(id=id_counter,name=name,course=course,marks=marks,grade=grade_generator(marks)))
        id_counter+=1
        print(students)
    except:
        print("Enter valid integer value.")

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
    try:
        with open(filename,mode='r') as file:
            students=json.load(file)
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
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
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