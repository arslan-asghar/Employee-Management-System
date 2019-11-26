# This is an employee class and it is a parent class


class Employee:

    def __init__(self, id, nam, des, sal, rep, exp):
        self.Employee_Id = id
        self.Name = nam
        self.Roll = des
        self.Salary = sal
        self.Report = rep
        self.Experience = exp
        self.Manger_Remarks = "none"
#new commentt
    def showemployees(self, lst):
        print("--------------------------------------------")
        print("            All Employees Data")
        print("--------------------------------------------")
        for i in lst:
            print("Employee ID = ", i.Employee_Id)
            print("Employee Name = ", i.Name)
            print("Employee Designation = ", i.Roll)
            print("Employee Report = ", i.Report)
            print("Employee Experience = ", i.Experience)
            print("Manger Remarks = ", i.Manger_Remarks)
            print("--------------------------------------------")


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
    employee_id = int(input("Enter Employee ID : "))
    name = input("Enter Name :")
    roll = input("Enter Employee designation : ")
    experience = 0
    salary = int(input("Enter Employee Salary :"))
    print("--------------------------------------------")
    return employee_id, name, roll, experience, salary


def add_new_employee():
    a, b, c, d, e = add_employee()
    add_employe = Employee(a, b, c, d, "none", e)
    Employee_List.append(add_employe)


Employee_obj = Employee(1, "Arslan", "PM", 500, 1, "none")
Employee_List.append(Employee_obj)
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
