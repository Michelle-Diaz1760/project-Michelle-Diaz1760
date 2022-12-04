#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner
class Monthly():
    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.net_income = 0
        self.amount_saved = 0
        self.non_essentials = 0

    def Hourly_pay(self):
        print("How many of your incomes have an hourly wage?")
        n = int(input())
        if not type(n) is int:
            raise ValueError
        for i in range(n):
            JobName=input("Income name:")
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
            monthly_income = weekly_income * 4
            print(f"On average your monthly income for {JobName} is ${monthly_income}")
            print("Next Income->")

    def Total_Income(self):
        income = {}
        print("How many incomes do you have?")
        n = int(input())
        if not type(n) is int:
                raise ValueError
        for i in range(n):
            name = input("Enter income name: ")
            if not type(name) is str:
                raise ValueError
            amount = float(input("Enter monthly income amount: "))
            if not type(amount) is float:
                raise ValueError
            income[name] = amount 
        incomeList = '\n'.join(f'{key}: ${value}' for key, value in income.items())
        print("List of Incomes")
        print(incomeList)
        self.total_income = sum(income.values())
        print(f"Total Monthly Income: ${self.total_income}")
        return self.total_income
      
    def Total_Expenses(self):
        expenses = {}
        print("How many monthly expenses do you have?")
        n = int(input())
        if not type(n) is int:
                raise TypeError
        for i in range(n):
            name = input("Enter expense name: ")
            if not type(name) is str:
                raise TypeError
            amount = int(input("Enter monthly expense amount: "))
            if not type(amount) is int:
                raise TypeError
            expenses[name] = amount 
        expenseList = '\n'.join(f'{key}: ${value}' for key, value in expenses.items())
        print("List of Expenses")
        print(expenseList)
        self.total_expenses = sum(expenses.values())
        print(f"Total Monthly Expenses: ${self.total_expenses}")
        return self.total_expenses

    def Net_Income(self):
        I = self.total_income 
        E = self.total_expenses
        self.net_income = I - E
        print (f"Monthly Net Income: ${self.net_income}") 
        return self.net_income

    def Percent_Savings(self):
        print("What percent from your net income do you want to save?")
        print("Please enter a decimal value:")
        personalized_savings = float(input())
        self.amount_saved = self.net_income * personalized_savings
        print(f"Monthly Savings: ${self.amount_saved:.2f}")
        return self.amount_saved

    def Non_Essential(self):
        self.non_essentials = self.net_income - self.amount_saved
        print(f"Monthly Money for Non-Essentials: ${self.non_essentials}")
        return self.non_essentials
    

if __name__ == '__main__':

    # let the user chose if they want a monthly, weekly, or annual budget
    my_monthly_budget = Monthly()
    my_monthly_budget.Hourly_pay()
    my_monthly_budget.Total_Income()
    my_monthly_budget.Total_Expenses()
    my_monthly_budget.Net_Income()
    my_monthly_budget.Percent_Savings()
    my_monthly_budget.Non_Essential()

