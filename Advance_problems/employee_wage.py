import random

class Employee:
    def __init__(self, name, wage_per_hour=200, full_day_hours=8, part_time_hours=4):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = full_day_hours
        self.part_time_hours = part_time_hours

    def check_attendance(self):
        attendance_status = random.randint(0, 2)
        return attendance_status
    
    def calculate_wage(self, hours_worked):
        return self.wage_per_hour * hours_worked

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")

    employee = Employee("Varshab Kanthi")
    attendance = employee.check_attendance()

    if attendance == 1:
        print(f"{employee.name} is present full-time.")
        daily_wage = employee.calculate_wage(employee.full_day_hours)
        print(f"Daily wage of {employee.name}: Rs.{daily_wage}")
    elif attendance == 2:
        print(f"{employee.name} is present part-time.")
        daily_wage = employee.calculate_wage(employee.part_time_hours)
        print(f"Daily wage of {employee.name}: Rs.{daily_wage}")
    else:
        print(f"{employee.name} is absent.")
