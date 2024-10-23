#This will be a home loan repayment estimator and timeline estimator if certain amounts are paid.

#This will be the person class where we enter all their information to use the various methods we will create

class Person:
    def __init__(self, loan: float, duration: int, interest_rate: float):
        """
        Loan: The total loan amount in dollars
        Duration: The length of the mortgage
        Interest rate: Current annual interest rate as a percentage
        """
        self.loan = loan
        self.duration = duration
        self.interest_rate = interest_rate

    def repayment_calculator(self):
        pass