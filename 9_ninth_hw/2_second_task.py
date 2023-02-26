"""
Create a class with a description of the worker. Any worker. employees.

I will evaluate the completeness of the described class and will withdraw points for everything unnecessary.
I want to see clean code. I expect to see clean code with annotations.
So far, no first-class connections with the second. In all methods, I expect to see docstrings with a sane description.
"""
from datetime import datetime

now = datetime.today()


class Employee:
    def __init__(self, __name: str, __second_name: str, __gender: str, __salary: int, __hire_date: str,
                 __birth_date: str):
        self.__name = __name
        self.__second_name = __second_name
        self.__gender = __gender
        self.__salary = __salary
        self.__hire_date = __hire_date
        self.__birth_date = __birth_date

    def get_name(self):
        """
        :return: employee name
        """
        return self.__name

    def get_second_name(self):
        """
        :return: employee second name
        """
        return self.__second_name

    def set_second_name(self, new_second_name: str):
        """
        :param new_second_name: change value
        :return: edited employee second name
        """
        if isinstance(new_second_name, str):
            self.__second_name = new_second_name
        else:
            return 'Second name change not supported'

    def get_gender(self):
        """
        :return: employee gender
        """
        return self.__gender

    def hire_date(self):
        """
        :return: employee hire date
        """
        return self.__hire_date

    def get_salary(self):
        """
        :return: employee salary
        """
        return self.__salary

    def employee_age(self):
        """
        :return: employee age
        """
        birthday = datetime.strptime(self.__birth_date, '%Y-%m-%d')
        age = now.year - birthday.year
        return age

    def salary_with_new_year_bonus(self):
        """
        :return: add new year bonus to salary at december
        """
        if now.month == 12:
            return self.__salary + 100
        else:
            return self.__salary

    def salary_evaluate(self, rise_persent: int):
        """
        :param rise_persent: salary rise persent
        :return: employee new salary
        """
        self.__salary += round(rise_persent / 100 * self.__salary)
        return self.__salary


if __name__ == '__main__':
    mia = Employee('Mia', 'Ko', 'f', 2000, '2020-02-02', '1990-01-01')
    print(mia.get_name())
    print(mia.get_second_name())
    mia.set_second_name('Fey')
    print(mia.get_second_name())
    print(mia.employee_age())
    print(mia.salary_with_new_year_bonus())
    print(mia.salary_evaluate(20))
    print(mia.get_salary())
