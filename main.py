#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner
def Hourly_pay():
    print("Enter Wage Income:")
    print("Type DONE when finished")
    while True:   
        JobName=input("Income name:")
        if JobName == "DONE":
            print("---------------")
            break
        if not type(JobName) is str:
            raise ValueError
        print("How much money do you earn in an hour?")         
        hour_pay = float(input())
        if not type(hour_pay) is float:
            raise ValueError
        print("How many hours do you work per week?")
        hour_work = float(input())
        if not type(hour_work) is float:
            raise ValueError
        weekly_income = hour_pay * hour_work
        print("---------------")
        print("Income:",JobName)
        print(f"On average your weekly income: ${weekly_income}")
        monthly_income = weekly_income * 4
        print(f"On average your monthly income: ${monthly_income}")
        annual_income = monthly_income * 12
        print(f"On average your annual income: ${annual_income}")
        print("---------------")

class Budget_Plan():
    def __init__(self):
        self.total_income = 0
        self.total_fixed_expenses = 0
        self.total_variable_expenses = 0
        self.total_expenses = 0
        self.net_income = 0
        self.amount_saved = 0
        self.non_essentials = 0

    def Total_Income(self):
        income = {}
        print("Please enter Monthly Incomes:")
        print("Type DONE when finished")
        while True:
            name = input("Enter income name: ")
            if name == "DONE":
                break 
            else:
                if not type(name) is str:
                    raise ValueError
                amount = float(input("Enter monthly income amount: "))
                if not type(amount) is float:
                    raise ValueError
                income[name] = amount 
        incomeList = '\n'.join(f'{key}: ${value}' for key, value in income.items())
        print("---------------")
        print("List of Incomes")
        print(incomeList)
        self.total_income = sum(income.values())
        print(f"Total Monthly Income: ${self.total_income}")
        print("---------------")
        return self.total_income
      
    def Fixed_Expenses(self):
        expenses = {}
        print("Please enter monthly fixed expenses:")
        print("Type DONE when finished")
        while True:
                name = input("Enter expense name: ")
                if name == "DONE":
                    break 
                else:
                    if not type(name) is str:
                        raise TypeError
                    amount = int(input("Enter monthly expense amount: "))
                    if not type(amount) is int:
                        raise TypeError
                    due_date = input("Enter due date: ")
                    if not type(name) is str:
                        raise TypeError
                    expenses[name] = amount
        expenseList = '\n'.join(f'{key}: ${value}, DUE: {due_date}' for key, value in expenses.items())
        print("---------------")
        print("List of Fixed Expenses")
        print(expenseList)
        self.total_fixed_expenses = sum(expenses.values())
        print(f"Total Monthly Fixed Expenses: ${self.total_fixed_expenses}")
        print("---------------")
        return self.total_fixed_expenses

    def Variable_Expenses(self):
            expenses = {}
            print("Please enter monthly variable expenses:")
            print("Type DONE when finished")
            while True:
                    name = input("Enter expense name: ")
                    if name == "DONE":
                        break 
                    else:
                        if not type(name) is str:
                            raise TypeError
                        amount = int(input("Enter monthly expense amount: "))
                        if not type(amount) is int:
                            raise TypeError
                        expenses[name] = amount
            expenseList = '\n'.join(f'{key}: ${value}' for key, value in expenses.items())
            print("---------------")
            print("List of Variable Expenses")
            print(expenseList)
            self.total_variable_expenses = sum(expenses.values())
            print(f"Total Monthly Variable Expenses: ${self.total_variable_expenses}")
            print("---------------")
            return self.total_variable_expenses
    
    def Total_Expenses(self):
        F = self.total_fixed_expenses
        V = self.total_variable_expenses
        self.total_expenses = F + V
        print (f"Total Monthly Expenses: ${self.total_expenses}") 
        return self.total_expenses

    def Net_Income(self):
        I = self.total_income 
        E = self.total_expenses
        self.net_income = I - E
        print (f"Monthly Net Income: ${self.net_income}") 
        print("---------------")
        return self.net_income

    def Percent_Savings(self):
            print("What percent from your net income do you want to save?")
            print("Please enter a number:")
            personalized_savings = float(input())
            if not type(personalized_savings) is float:
                    raise ValueError 
            int_float = personalized_savings/100
            self.amount_saved = self.net_income * int_float
            print(f"Monthly Savings: ${self.amount_saved:.2f}")
            return self.amount_saved

    def Non_Essential(self):
        self.non_essentials = self.net_income - self.amount_saved
        print(f"Monthly Money for Non-Essentials: ${self.non_essentials}")
        print("---------------")
        return self.non_essentials

    def W_Info_Summary(self):
        print("---------------")
        print("Weekly Budget Review:")
        print(f"Total Income:{(self.total_income/4):.2f}")
        print(f"Total Expenses:{(self.total_expenses/4):.2f}")
        print(f"Total Net Income:{(self.net_income/4):.2f}")
        print(f"Total Amount Saved:{(self.amount_saved/4):.2f}")
        print(f"Total Non-Essentials:{(self.non_essentials/4):.2f}")
        print("---------------")

    def M_Info_Summary(self):
        print("---------------")
        print("Monthly Budget Review:")
        print(f"Total Income:{self.total_income}")
        print(f"Total Expenses:{self.total_expenses}")
        print(f"Total Net Income:{self.net_income}")
        print(f"Total Amount Saved:{self.amount_saved}")
        print(f"Total Non-Essentials:{self.non_essentials}")
        print("---------------")

    def A_Info_Summary(self):
        print("---------------")
        print("Annual Budget Review:")
        print(f"Total Income:{(self.total_income*12):.2f}")
        print(f"Total Expenses:{(self.total_expenses*12):.2f}")
        print(f"Total Net Income:{(self.net_income*12):.2f}")
        print(f"Total Amount Saved:{(self.amount_saved*12):.2f}")
        print(f"Total Non-Essentials:{(self.non_essentials*12):.2f}")
        print("---------------")

if __name__ == '__main__':
    print("Hello! I am your personalized budget planner")
    while True:
        try:
            Wage = Hourly_pay()
        except ValueError as VE:
                        print("INCORRECT!")
        else:
            my_budget = Budget_Plan()
            while True:
                try:
                    my_budget.Total_Income()
                except ValueError as VE:
                    print("INCORRECT!")
                else:
                    while True:
                        try:
                            my_budget.Fixed_Expenses()
                        except ValueError as VE:
                            print("INCORRECT!")
                        else:
                            while True:
                                try:
                                    my_budget.Variable_Expenses()
                                except ValueError as VE:
                                    print("INCORRECT!")
                                else:
                                    while True:
                                        try:
                                            my_budget.Total_Expenses()
                                        except ValueError as VE:
                                            print("INCORRECT!")
                                        else:
                                            my_budget.Net_Income()
                                            while True:
                                                try:
                                                    my_budget.Percent_Savings()
                                                except ValueError as VE:
                                                        print("INCORRECT!")
                                                else:
                                                    my_budget.Non_Essential()
                                                    print("Information Summary:")
                                                    print("Type WEEKLY, MONTHLY, OR ANNUAL")
                                                    while True:
                                                            budget_plan = input()
                                                            if budget_plan == "DONE":
                                                                quit()
                                                            if budget_plan == "WEEKLY":
                                                                my_budget.W_Info_Summary()
                                                            elif budget_plan == "MONTHLY":
                                                                my_budget.M_Info_Summary()
                                                            elif budget_plan == "ANNUAL":
                                                                my_budget.A_Info_Summary()
                                                            
