'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner
def Hourly_pay():
    while True:
        print("---------------")
        print("Wage Calculator")
        print("if you don't have a wage income or you are finished, Type DONE")
        JobName=input("Income source:")
        if JobName.lower() == "done":
            print("---------------")
            break
        else:
            print("How much money do you earn in an hour?")         
            hour_pay = float(input())
            if not type(hour_pay) is float:
                raise ValueError
            while (True):
                print("How many hours do you work per week?")
                hour_work = float(input())
                if not type(hour_work) is float:
                    raise ValueError
                if hour_work > 168:
                    print("TOO MANY HOURS!")
                else:
                    break
            weekly_income = hour_pay * hour_work
            print("---------------")
            print("Income:",JobName)
            print(f"On average your weekly income: ${weekly_income:.2f}")
            monthly_income = weekly_income * 4
            print(f"On average your monthly income: ${monthly_income:.2f}")
            annual_income = monthly_income * 12
            print(f"On average your annual income: ${annual_income:.2f}")
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
        print("---------------")
        print("Enter Monthly Incomes:")
        print("Note:")
        print("Please retype the calculated income or enter new incomes")
        print("Type DONE when finished")
        print("---------------")
        while True:
            name = input("Enter income source: ")
            if name.lower() == "done":
                break
            else:
                if not type(name) is str:
                    raise ValueError
                amount = abs(float(input("Enter monthly income amount: ")))
                if not type(amount) is float:
                    raise ValueError
                income[name] = amount 
        incomeList = '\n'.join(f'{key}: ${value:.2f}' for key, value in income.items())
        print("---------------")
        print("List of Incomes")
        print(incomeList)
        self.total_income = sum(income.values())
        print(f"Total Monthly Income: ${self.total_income:.2f}")
        print("---------------")
        return self.total_income
      
    def Fixed_Expenses(self):
        expenses = {}
        print("---------------")
        print("Please enter monthly fixed expenses:")
        print("Type DONE when finished")
        while True:
            name = input("Enter expense name: ")
            if name.lower() == "done":
                break 
            else:
                if not type(name) is str:
                    raise ValueError
                amount = abs(float(input("Enter monthly expense amount: ")))
                if not type(amount) is float:
                    raise ValueError
                expenses[name] = amount
        expenseList = '\n'.join(f'{key}: ${value:.2f}' for key, value in expenses.items())
        print("---------------")
        print("List of Fixed Expenses")
        print(expenseList)
        self.total_fixed_expenses = sum(expenses.values())
        print(f"Total Monthly Fixed Expenses: ${self.total_fixed_expenses:.2f}")
        print("---------------")
        return self.total_fixed_expenses

    def Variable_Expenses(self):
            expenses = {}
            print("---------------")
            print("Please enter monthly variable expenses:")
            print("Type DONE when finished")
            while True:
                    name = input("Enter expense name: ")
                    if name.lower() == "done":
                        break 
                    else:
                        if not type(name) is str:
                            raise ValueError
                        amount = abs(float(input("Enter monthly expense amount: ")))
                        if not type(amount) is float:
                            raise ValueError
                        expenses[name] = amount
            expenseList = '\n'.join(f'{key}: ${value:.2f}' for key, value in expenses.items())
            print("---------------")
            print("List of Variable Expenses")
            print(expenseList)
            self.total_variable_expenses = sum(expenses.values())
            print(f"Total Monthly Variable Expenses: ${self.total_variable_expenses:.2f}")
            print("---------------")
            return self.total_variable_expenses
    
    def Total_Expenses(self):
        F = self.total_fixed_expenses
        V = self.total_variable_expenses
        self.total_expenses = F + V
        print (f"Total Monthly Expenses: ${self.total_expenses:.2f}") 
        return self.total_expenses

    def Net_Income(self):
        I = self.total_income 
        E = self.total_expenses
        self.net_income = I - E
        print (f"Monthly Net Income: ${self.net_income:.2f}") 
        print("---------------")
        return self.net_income

    def Percent_Savings(self):
        print("What percent from your net income do you want to save?")
        print("Please enter a number:___%")
        if self.net_income <= 0:
            self.amount_saved == 0
            print("---------------")
            print(f"Monthly Savings: ${self.amount_saved:.2f}")
            return self.amount_saved
        else:
            personalized_savings = float(input())
            if not type(personalized_savings) is float:
                    raise ValueError 
            int_float = personalized_savings/100
            self.amount_saved = self.net_income * int_float
            print("---------------")
            print(f"Monthly Savings: ${self.amount_saved:.2f}")
            return self.amount_saved

    def Non_Essential(self):
        if self.net_income <= 0:
            self.non_essentials == 0
            print(f"Monthly Money for Non-Essentials: ${self.non_essentials:.2f}")
            print("---------------")
            return self.non_essentials
        else:
            self.non_essentials = self.net_income - self.amount_saved
            print(f"Monthly Money for Non-Essentials: ${self.non_essentials:.2f}")
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
        print(f"Total Income:{self.total_income:.2f}")
        print(f"Total Expenses:{self.total_expenses:.2f}")
        print(f"Total Net Income:{self.net_income:.2f}")
        print(f"Total Amount Saved:{self.amount_saved:.2f}")
        print(f"Total Non-Essentials:{self.non_essentials:.2f}")
        print("---------------")

    def A_Info_Summary(self):
        year = input("Enter Year:")
        print("---------------")
        print(f"{year} Budget Review:")
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
        self.num_bud_expense = 0
        self.num_bud_savings = 0
        self.num_bud_non_essen = 0 

    def Total_Income(self):
        income = {}
        print("Please enter Monthly Incomes:")
        print("Type DONE when finished")
        while True:
            name = input("Enter income source: ")
            if name.lower() == "done":
                break 
            else:
                if not type(name) is str:
                    raise ValueError
                amount = abs(float(input("Enter monthly income amount: ")))
                if not type(amount) is float:
                    raise ValueError
                income[name] = amount 
        self.total_income = sum(income.values())
        print(f"Total Monthly Income: ${self.total_income:.2f}")
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
                    amount = abs(float(input("Enter monthly expense amount: ")))
                    if not type(amount) is float:
                        raise ValueError
                    expenses[name] = amount
        self.total_fixed_expenses = sum(expenses.values())
        print(f"Total Monthly Fixed Expenses: ${self.total_fixed_expenses:.2f}")
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
                        amount = abs(float(input("Enter monthly expense amount: ")))
                        if not type(amount) is float:
                            raise ValueError
                        expenses[name] = amount
            self.total_variable_expenses = sum(expenses.values())
            print(f"Total Monthly Variable Expenses: ${self.total_variable_expenses:.2f}")
            print("---------------")
            
            return self.total_variable_expenses
    
    def Total_Expenses(self):
        F = self.total_fixed_expenses
        V = self.total_variable_expenses
        self.total_expenses = F + V
        print (f"Total Monthly Expenses: ${self.total_expenses:.2f}")
        print("---------------")
        return self.total_expenses

    def Percent_Savings(self):
        print("How much money did you save?")
        while True:
            personalized_savings = abs(float(input("Enter Savings:")))
            if not type(personalized_savings) is float:
                    raise ValueError 
            self.amount_saved = personalized_savings
            print("---------------")
            return self.amount_saved
    
    def Non_Essential(self):
        non_essentials = {}
        print("Please enter monthly non-essentials:")
        print("Type DONE when finished")
        while True:
            name = input("Enter non-essential name: ")
            if name.lower() == "done":
                break 
            else:
                if not type(name) is str:
                    raise ValueError
                amount = abs(float(input("Enter non-essential amount: ")))
                if not type(amount) is float:
                    raise ValueError
                non_essentials[name] = amount
        self.non_essentials = sum(non_essentials.values())
        print(f"Total Non-Essential Expenses: ${self.non_essentials:.2f}")
        print("---------------") 
        return self.non_essentials

    def passORfail_Expenses(self):
        I = self.total_income 
        half_income = I * 0.50
        E = self.total_expenses
        if E <= half_income:
            print("PASSED EXPENSE BUDGET!")
        elif E > half_income:
            print("FAILED EXPENSE BUDGET!")
            print("LOWER EXPENSES")

    def passORfail_Percent_Savings(self):
        I = self.total_income 
        AS = self.amount_saved
        twenty_income = I * 0.20
        if AS <= twenty_income:
            print("FAILED SAVING BUDGET!")
            print("RAISE SAVINGS")
        elif AS > twenty_income :
            print("PASSED EXPENSE BUDGET!")

    def passORfail_Non_Essential(self):
        I = self.total_income
        NE = self.non_essentials
        thirty_income = I * 0.30
        if NE <= thirty_income:
            print("PASSED NON-ESSENTIALS BUDGET!")
        elif NE > thirty_income :
            print("FAILED NON-ESSENTIALS BUDGET!")
            print("LOWER NON-ESSENTIALS")
    
    def PERpassORfail_Expenses(self):
        I = self.total_income 
        self.num_bud_expense = abs(int(input("what is your budget for expenses:")))
        if not type(self.num_bud_expense) is int:
            raise ValueError
        int_percent = self.num_bud_expense/100
        budget_income = I * int_percent
        E = self.total_expenses
        if E <= budget_income:
            print("PASSED EXPENSE BUDGET!")
        elif E > budget_income:
            print("FAILED EXPENSE BUDGET")
            print("LOWER EXPENSES")
        return self.num_bud_expense

    def PERpassORfail_Percent_Savings(self):
        I = self.total_income 
        AS = self.amount_saved
        while (True):
            self.num_bud_savings = abs(int(input("what is your budget for savings:")))
            if not type(self.num_bud_savings) is int:
                raise ValueError
            if self.num_bud_savings > (100-self.num_bud_expense):
                print("INCORRECT VALUE, MAKE IT LESS")
            else:
                break
        int_percent = self.num_bud_savings/100
        budget_income = I * int_percent
        if AS <= budget_income:
            print("FAILED SAVING BUDGET!")
            print("RAISE SAVINGS")
        elif AS > budget_income :
            print("PASSED EXPENSE BUDGET")
        return self.num_bud_savings

    def PERpassORfail_Non_Essential(self):
        I = self.total_income
        NE = self.non_essentials
        while (True):
            self.num_bud_non_essen = abs(int(input("what is your budget for non-essentials:")))
            if not type(self.num_bud_non_essen) is int:
                raise ValueError
            if self.num_bud_non_essen > (100-self.num_bud_expense-self.num_bud_savings):
                print("INCORRECT VALUE")
            else:
                break
        int_percent = self.num_bud_non_essen/100
        budget_income = I * int_percent
        if NE <= budget_income:
            print("PASSED NON-ESSENTIALS BUDGET!")
        elif NE > budget_income :
            print("FAILED NON-ESSENTIALS BUDGET")
            print("LOWER NON-ESSENTIALS")
        return self.num_bud_non_essen

