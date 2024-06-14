import random

class Employee:
    def __init__(self, name ,wage_per_hour =20,full_day_hours=8):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = full_day_hours

    def check_attendance(self):
        attendance_status = random.randint(0, 1)
        return attendance_status
    
    def calculate_daily_wage(self):
        return self.wage_per_hour * self.full_day_hours

if __name__=='__main__':
    print("Welcome to Employee Wage Computation Program")

    employee = Employee("Varshab Kanthi")
    attendance = employee.check_attendance()
    if attendance == 1:
        print(f"{employee.name} is present.")
        daily_wage = employee.calculate_daily_wage()
        print(f"Daily wage of {employee.name}: {daily_wage}")
    else:
        print(f"{employee.name} is absent.")