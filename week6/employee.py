class Employee:
    BASIC_SALARY = 1000

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == '':
            print("Error: Name cannot be empty.")
        else:
            self.__name = name
        
    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        if rate < 0:
            print("Error: Rate cannot be negative.")
        else:
            self.__rate = rate

    @property
    def salary(self):
        return self.BASIC_SALARY * self.rate