#This will be a home loan repayment estimator and timeline estimator if certain amounts are paid.

#This will be the Loan class where we enter all the loan information to use the various methods we will create

class Loan:
    def __init__(self, amount: float, duration: int, interest_rate: float, repayment_freq: str):
        """
        Amount: The total loan amount in dollars
        Duration: The length of the mortgage
        Interest rate: Current annual interest rate as a percentage
        Repayment freq: How often you pay the mortgage: Weekly, Fortnightly, Monthly
        """
        self.amount = amount
        self.duration = duration
        self.interest_rate = interest_rate
        self.repayment_freq = repayment_freq
    def __repr__(self):
        return f"Hello your loan amount is ${self.amount}. The duration of your loan is {self.duration} years at an interest rate of {self.interest_rate}% p.a. Because you are making {self.repayment_freq} payments your repayments will be ${self.repayment_calc(): .2f}."
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
        monthly_interest = self.monthly_interest()
        repayment_frequency = self.repayment_frequency()
        repayments = (self.amount * monthly_interest * (1 + monthly_interest)** repayment_frequency) / ((1 + monthly_interest) ** repayment_frequency - 1)
        
        #Adjust repayment based on frequency
        if self.repayment_freq == "Weekly":
            return repayments / 4.33 #This converts the payment to weekly
        elif self.repayment_freq == "Fortnightly":
            return repayments / 2.17 #This converts the payment to fortnightly
        else:
            return repayments #the default formula calculates monthly repayments
        
    def lifetime_payments(self): #this shows them how much they pay back over the life of the loan
        return self.repayment_calc() * self.repayment_frequency()
    
    def lifetime_interest(self):
        return self.lifetime_payments() - self.amount
    
    def new_term(self, extra_payment):
        total_payment = self.repayment_calc() + extra_payment
        balance = self.amount
        time = 0

        while balance > 0:
            interest = balance * self.monthly_interest()
            balance = balance - (total_payment - interest)
            time += 1
        return time


person1 = Loan(200000, 30, 6.24, "Monthly")
print(person1)
extra_payment = person1.new_term(100)
print(extra_payment)

