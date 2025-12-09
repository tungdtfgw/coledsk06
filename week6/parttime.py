from employee import Employee

class PartTime(Employee):
    def __init__(self, name, rate, days):
        super().__init__(name, rate)
        self.days = days

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, days):
        if days < 0 or days > 5:
            print("Error: Days must be between 0 and 5.")
        else:
            self.__days = days

    @property
    def salary(self):
        return super().salary * self.days / 5
    
if __name__ == "__main__":
    john = Employee("John", 1.5)
    print(john.name, john.salary)

    paul = PartTime("Paul", 1.5, 3)
    print(paul.name, paul.salary)