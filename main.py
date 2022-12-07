'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner
def Hourly_pay():
    while True:
        print("Enter Wage Income:")
        print("Type DONE when finished")
        JobName=input("Income name:")
        if JobName.lower() == "done":
            print("---------------")
            break
        else:
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
            if name.lower() == "done":
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
            if name.lower() == "done":
                break 
            else:
                if not type(name) is str:
                    raise ValueError
                amount = int(input("Enter monthly expense amount: "))
                if not type(amount) is int:
                    raise ValueError
                due_date = input("Enter due date: ")
                if not type(name) is str:
                    raise ValueError
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
                    if name.lower() == "done":
                        break 
                    else:
                        if not type(name) is str:
                            raise ValueError
                        amount = int(input("Enter monthly expense amount: "))
                        if not type(amount) is int:
                            raise ValueError
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
            print("Please enter a number:___%")
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
        month = input("Enter Month:")
        print("---------------")
        print(f"{month} Budget Review:")
        print(f"Total Income:{self.total_income}")
        print(f"Total Expenses:{self.total_expenses}")
        print(f"Total Net Income:{self.net_income}")
        print(f"Total Amount Saved:{self.amount_saved}")
        print(f"Total Non-Essentials:{self.non_essentials}")
        print("---------------")

    def A_Info_Summary(self):
        year = input("Enter Year:")
        print("---------------")
        print("Annual Budget Review:")
        print(f"Total Income:{(self.total_income*12):.2f}")
        print(f"Total Expenses:{(self.total_expenses*12):.2f}")
        print(f"Total Net Income:{(self.net_income*12):.2f}")
        print(f"Total Amount Saved:{(self.amount_saved*12):.2f}")
        print(f"Total Non-Essentials:{(self.non_essentials*12):.2f}")
        print("---------------")

class Pass_Fail():
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
            if name.lower == "done":
                break 
            else:
                if not type(name) is str:
                    raise ValueError
                amount = float(input("Enter monthly income amount: "))
                if not type(amount) is float:
                    raise ValueError
                income[name] = amount 
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
                if name.lower == "done":
                    break 
                else:
                    if not type(name) is str:
                        raise ValueError
                    amount = int(input("Enter monthly expense amount: "))
                    if not type(amount) is int:
                        raise ValueError
                    expenses[name] = amount
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
                    if name.lower == "done":
                        break 
                    else:
                        if not type(name) is str:
                            raise ValueError
                        amount = int(input("Enter monthly expense amount: "))
                        if not type(amount) is int:
                            raise ValueError
                        expenses[name] = amount
            self.total_variable_expenses = sum(expenses.values())
            print(f"Total Monthly Variable Expenses: ${self.total_variable_expenses}")
            print("---------------")
            
            return self.total_variable_expenses
    
    def Total_Expenses(self):
        F = self.total_fixed_expenses
        V = self.total_variable_expenses
        self.total_expenses = F + V
        print (f"Total Monthly Expenses: ${self.total_expenses}")
        print("---------------")
        return self.total_expenses

    def Percent_Savings(self):
            print("How much money did you save?")
            personalized_savings = float(input("Enter Savings:"))
            if not type(personalized_savings) is float:
                    raise ValueError 
            self.amount_saved = personalized_savings
            return self.amount_saved
    
    def Non_Essential(self):
        non_essentials = {}
        print("Please enter monthly non-essentials:")
        print("Type DONE when finished")
        while True:
                name = input("Enter non-essential name: ")
                if name.lower == "done":
                    break 
                else:
                    if not type(name) is str:
                        raise ValueError
                    amount = int(input("Enter non-essential amount: "))
                    if not type(amount) is int:
                        raise ValueError
                    non_essentials[name] = amount
        self.non_essentials = sum(non_essentials.values())
        print(f"Total Non-Essential Expenses: ${self.non_essentials}")
        print("---------------") 
        return self.non_essentials

    def passORfail_Expenses(self):
        I = self.total_income 
        half_income = I * 0.50
        E = self.total_expenses
        if E <= half_income:
            print("PASS EXPENSE BUDGET!")
        elif E > half_income:
            print("FAILED EXPENSE BUDGET")

    def passORfail_Percent_Savings(self):
        I = self.total_income 
        AS = self.amount_saved
        twenty_income = I * 0.20
        if AS <= twenty_income:
            print("FAILED SAVING BUDGET!")
        elif AS > twenty_income :
            print("PASS EXPENSE BUDGET")

    def passORfail_Non_Essential(self):
        I = self.total_income
        NE = self.non_essentials
        thirty_income = I * 0.30
        if NE <= thirty_income:
            print("PASS NON-ESSENTIALS BUDGET!")
        elif NE > thirty_income :
            print("FAILED NON-ESSENTIALS BUDGET")
    
    def PERpassORfail_Expenses(self):
        I = self.total_income 
        num = int(input("what is your budget for expenses:"))
        if not type(num) is int:
            raise ValueError
        int_percent = num/100
        budget_income = I * int_percent
        E = self.total_expenses
        if E <= budget_income:
            print("PASS EXPENSE BUDGET!")
        elif E > budget_income:
            print("FAILED EXPENSE BUDGET")

    def PERpassORfail_Percent_Savings(self):
        I = self.total_income 
        AS = self.amount_saved
        num = int(input("what is your budget for savings:"))
        if not type(num) is int:
            raise ValueError
        int_percent = num/100
        budget_income = I * int_percent
        if AS <= budget_income:
            print("FAILED SAVING BUDGET!")
        elif AS > budget_income :
            print("PASS EXPENSE BUDGET")

    def PERpassORfail_Non_Essential(self):
        I = self.total_income
        NE = self.non_essentials
        num = int(input("what is your budget for non-essentials:"))
        if not type(num) is int:
            raise ValueError
        int_percent = num/100
        budget_income = I * int_percent
        if NE <= budget_income:
            print("PASS NON-ESSENTIALS BUDGET!")
        elif NE > budget_income :
            print("FAILED NON-ESSENTIALS BUDGET")

