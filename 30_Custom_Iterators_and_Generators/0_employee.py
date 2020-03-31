class Employee:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def get_name(self):
        return self._name


class EmployeeManager:
    def __init__(self):
        self._employee_list = []

    def add_employee(self, new_empl):
        self._employee_list.append(new_empl)

    def __iter__(self):
        self.eml_idx = -1
        return self

    def __next__(self):
        if(self.eml_idx >= len(self._employee_list) - 1):
            raise StopIteration()
        self.eml_idx += 1
        return self._employee_list[self.eml_idx].get_name()


hr_manager = EmployeeManager()
hr_manager.add_employee(Employee("Kobi", 32, 15000))
hr_manager.add_employee(Employee("Adi", 28, 17000))
hr_manager.add_employee(Employee("Chen", 25, 16000))

for emp_name in hr_manager:
    print(emp_name)

