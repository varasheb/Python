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

    def calculate_monthly_wage(self, working_days=20):
        total_wage = 0
        for day in range(working_days):
            attendance = self.check_attendance()
            if attendance == 1:
                total_wage += self.calculate_wage(self.full_day_hours)
            elif attendance == 2:
                total_wage += self.calculate_wage(self.part_time_hours)
        return total_wage

if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")

    employee = Employee("Varshab Kanthi")
    monthly_wage = employee.calculate_monthly_wage()

    print(f"Monthly wage of {employee.name} for 20 working days: Rs.{monthly_wage:.2f}")
