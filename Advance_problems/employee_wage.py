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

    def calculate_monthly_wage(self, max_hours=100, max_days=20):
        total_wage = 0
        total_hours = 0
        total_days = 0
        
        while total_hours < max_hours and total_days < max_days:
            attendance = self.check_attendance()
            if attendance == 1:
                total_hours += self.full_day_hours
                total_wage += self.calculate_wage(self.full_day_hours)
                total_days += 1
            elif attendance == 2:
                total_hours += self.part_time_hours
                total_wage += self.calculate_wage(self.part_time_hours)
                total_days += 1
            else:
                total_days += 1  

        return total_wage,total_days,total_hours
    
if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")

    employee = Employee("Varshab Kanthi")
    monthly_report = employee.calculate_monthly_wage()

    print(f"Monthly wage of {employee.name} for {monthly_report[1]} working days with {monthly_report[2]} hours worked: Rs.{monthly_report[0]:.2f}")

