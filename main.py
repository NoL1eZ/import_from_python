from application import salary
from application.db import people
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today())
    print(salary.calculate_salary())
    print(people.get_employees())

