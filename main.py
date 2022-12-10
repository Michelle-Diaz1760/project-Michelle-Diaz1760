'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Budget Planner
'''
Wage calculator that will help the user see an average amount of income they recieve 
on a weekly, monthly, and annual basis
'''
def Hourly_pay():
    """ Function:
            Prints a dictionary of weekly, monthly, and annual wage income amount
            in which the key is the name of the wage source, and the value is the 
            amount of money gained from the source. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in integer input

        Returns:
            No returns       
    """
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
        """ Function:
            -   Prints a dictionary of listed monthly income in which the key
                is the name of the income source,and the value is the amount of 
                money gained from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total income. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of the values of the dictionary into attribute self.total_income  
            returns self.total_income 
        """
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
        """ Function:
            -   Prints a dictionary of listed monthly fixed expenses in which the key
                is the name of the expenses source,and the value is the amount of 
                money needed to be spent from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total expense. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If float entered in integer input

        Returns:
            returns the sum of the values of the dictionary into attribute self.total_fixed_expenses  
            returns self.total_fixed_expenses 
        """
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
        """ Function:
            -   Prints a dictionary of listed monthly Variable Expenses in which the key
                is the name of the Variable Expenses source,and the value is the amount of 
                money needed to be spent from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total Variable_Expenses. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of the values of the dictionary into self.total_variable_expenses
            returns self.total_variable_expenses
        """
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
        """ Function:
            - Adds the total fixed expenses and the total variable variable into an attribute self.total_expenses
            - Prints attribute self.total_expenses as total monthly expense

        Parameters:
            No Parameters added or used

        Raises:

        Returns:
            returns the sum of self.total_fixed_expenses and self.total_variable_expenses as self.total_expenses
            returns self.total_expense
        """
        F = self.total_fixed_expenses
        V = self.total_variable_expenses
        self.total_expenses = F + V
        print (f"Total Monthly Expenses: ${self.total_expenses:.2f}") 
        return self.total_expenses

    def Net_Income(self):
        """ Function:
            - subtracts the total income and the total expenses into an attribute self.net_income
            - Prints attribute self.net_income as monthly net income

        Parameters:
            No Parameters added or used

        Raises:

        Returns:
            returns the difference of self.total_income  and self.total_expenses as self.net_income
            returns self.net_income
        """
        I = self.total_income 
        E = self.total_expenses
        self.net_income = I - E
        print (f"Monthly Net Income: ${self.net_income:.2f}") 
        print("---------------")
        return self.net_income

    def Percent_Savings(self):
        """ Function:
            -   returns the product of self.net_income with float input of desired percentage of savings for budget
        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns self.amount_saved
        """
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
        """ Function:
            - subtracts the total net income and savings into an attribute self.non_essentials
            - Prints attribute self.non_essentials as monthly non essentials

        Parameters:
            No Parameters added or used

        Raises:

        Returns:
            returns the difference of self.net_income and self.amount_saved as self.non_essentials
            returns self.non_essentials
        """
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
        """ Function:
            -   Prints a summary of the total income, total expenses, net income, amount of money 
                saved and amount for non-essentials for a Weekly budget 
        Parameters:
            No Parameters added or used

        Raises:
            No Raises

        Returns:
            returns attributes self.total_income, self.total_expenses, self.net_income
                    self.amount_saved, and self.non_essentials
        """
        print("---------------")
        print("Weekly Budget Review:")
        print(f"Total Income:{(self.total_income/4):.2f}")
        print(f"Total Expenses:{(self.total_expenses/4):.2f}")
        print(f"Total Net Income:{(self.net_income/4):.2f}")
        print(f"Total Amount Saved:{(self.amount_saved/4):.2f}")
        print(f"Total Non-Essentials:{(self.non_essentials/4):.2f}")
        print("---------------")

    def M_Info_Summary(self):
        """ Function:
            -   Prints a summary of the total income, total expenses, net income, amount of money 
                saved and amount for non-essentials for a Monthly budget 
        Parameters:
            No Parameters added or used

        Raises:
            No Raises

        Returns:
            returns attributes self.total_income, self.total_expenses, self.net_income
                    self.amount_saved, and self.non_essentials
        """
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
        """ Function:
            -   Prints a summary of the total income, total expenses, net income, amount of money 
                saved and amount for non-essentials for a Annual budget 
        Parameters:
            No Parameters added or used

        Raises:
            No Raises

        Returns:
            returns attributes self.total_income, self.total_expenses, self.net_income
                    self.amount_saved, and self.non_essentials
        """
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
        """ Function:
            -   Prints a dictionary of listed monthly income in which the key
                is the name of the income source,and the value is the amount of 
                money gained from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total income. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of the values of the dictionary into attribute self.total_income  
            returns self.total_income 
        """
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
        """ Function:
            -   Prints a dictionary of listed monthly fixed expenses in which the key
                is the name of the expenses source,and the value is the amount of 
                money needed to be spent from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total expense. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of the values of the dictionary into attribute self.total_fixed_expenses  
            returns self.total_fixed_expenses 
        """
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
        """ Function:
            -   Prints a dictionary of listed monthly Variable Expenses in which the key
                is the name of the Variable Expenses source,and the value is the amount of 
                money needed to be spent from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total Variable_Expenses. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of the values of the dictionary into self.total_variable_expenses
            returns self.total_variable_expenses
        """
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
        """ Function:
            - Adds the total fixed expenses and the total variable variable into an attribute self.total_expenses
            - Prints attribute self.total_expenses as total monthly expense

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of self.total_fixed_expenses and self.total_variable_expenses as self.total_expenses
            returns self.total_expense
        """
        F = self.total_fixed_expenses
        V = self.total_variable_expenses
        self.total_expenses = F + V
        print (f"Total Monthly Expenses: ${self.total_expenses:.2f}")
        print("---------------")
        return self.total_expenses

    def Percent_Savings(self):
        """ Function:
            -   returns float input as attribute self.amount_saved
        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns self.amount_saved
        """
        print("How much money did you save?")
        while True:
            personalized_savings = abs(float(input("Enter Savings:")))
            if not type(personalized_savings) is float:
                    raise ValueError 
            self.amount_saved = personalized_savings
            print("---------------")
            return self.amount_saved
    
    def Non_Essential(self):
        """ Function:
            -   Prints a dictionary of listed monthly non-essentials in which the key
                is the name of the non-essentials source,and the value is the amount of 
                money spent from the source. 
            -   Prints a sum of the values of the dictionary as a overall monthly total non-essentials. 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the sum of the values of the dictionary into attribute self.non_essentials  
            returns self.non_essentials
        """
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
        """ Function:
            -   returns the product of 50% of the total income compares it to the the total amount 
                of expenses
            -   if the expenses are less, it will print out pass
            -   if the expenses are more, it will print out fail 

        Parameters:
            No Parameters added or used

        Raises:

        Returns:
            returns the product of 50% of the total income compares it to the the total amount of expenses
        """
        I = self.total_income 
        half_income = I * 0.50
        E = self.total_expenses
        if E <= half_income:
            print("PASSED EXPENSE BUDGET!")
        elif E > half_income:
            print("FAILED EXPENSE BUDGET!")
            print("LOWER EXPENSES")

    def passORfail_Percent_Savings(self):
        """ Function:
            -   returns the product of 20% of the total income compares it to the savings
            -   if the savings are less, it will print out fail
            -   if the savings are more, it will print out pass

        Parameters:
            No Parameters added or used

        Raises:

        Returns:
            returns the product of 20% of the total income compares it to the savings
        """
        I = self.total_income 
        AS = self.amount_saved
        twenty_income = I * 0.20
        if AS <= twenty_income:
            print("FAILED SAVING BUDGET!")
            print("RAISE SAVINGS")
        elif AS > twenty_income :
            print("PASSED EXPENSE BUDGET!")

    def passORfail_Non_Essential(self):
        """ Function:
            -   returns the product of 30% of the total income compares it to the total amount of non essentials
            -   if the non essentials are less, it will print out pass
            -   if the non_essentials are more, it will print out fail

        Parameters:
            No Parameters added or used

        Raises:

        Returns:
            returns the product of 30% of the total income compares it to the total non essentials
        """
        I = self.total_income
        NE = self.non_essentials
        thirty_income = I * 0.30
        if NE <= thirty_income:
            print("PASSED NON-ESSENTIALS BUDGET!")
        elif NE > thirty_income :
            print("FAILED NON-ESSENTIALS BUDGET!")
            print("LOWER NON-ESSENTIALS")
    
    def PERpassORfail_Expenses(self):
        """ Function:
            -   returns the product of 50% of the total income compares it to the the total amount 
                of expenses
            -   if the expenses are less, it will print out pass
            -   if the expenses are more, it will print out fail 

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the product of 50% of the total income compares it to the the total amount of expenses
        """
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
        """ Function:
            -   returns the product of 20% of the total income compares it to the savings
            -   if the savings are less, it will print out fail
            -   if the savings are more, it will print out pass

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the product of 20% of the total income compares it to the savings
        """
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
        """ Function:
            -   returns the product of 30% of the total income compares it to the total amount of non essentials
            -   if the non essentials are less, it will print out pass
            -   if the non_essentials are more, it will print out fail

        Parameters:
            No Parameters added or used

        Raises:
            ValueError - If string entered in float input

        Returns:
            returns the product of 30% of the total income compares it to the total non essentials
        """
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
        quit()
