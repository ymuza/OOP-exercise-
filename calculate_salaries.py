
class Employee:
    name = "barney"
    lastname = "gumble"
    age = 40


class CalculateSalary(Employee):
    years_of_exp = 0

    @staticmethod
    def calculate_overall_salary(antiquity, position, yop):
       # @classmethod  si uso el cls con el years_of_exp , muestro qe desde main no puedo cambiar el valor si se lo paso porque hay encapsulamiento
        # def calculate_overall_salary(cls, antiquity, position):
        salary = 0
        if position == "a" and antiquity >= 10:
            salary = 10000
        elif position == "a" and antiquity < 10:
            salary = 8000
        elif position == "b" and antiquity >= 10:
            salary = 6000
        elif position == "b" and antiquity < 10:
            salary = 4000
        # overall_salary = salary + (cls.years_of_exp*50)
        overall_salary = salary + (yop * 50)
        return overall_salary


class Taxes:
    pass




