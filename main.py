from fastapi import FastAPI
import calculate_salaries
app = FastAPI()

ov_salary = calculate_salaries.CalculateSalary


@app.post('/salary-calc')
def salaries(antiquity: int, position: str, yop: int):
    salary = ov_salary.calculate_overall_salary(antiquity, position, yop)
    return {"salary": salary,
            "employee name": ov_salary.name}  # name es heredado de la clase Employee.




