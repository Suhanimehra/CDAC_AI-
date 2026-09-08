employees=[
    {"id": 1, "name": "Rahul Sharma", "department": "IT", "salary": 50000.0, "days_present": 25, "status": "Eligible"},
    {"id": 2, "name": "Priya Mehta", "department": "HR","salary": 45000.0, "days_present": 22, "status": "Regular"}
]

id_counter=len(employees)

import json


def main():
    global employees
    try:
        while True:
            menu()
            print('-'*60)

            user_choice=int(input("Choose Operation: "))

            match user_choice:
                case 1:
                    add_employee()
                case 2:
                    display_employees()
                case 3:
                    search_employees()
                case 4:
                    update_employees()
                case 5:
                    delete_eployees()
                case 6:
                    calculate_payroll(employees)
                case 7:
                    save_to_json()
                case 8:
                    load_to_json()
                case 9:
                    break
                case _ :
                    print("Enter Valid Operation Choice!!")


    except:
        print("Enter a valid integer value")

def menu():
    print("="*60)
    print("-----Employee Attendance & Payroll Managemnet System-----")
    menu_text='''
    [1] Add Employee 
    [2] View Employees 
    [3] Search Employee 
    [4] Update Employee 
    [5] Delete Employee 
    [6] Calculate Payroll 
    [7] Save to JSON 
    [8] Load from JSON 
    [9] Exit
    '''

    print("="*60)
    print (menu_text)
    print("="*60)

def add_employee():
    global id_counter
    try:

        name=input("Enter Name of Employe: ")
        if name.strip()=='':
            print("Name cannot be an empty string!")

        department=input("Enter Name of Department: ")
        if department.strip()=='':
            print("Name cannot be an empty string!")

        salary=float(input("Enter monthly salary: "))
        if not salary>0:
            print("Salary Cannot be negative!")

        days_present=int(input("Enter Days Present: "))
        if days_present not in range(0,27):
            print("Days cannot be less than 0 or more than 26!")

        status=calculate_status(days_present)
        print(status)

        employees.append(dict(id=id_counter+1,name=name,department=department,salary=salary,days_present=days_present,satus=status))
        id_counter+=1
    except:
        print("Enter Valid Values!")

def calculate_status(days_present):

    if days_present>=24:
        return "Eligible"

    if 20<=days_present<24:
        return "Regular"

    if 15<=days_present<20:
        return "Warning"

    if days_present<15:
        return "Critical"
    

def display_employees():

    if len(employees)==0:
        print("No Record!")

    elif len(employees)==1:
        print_one_record(employees[0])
    else:
        print_many_record(employees)

def print_one_record(e):

    id,name,department,salary,days_present,status=e.values()

    print("----Employee Details----")

    print(f"ID:              {id}")
    print(f"Name:            {name}")
    print(f"Department:      {department}")
    print(f"Salary:          {salary}")
    print(f"Days Present:    {days_present}")
    print(f"Status:          {status}")

def print_many_record(employees):

    print("----Employee Details----")

    print(f"{'ID':<5}{'Name':<10}{'Department':<15}{'Salary':>10}{'Days Present':>10}{'Status':>7}")
    for e in employees:
        id,name,department,salary,days_present,status=e.values()
        print(f"{id:<5}{name:<10}{department:<15}{salary:>10}{days_present:>10}{status:>7}")


def search_employees():

    search_choice=int(input("Enter 1 for Search by ID.\n Enter 2 to search by Employee Name.\n Enter 3 to search by Department Name."))

    if search_choice==1:
        search_by_id()
    elif search_choice==2:
        search_by_name()
    elif search_choice==3:
        search_by_department()
    else:
        print("Enter a Valid Choice To search.")

def search_by_id():
    try:
        id_choice=int(input("Enter Employee ID to search: "))

        res =[e for e in employees if e['id']==id_choice]

        if not res:
            print(f"No Employee Found of {id_choice}")

        else:
            print_one_record(res[0])

    except:
        print("Input a Valid ID Value!")

def search_by_name():
    try:
        name_choice=int(input("Enter Employee Name to search: "))

        if name_choice.strip()=='':
            print("Name cannot be an empty string!")


        res =[e for e in employees if name_choice.lower().strip() in e['name'].lower()]

        if not res:
            print(f"No Employee Found of {name_choice}")

        else:
            print_many_record(res)

    except:
        print("Input a Valid Name Value!")

def search_by_department():
    try:
        dept_choice=int(input("Enter Department Name to search: "))

        if dept_choice=='':
            print("Department Cannot be an empty string!")

        res =[e for e in employees if dept_choice.lower().strip() in e['dept'].lower()]

        if not res:
            print(f"No Employee Found of {dept_choice}")

        else:
            print_many_record(res)

    except:
        print("Input a Valid Name Value!")

def update_employees():

    update_choice=int(input("Enter The Employee ID to Update: "))
    res =[e for e in employees if e['id']==update_choice]

    if not res:
        print("No Employee Found!")

    else:
        name=input("Enter Name of Employe: ")
        if name.strip()=='':
            print("Name cannot be an empty string!")

        department=input("Enter Name of Department: ")
        if department.strip()=='':
            print("Name cannot be an empty string!")

        salary=float(input("Enter monthly salary: "))
        if not salary>0:
            print("Salary Cannot be negative!")

        days_present=int(input("Enter Days Present: "))
        if days_present not in range(0,27):
            print("Days cannot be less than 0 or more than 26!")

        res[0]['name']=name
        res[0]['department']=department
        res[0]['salary']=salary
        res[0]['days_present']=days_present
        res[0]['status']=calculate_status(days_present)

        print_many_record(employees)


def delete_eployees():

    delete_choice=int(input("Enter ID you want to Delete: "))

    res=[e for e in employees if e['id']==delete_choice]

    if not res:
        print("No Employee Found !")

    else:
        sure_choice=("Are You Sure [y/n]: ")
        if sure_choice.strip().lower()=='y':
            employees.remove(res[0])
            print("Employee Removed Successfully! ")
            if len(employees)==0:
                print("No Record Left!")
            else:
                print_many_record(employees)
        else:
            print("Nothing Deleted")
    
def calculate_payroll(employees):
    for e in employees:
        salary=e['salary']
        present_days=e['days_present']
        daily_salary=salary//26
        absent_days=26-present_days
        deduction=daily_salary*absent_days
        final_salary=salary-deduction

        print(final_salary)


def save_to_json():
    try:
        with open("employees.json", mode='w') as file:

            json.dump(employees,file)

            print("File saved successfully")

    except:
        print("Not saved")
def load_to_json():
    pass

if __name__=='__main__':
    main()