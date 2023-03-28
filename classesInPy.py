#display the output
class Employee:
    def __init__(self, ID, name, working_days):
        self.ID = ID
        self.name = name
        self.working_days = working_days
        
    def info(self):
        return "ID: " + self.ID + ", Name: " + self.name + ", working days: " + str(self.working_days)
    
    def salary(self, salary_per_day):
        return self.working_days * salary_per_day

employee = Employee("E001", "John Doe", 25)
print(employee.info()) # Output: "ID: E001, Name: John Doe, working days: 25"
print(employee.salary(100)) # Output: 2500
