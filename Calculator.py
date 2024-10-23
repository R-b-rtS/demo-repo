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
        self.repayment_freq = repaymet_freq

    def repayment_frequency(self):
        frequencies = {
            "Weekly": 52,
            "Monthly": 12,
            "Fortnightly": 26
        }
        return frequencies.get(self.repayment_freq, 12)
        