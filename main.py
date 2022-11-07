#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner

#INCOME

# Hourly Pay
print("How much do you make an hour?")
hourPay = int(input())
print("How many hours do you work?")
hourWork = int(input())
weeklyPay = hourPay * hourWork
print("Weekly wage:", weeklyPay )
MonthlyPay = weeklyPay * 4
print("Monthly wage:",MonthlyPay)


def returnSum(income):
 
    sum = 0
    for i in income.values():
        sum = sum + i
    return sum

income = {}
 
print("How many incomes do you have?")
n = int(input())
 
for i in range(n):
    
    name = input("Enter income name: ")
    amount = int(input("Enter income amount: "))
    income[name] = amount 

incomeList = '\n'.join(f'{key}: {value}' for key, value in income.items())

print("List of Incomes")
print(incomeList)
Totalincome = returnSum(income)
print("Total Income:",Totalincome)

#EXPENSES

def returnSum(expenses):
 
    sum = 0
    for i in expenses.values():
        sum = sum + i
    return sum

expenses = {}
 
print("How many expenses do you have?")
n = int(input())
 
for i in range(n):
    
    name = input("Enter expense name: ")
    amount = int(input("Enter expense amount: "))
    expenses[name] = amount 

expensesList = '\n'.join(f'{key}: {value}' for key, value in expenses.items())

print("List of Expenses")
Totalexpenses = returnSum(expenses)
print("Total Expenses:",Totalexpenses)