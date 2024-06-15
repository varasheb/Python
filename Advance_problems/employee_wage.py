import random

class Employee:
    def __init__(self, name, wage_per_hour, full_day_hours, part_time_hours):
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
class Company(Employee):
    def __init__(self, company_name,name, wage_per_hour, full_day_hours=8, part_time_hours=4):
        super().__init__(name, wage_per_hour, full_day_hours, part_time_hours)
        self.company_name=company_name


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")

    employees = [ 
        Company("Google","Varshab Kanthi",1000),
        Company("Intellicar", "Ramesh",400),
        Company("Amazon", "Suresh",200),
        Company("Microsoft", "Ganesh",230)
                ]
    for employee in employees:
        monthly_report = employee.calculate_monthly_wage()

        print(f"Monthly wage of {employee.company_name}'s employee {employee.name}:")
        print(f"- For {monthly_report[1]} working days")
        print(f"- With {monthly_report[2]} hours worked")
        print(f"- Total wage: Rs.{monthly_report[0]:.2f}")





                  