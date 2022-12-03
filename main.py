#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner
print("Hello!, I am your personalized budget planner")
print("Let's get started how much you earn")

class Income(object):
    def __init__(self):
        self.hour_pay = 0
        self.hour_work = 0
        self.total_income = 0

    def Hourly_pay(self):
        print("How many incomes of your income are paid by hour?")
        n = int(input())
        if not type(n) is int:
            raise ValueError
        for i in range(n):
            print("How much money do you earn in an hour?")
            hour_pay = int(input())
            if not type(hour_pay) is int:
                raise ValueError
            else:
                print("How many hours do you work per week?")
            hour_work = int(input())
            if not type(hour_work) is int:
                    raise ValueError
            else:
                weekly_income = hour_pay * hour_work
                print("On average your weekly income is",weekly_income)
                print("On average your monthly income is",(weekly_income*4))
                print("On average your annual income is",(weekly_income*52))

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
            amount = int(input("Enter income amount: "))
            if not type(amount) is int:
                raise ValueError
            income[name] = amount 
        incomeList = '\n'.join(f'{key}: {value}' for key, value in income.items())
        print("List of Incomes")
        print(incomeList)
        total_income = sum(income.values())
        print("Total Income:",total_income)  

class Expenses(object):
    def __init__(self):
        self.name = 0
        self.amount = 0
        self.total_expenses = 0

    def Total_Expenses(self):
        expenses = {}
        print("How many expenses do you have?")
        n = int(input())
        if not type(n) is int:
                raise TypeError("Sorry! You entered an incorrect value, please try again")
        for i in range(n):
            name = input("Enter expense name: ")
            if not type(name) is str:
                raise TypeError("Sorry! You entered an incorrect value, please try again")
            amount = int(input("Enter expense amount: "))
            if not type(amount) is int:
                raise TypeError("Sorry! You entered an incorrect value, please try again")
            expenses[name] = amount 
        expenseList = '\n'.join(f'{key}: {value}' for key, value in expenses.items())
        print("List of Expenses")
        print(expenseList)
        totalexpenses = sum(expenses.values())
        print("Total Expenses:",totalexpenses)
    
class NetIncome(Income,Expenses):
    def __init__(self):
        MytotalIncome = self.total_income
        MyTotExpenses = self.total_expenses
        MyNet = MytotalIncome - MyTotExpenses
        print("After processing your income and bills, we've calculated your net income")
        print(MyNet)

if __name__ == '__main__':

    my_wallet = Income()
    while True:
        try:
            my_wallet.Hourly_pay()
            my_wallet.Total_Income()
        except ValueError:
            print("Sorry! You entered an incorrect value, please try again")
        else:
            break
        
    my_bills = Expenses()
    my_bills.Total_Expenses()

    my_net = NetIncome()
