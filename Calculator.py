#This will be a home loan repayment estimator and timeline estimator if certain amounts are paid.

#This will be the person class where we enter all their information to use the various methods we will create

class Person:
    def __init__(self, loan, duration, interest_rate):
        self.loan = loan
        self.duration = duration
        self.interest_rate = interest_rate
        