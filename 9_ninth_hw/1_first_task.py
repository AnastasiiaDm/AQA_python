"""
Create a class describing any company. For example, Toshiba or Apple

I will evaluate the completeness of the described class and will withdraw points for everything unnecessary.
I want to see clean code. I expect to see clean code with annotations.
So far, no first-class connections with the second. In all methods, I expect to see docstrings with a sane description.
"""
from datetime import date, timedelta, datetime


class Apple:
    BRAND = "Apple"

    def __init__(self, __website: str = "apple.com", __address: str = "silicone str"):
        self.__website = __website
        self.__address = __address
        self.employees = 0

    def new_employee(self, new_employees_num: int):
        """
        :param new_employees_num: update number of employees by the new employees
        :return: new number of employees
        """
        self.employees += new_employees_num
        return self.employees

    def fire_employee(self, fire_employees_num: int):
        """
        :param fire_employees_num: update number of employees by reduction of employees amount
        :return: new number of employees
        """
        self.employees -= fire_employees_num
        return self.employees

    def website(self):
        """
        :return: website name
        """
        return self.__website

    def address(self):
        """
        :return: address name
        """
        return self.__address

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
    apple = Apple()
    print(apple.BRAND)
    print(apple.website())
    print(apple.address())
    print(apple.employees)
    print(apple.new_employee(1))
    print(apple.new_employee(9))
    print(apple.employees)
    print(apple.fire_employee(2))
    print(apple.employees)
    print(Apple.business_days_per_current_year())
    print(Apple.work_days_except_holidays(holidays_num=10))
    print(Apple.work_days_except_vacation_per_employee(vacation_days=20, holidays_num=10))
    print(Apple.work_days_except_sick_leave_per_employee(vacation_days=15, holidays_num=20, sick_leave_days=10))
