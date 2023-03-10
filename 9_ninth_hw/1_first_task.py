"""
Create a class describing any company. For example, Toshiba or Apple

I will evaluate the completeness of the described class and will withdraw points for everything unnecessary.
I want to see clean code. I expect to see clean code with annotations.
So far, no first-class connections with the second. In all methods, I expect to see docstrings with a sane description.
"""
import re
from datetime import date, timedelta, datetime


class Apple:
    BRAND = "Apple"

    def __init__(self, __website: str, __address: str, __employees: int):
        self.__website = __website
        self.__address = __address
        self.__employees = __employees

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, new_employees_amount: int):
        if new_employees_amount >= 0:
            self.__employees = new_employees_amount
        else:
            print(f'"{new_employees_amount}" is negative, amount should be positive')

    def add_employees(self, add_employees_num: int):
        """
        :param add_employees_num: update number of employees by the new employees
        :return: new number of employees
        """
        if add_employees_num == 0:
            return f'no new employee, amount should be more than {add_employees_num}'
        if add_employees_num > 0:
            self.__employees += add_employees_num
            return self.__employees
        else:
            return f'"{add_employees_num}" is negative, amount should be positive'

    def fire_employees(self, fire_employees_num: int):
        """
        :param fire_employees_num: update number of employees by reduction of employees amount
        :return: new number of employees
        """
        if fire_employees_num == 0:
            return f'no one was fired, amount should be more than {fire_employees_num}'
        if fire_employees_num < self.__employees:
            self.__employees -= fire_employees_num
            return self.__employees
        else:
            return f'amount "{fire_employees_num}" should be less than all employees amount: {self.__employees}'

    @property
    def website(self):
        """
        :return: website name
        """
        return self.__website

    @website.setter
    def website(self, new_website_page: str):
        """
        :param new_website_page: new website page value
        :return: a new website page
        """
        if re.match(r'(www.|)[A-z]+.com(\/(ua|it)|)', new_website_page):
            self.__website = new_website_page
        else:
            print(f'{new_website_page} is invalid')

    @property
    def address(self):
        """
        :return: address name
        """
        return self.__address

    @address.setter
    def address(self, new_address: str):
        """
        :param new_address: new address value
        :return: new address
        """
        self.__address = new_address

    @staticmethod
    def business_days_per_current_year():
        """
        :return: number of business days per current year
        """
        current_year = datetime.now().strftime("%Y")
        next_year = int(current_year) + 1
        current_year_start = date(int(current_year), 1, 1)
        next_year_start = date(int(next_year), 1, 1)
        all_days = (current_year_start + timedelta(x) for x in range((next_year_start - current_year_start).days))
        business_days = sum(1 for day in all_days if day.weekday() < 5)
        return business_days

    @staticmethod
    def work_days_except_holidays(holidays_num: int):
        """
        :param holidays_num: number of holidays
        :return: number of work days except holidays
        """
        return Apple.business_days_per_current_year() - holidays_num

    @staticmethod
    def work_days_except_vacation_per_employee(vacation_days: int, holidays_num: int):
        """
        :param vacation_days: number of vacation days per employee
        :param holidays_num: number of holidays
        :return: number of employee work days except holidays and vacation days
        """
        if vacation_days <= 20:
            return Apple.work_days_except_holidays(holidays_num) - vacation_days
        else:
            return f'Count of vacation days could be not more than 20 days'

    @staticmethod
    def work_days_except_sick_leave_per_employee(sick_leave_days: int, vacation_days: int, holidays_num: int):
        """
        :param sick_leave_days: number of employee sick leave days
        :param vacation_days: number of employee vacation days
        :param holidays_num: number of holidays
        :return: number of employee work days except holidays, vacation days and sick leave days
        """
        if sick_leave_days <= 15:
            return Apple.work_days_except_vacation_per_employee(vacation_days, holidays_num) - sick_leave_days
        else:
            return f'Sick leave days could not be payed for more than 15 days'


if __name__ == '__main__':
    apple = Apple("www", "some str", 1000)
    print(apple.BRAND)
    print(apple.website)
    apple.website = "apple.com"
    print(apple.website)
    print(apple.address)
    apple.address = "silicone str"
    print(apple.address)
    apple.employees = -1
    print(apple.employees)
    print(apple.add_employees(1))
    print(apple.add_employees(9))
    print(apple.employees)
    print(apple.fire_employees(0))
    print(apple.employees)
    print(Apple.business_days_per_current_year())
    print(Apple.work_days_except_holidays(holidays_num=10))
    print(Apple.work_days_except_vacation_per_employee(vacation_days=20, holidays_num=10))
    print(Apple.work_days_except_sick_leave_per_employee(vacation_days=15, holidays_num=20, sick_leave_days=10))
