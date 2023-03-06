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

    @property
    def name(self):
        """
        :return: employee name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        :param new_name: new name value
        :return: new name
        """
        if new_name == "":
            print(f'please, give your employee the name')
        else:
            self.__name = new_name

    @property
    def second_name(self):
        """
        :return: employee second name
        """
        return self.__second_name

    @second_name.setter
    def second_name(self, new_second_name: str):
        """
        :param new_second_name: change value
        :return: edited employee second name
        """
        if new_second_name == "":
            print(f'please, give your employee the second name')
        else:
            self.__second_name = new_second_name

    @property
    def gender(self):
        """
        :return: employee gender
        """
        return self.__gender

    @gender.setter
    def gender(self, new_gender: str):
        """
        :param new_gender: new gender value
        :return: new gender
        """
        if new_gender == "":
            print(f"please, set your employee's gender")
        else:
            self.__gender = new_gender

    @property
    def hire_date(self):
        """
        :return: employee hire date
        """
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, new_hire_date: str):
        """
        :param new_hire_date: new hire date value
        :return: new hire date
        """
        if new_hire_date == "":
            print(f"please, set your employee's hire date")
        else:
            self.__hire_date = new_hire_date

    @property
    def salary(self):
        """
        :return: employee salary
        """
        return self.__salary

    @salary.setter
    def salary(self, new_salary: int):
        """
        :param new_salary: new salary value
        :return: new salary
        """
        if new_salary < 0:
            print(f"it's not fear")
        else:
            self.__salary = new_salary

    @property
    def birth_date(self):
        """
        :return: date of birth
        """
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, new_birth_date: str):
        """
        :param new_birth_date: new date of birth value
        :return: new date of birth
        """
        birth_date = datetime.strptime(new_birth_date, '%Y-%m-%d')
        if birth_date.year > 120:
            print("you are too old")
        if birth_date.year <= 14:
            print('you are too yong')
        else:
            self.__birth_date = new_birth_date

    def get_age(self):
        """
        :return: employee age
        """
        birthday = datetime.strptime(self.__birth_date, '%Y-%m-%d')
        age = now.year - birthday.year
        return age

    def add_new_year_bonus_to_salary(self):
        """
        :return: add new year bonus to salary at december
        """
        if now.month == 12:
            return self.__salary + 100
        else:
            return self.__salary

    def increase_salary(self, increase_persent: int):
        """
        :param increase_persent: salary rise persent
        :return: employee new salary
        """
        self.__salary += round(increase_persent / 100 * self.__salary)
        return self.__salary


if __name__ == '__main__':
    mia = Employee('Mia', 'Ko', 'f', 2000, '2020-02-02', '1990-01-01')
    # print(mia.name)
    # mia.name = ""
    # print(mia.name)
    # print(mia.second_name)
    # mia.second_name = 'Fey'
    # print(mia.second_name)
    # print(mia.age())
    # print(mia.salary_with_new_year_bonus())
    # print(mia.salary_evaluate(20))
    # print(mia.salary)
    # mia.salary = -5
    # print(mia.salary)
    print(mia.birth_date)
    mia.birth_date = "v"