if __name__ == '__main__':
    print("Hello! I am your personalized budget planner")
    print("Do you want to make a budget plan?")
    print("Please type YES or NO")
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
                            print("INCORRECT, TRY AGAIN!")
                        else:
                            while True:
                                try:
                                    my_budget.Variable_Expenses()
                                except ValueError as VE:
                                    print("INCORRECT, TRY AGAIN!")
                                else:
                                    while True:
                                        try:
                                            my_budget.Total_Expenses()
                                        except ValueError as VE:
                                            print("INCORRECT, TRY AGAIN!")
                                        else:
                                            my_budget.Net_Income()
                                            while True:
                                                try:
                                                    my_budget.Percent_Savings()
                                                except ValueError as VE:
                                                        print("INCORRECT, TRY AGAIN!")
                                                else:
                                                    my_budget.Non_Essential()
                                                    print("Information Summary:")
                                                    print("Type WEEKLY, MONTHLY, OR ANNUAL")
                                                    print("When finished, type DONE")
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
    if y.lower() =="yes":
        passORFail = Pass_Fail()
        while True:
            try:
                passORFail.Total_Income()
            except ValueError as VE:
                print("INCORRECT, TRY AGAIN!")
            else:
                while True:
                    try:
                        passORFail.Fixed_Expenses()
                    except ValueError as VE:
                        print("INCORRECT, TRY AGAIN!")
                    else:
                        while True:
                            try:
                                passORFail.Variable_Expenses()
                            except ValueError as VE:
                                print("INCORRECT, TRY AGAIN!")
                            else:
                                while True:
                                    try:
                                        passORFail.Total_Expenses()
                                    except ValueError as VE:
                                        print("INCORRECT, TRY AGAIN!")
                                    else:
                                        while True:
                                            try:
                                                passORFail.Non_Essential()
                                            except ValueError as VE:
                                                print("INCORRECT, TRY AGAIN!")
                                            else:
                                                while True:
                                                    try:
                                                        passORFail.Percent_Savings()
                                                    except ValueError as VE:
                                                        print("INCORRECT, TRY AGAIN!")
                                                    else:
                                                        while True:
                                                            print("Do you want to use your own personalized budget plan?")
                                                            print("Please type YES or NO")
                                                            x = input().lower()
                                                            if x not in ['yes', 'no']:
                                                                print("Please Enter Yes or No")
                                                            else:
                                                                break
                                                        if x == "yes":
                                                            while True:
                                                                try:
                                                                    passORFail.PERpassORfail_Expenses()
                                                                except ValueError as VE:
                                                                    print("INCORRECT, TRY AGAIN!")
                                                                else:
                                                                    while True:
                                                                        try:    
                                                                            passORFail.PERpassORfail_Percent_Savings()
                                                                        except ValueError as VE:
                                                                            print("INCORRECT, TRY AGAIN!")
                                                                        else:
                                                                            while True:
                                                                                try:
                                                                                    passORFail.PERpassORfail_Non_Essential()
                                                                                except ValueError as VE:
                                                                                    print("INCORRECT, TRY AGAIN!")
                                                                                quit()
                                                        elif x == "no":
                                                            passORFail.passORfail_Expenses()
                                                            passORFail.passORfail_Non_Essential()
                                                            passORFail.passORfail_Percent_Savings()
                                                            quit()
if y.lower =="no":
