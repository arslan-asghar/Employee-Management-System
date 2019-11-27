# This is an employee class and it is a parent class
# This function will get only integer value
employee_designations = ("Manager", "Supervisor", "Supervisor Backup", "Sales Man", "Office Boy")


def input_number(message):
    while True:
        try:
            user_input = int(input(message))

        except ValueError:
            print("Not an integer value! Try again")
            continue
        else:
            return user_input
        break


def designation():
    while True:

        choice = input_number("Chose Designation\n1-Manager\n2-Supervisor\n3-Supervisor Backup\n4-Sales Man\n5-Office Boy")
        if choice > 0 and choice < 6:
            return employee_designations[choice-1]
            break
        else:
            print("value must be integer from 1 - 5")



class Employee:
    e_id = 0

    def __init__(self, nam, des, sal, exp, rep=None):

        self.Name = nam
        self.Roll = des
        self.Salary = sal
        self.Report = rep
        self.Experience = exp
        self.Manger_Remarks = "none"
        self.employee_id = 0
# new comment by me

    def showemployees(self, lst):
        print("--------------------------------------------")
        print("            All Employees Data")
        print("--------------------------------------------")
        for i in lst:
            print("Employee ID = ", i.employee_id)
            print("Employee Name = ", i.Name)
            print("Employee Designation = ", i.Roll)
            print("Employee Report = ", i.Report)
            print("Employee Experience = ", i.Experience)
            print("Manger Remarks = ", i.Manger_Remarks)
            print("--------------------------------------------")

    def set_id(self, id):
        self.employee_id = id


class EmployeeManager(Employee):
    def __init__(self):
        pass

    def show_report(self, lst):

        search_employee = input("Enter employee id for search report")
        s_m = int(search_employee)

        for i in lst:
            if i.Employee_Id == s_m:
                print("--------------------------------------------")
                print("            Employee Report")
                print("--------------------------------------------")
                print("Employee ID = ", i.Employee_Id)
                print("Employee Name = ", i.Name)
                print("Employee Designation = ", i.Roll)
                print("Employee Report = ", i.Report)
                print("Last Remarks = ", i.Manger_Remarks)
                remarks = input("Enter Remarks")
                i.Manger_Remarks = remarks
                print("--------------------------------------------")
                break

        else:
            print("employee does not exist")


# create function for manage employee
# if progress is less then 5 then do not assign other task


class EmployeeGeneral(Employee):
    def __init__(self):
        pass

    def create_report(self, lst):
        search_employee = input("Enter employee id for Enter report")
        s_m = int(search_employee)

        for i in lst:
            if i.Employee_Id == s_m:
                print("--------------------------------------------")
                print("            Employee Report")
                print("--------------------------------------------")
                print("Employee ID = ", i.Employee_Id)
                print("Employee Name = ", i.Name)
                print("Employee Designation = ", i.Roll)
                i.Report = int(input("Enter Report (1 - 10) = "))


                print("--------------------------------------------")
                break

        else:
            print("employee does not exist")

    def manager_remarks(self, lst):

        search_employee = input("Enter employee id for search report")
        s_m = int(search_employee)

        for j in lst:
            if j.Employee_Id == s_m:
                print("--------------------------------------------")
                print("            Manger Remarks on Report")
                print("--------------------------------------------")
                print("Employee ID = ", j.Employee_Id)
                print("Employee Name = ", j.Name)
                print("Employee Designation = ", j.Roll)
                print("Employee Report = ", j.Report)
                print("Manager Remarks = ", j.Manger_Remarks)

                print("--------------------------------------------")
                break

        else:
            print("employee does not exist")




Employee_List = []


def add_employee():
    print("--------------------------------------------")
    print("            Create new employee")
    print("--------------------------------------------")
    name = input("Enter Name :")
    # roll = input("Enter Employee designation : ")
    roll = designation()

    experience = 0
    salary = input_number("Enter your salary")
    print("--------------------------------------------")
    return name, roll, experience, salary


def add_new_employee():
    name, roll, experience, salary = add_employee()
    employee = Employee(name, roll, experience, salary)
    employee.set_id(Employee.e_id + 1)
    Employee.e_id = Employee.e_id + 1
    Employee_List.append(employee)


#Employee_obj = Employee(1, "Arslan", "PM", 500, 1, "none")
#Employee_List.append(Employee_obj)
i = 1
while i > 0:
    print("Enter Your Desiger Value for Search\n 1 - Add New Employee\n 2 - Search All Employees")
    print(" 3 - Search Report ( Only for manager )\n 4 - Enter Report\n 5 - Search Manager Remarks on Report")
    search_value = int(input("Enter here : "))
    if search_value == 1:
        add_new_employee()
    elif search_value == 2:
        Obj = EmployeeManager()
        Obj.showemployees(Employee_List)
        print("thank you")
    elif search_value == 3:
        Obj = EmployeeManager()
        Obj.show_report(Employee_List)
    elif search_value == 4:
        print("working on it...")
        obj = EmployeeGeneral()
        obj.create_report(Employee_List)
    elif search_value == 5:
        obj = EmployeeGeneral()
        obj.manager_remarks(Employee_List)



    else:
        print("you chosen wrong value")
    choice = int(input("Enter 1 - If you want to goto main menu"))
    if choice != 1:
        print("End programe")
        break
