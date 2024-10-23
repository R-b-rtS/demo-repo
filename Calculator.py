#This will be a home loan repayment estimator and timeline estimator if certain amounts are paid.

#This will be the person class where we enter all their information to use the various methods we will create

class Person:
    def __init__(self, loan: float, duration: int, interest_rate: float, repayment_freq: str):
        """
        Loan: The total loan amount in dollars
        Duration: The length of the mortgage
        Interest rate: Current annual interest rate as a percentage
        Repayment freq: How often you pay the mortgage: Weekly, Fortnightly, Monthly
        """
        self.loan = loan
        self.duration = duration
        self.interest_rate = interest_rate
        self.repayment_freq = repayment_freq
    def __repr__(self):
        return f"Hello your loan amount is " + str(self.loan) + ". The duration of your loan is"
    def repayment_frequency(self):
        frequencies = {
            "Weekly": 52,
            "Monthly": 12,
            "Fortnightly": 26
        }
        return frequencies.get(self.repayment_freq, 12) * self.duration
    
    def monthly_interest(self):
        return self.interest_rate / 100 / 12
    
    def repayment_calc(self):
        repayments = (self.loan * self.monthly_interest() * (1 + self.monthly_interest())** self.repayment_frequency()) / ((1 + self.monthly_interest()) ** self.repayment_frequency() - 1)
        return repayments

person1 = Person(200000, 30, 6.24, "Monthly")
print(person1)
print(person1.repayment_calc())
