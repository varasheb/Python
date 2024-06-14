import random

class Employee:
    def __init__(self, name):
        self.name = name

    def check_attendance(self):
        attendance_status = random.randint(0, 1)
        return attendance_status



if __name__=='__main__':
    print("Welcome to Employee Wage Computation Program")

    employee = Employee("Varshab Kanthi")
    attendance = employee.check_attendance()
    if attendance == 1:
        print(f"{employee.name} is present.")
    else:
        print(f"{employee.name} is absent.")