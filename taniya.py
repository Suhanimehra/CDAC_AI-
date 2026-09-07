import json
students = [ 
    {"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
{"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"}

] 

id_counter = len(students)

#-------------------------------------------------------------------------------------

def menu():
    menu_text = '''1. Add Product 
2. View All students 
3. Search students
4. Update Product 
5. Delete Product 
6.save to json
7.load to json
8. Exit '''

    print('**** students Management System ****')
    print(menu_text)
    try:
        choice = int(input('Enter your choice: '))
    except:
        choice = -1

    return choice

#-------------------------------------------------------------------------------------
def calgrade(number):
    marks = number
    if marks >= 85.0:
        return "A"
    if marks >= 70.0   and marks < 85.0:
        return "B"
    if marks >= 50.0 and marks <70.0:
        return "C"
    if marks < 50.0:
        return "F"
    
    

# ------------------------------------------------
def add_students():
    global id_counter
    try:
        print('**** Add new product details ****')
        name = input('Name: ').strip()
        if name == '':
            print('Name cannot be empty!')
            return
        
        course = input('Course: ').strip()
        if course == '':
            print('Category cannot be empty!')
            return
        
        number = float(input('number: '))
        if number <= 0 or number > 100:
            print('no must be in between 0 and 100')
            return

        grade = calgrade(number)
   
        students.append(dict(id=id_counter+1, name=name, course=course, number=number, grade=grade))
        id_counter += 1

    except ValueError:
        print('Please retry with a numerical value')

#-------------------------------------------------------------------------------------

def print_one_product(p):
    pid, name, course, number, grade = p.values()
    print('----Student Details ----')
    print(f'ID          : {pid}')
    print(f'Name        : {name}')
    print(f'Course      : {course}')
    print(f'number      : {number}')
    print(f'grade       : {grade}')
    print('-'*50)    

#-------------------------------------------------------------------------------------

def print_many_students(product_list):
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Course':<20}{'number':<10}{'grade':<5}')
    print('-'*60)
    for p in product_list:
        pid, name, course, number, grade= p.values()
        print(f"{pid:^5}{name:<20}{course:<20}{number:<10.2f}{grade:<5}")
    print('-'*60)

#-------------------------------------------------------------------------------------

def view_students():
    if len(students) == 0:
        print("No students in the inventory. Please add first.")
    elif len(students) == 1:
        print_one_product(students[0])
    else:
        print_many_students(students)

#-------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------
def search_student(id):
    result = [p for p in students if p['id']==id]
    if result is None:
        print(f'No product found for name "{id}"')
        return
    if len(result) == 1:
        print_one_product(result[0])
        return result
    else:
        print_many_students(result)
#-------------------------------------------------------------------------------------
def delete_student():
    try:
        pid = int(input('Enter id of the product to delete: '))
        p = search_student(pid)
        if p is None:
            return

        ans = input('Are you sure to delete this product? (y/n): ').lower()

        if ans == 'y':
            students.remove(p)
            print('Product deleted successfully!')
        
    except:
        print('Invalid type of value for product id. Try again with an integer.')
#-------------------------------------------------------------------------------------
def update_student():
    try:
        pid=int(input("please the id you want to updata :"))
        p=search_student(pid)
        if p is None:
            print("item is not present")
        else:
            print('**** Add new student details ****')
            name = input('Name: ').strip()
            if name == '':
             print('Name cannot be empty!')
             return
            
                    
            course = input('Course: ').strip()
            if course == '':
                print('Category cannot be empty!')
                return
                    

            number= float(input('Price: '))
            if 0<number>100:
                print('number is invalid')
                return
            
            grade = calgrade(number)

            p[0]['id']=id
            p[0]["name"]=name
            p[0]["course"]=course
            p[0]["number"]= number
            p[0]["grade"]=grade
            print("element re added into data")
            print_many_students(students[0])
    except:
        print("plese enter valid data type")
# -----------------------------------------------------
def savetojson():
    try:
     with open("file.json" ,"w") as f:
        f.dump(students ,f,indent=4)
    except:
        print("error while saving file try again")
# -----------------------------------------------------------
def loadfromjson():
    try:
        with open("file.json","r")as f:
           students = json.load(f)
           print("file load sucessfully")
           print(students)
    except:
        print("errror on loading file")
# ------------------------------------------------------------------------------------
def main():
    while True:
        choice = menu()

        match choice:
            case 1:
                add_students()
            case 2:
                view_students()
            case 3:
                search_student()
            case 4:
                update_student()
            case 5:
                delete_student()
            case 6:
                savetojson()
            case 7:
                loadfromjson()
            case 8:
                break
            case _:
                print('Invalid choice. Please retry.')


if __name__ == '__main__':
    main()