if __name__ == '__main__':
    print("Hello! I am your personalized budget planner")
    print("Do you want to make a budget plan?")
while(True):
    x = input().lower()
    if x not in ['yes', 'no']:
        print("Please Enter Yes or No")
    else:
        break
if x == "yes":            
    while True:
        try:
            Wage = Hourly_pay()
        except ValueError as VE:
            print("INCORRECT, TRY AGAIN")
        else:
            while True:
                try:
                    my_budget = Budget_Plan()
                    my_budget.Total_Income()
                except ValueError as VE:
                    print("INCORRECT, TRY AGAIN")
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
                                                            if budget_plan.lower() == "done":
                                                                quit()
                                                            if budget_plan.lower() == "weekly":
                                                                my_budget.W_Info_Summary()
                                                            elif budget_plan.lower() == "monthly":
                                                                my_budget.M_Info_Summary()
                                                            elif budget_plan.lower() == "annual":
                                                                my_budget.A_Info_Summary()
if x == "no":
    print("Do you want to see if you pass your current budget plan?")
    while(True):
        y = input().lower()
        if y not in ['yes', 'no']:
            print("Please Enter Yes or No")
        else:
            break
        if y.lower =="yes":
            passORFail = Pass_Fail()
            while True:
                try:
                    passORFail.Total_Income()
                except ValueError as VE:
                    print("INCORRECT!")
                else:
                    while True:
                        try:
                            passORFail.Fixed_Expenses()
                        except ValueError as VE:
                            print("INCORRECT!")
                        else:
                            while True:
                                try:
                                    passORFail.Variable_Expenses()
                                except ValueError as VE:
                                    print("INCORRECT!")
                                else:
                                    while True:
                                        try:
                                            passORFail.Total_Expenses()
                                        except ValueError as VE:
                                            print("INCORRECT!")
                                        else:
                                            while True:
                                                try:
                                                    passORFail.Percent_Savings()
                                                except ValueError as VE:
                                                        print("INCORRECT!")
                                                else:
                                                    while True:
                                                        try:
                                                            passORFail.Non_Essential()
                                                        except ValueError as VE:
                                                            print("INCORRECT!")
                                                            break
                                                        else: 
                                                            print("Do you want to use your own personalized budget plan?")
                                                        while True:
                                                            budget_plan = input()
                                                            if budget_plan == "YES":
                                                                passORFail.PERpassORfail_Expenses()
                                                                passORFail.PERpassORfail_Percent_Savings()
                                                                passORFail.PERpassORfail_Non_Essential()
                                                            elif budget_plan == "NO":
                                                                passORFail.passORfail_Expenses()
                                                                passORFail.passORfail_Percent_Savings()
                                                                passORFail.passORfail_Non_Essential()
                                                            quit()
    if y.lower =="no":
        quit()
