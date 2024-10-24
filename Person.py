#Just creating a bit of separation between the person who will be using this, and the loan concept.
from Loan import Loan
class Person:
    def __init__(self, name: str, age: int, loan: Loan):
        self.name = name
        self.age = age
        self.loan = loan
    
    def __repr__(self):
        return f"{self.name}, aged {self.age}, has a loan of ${self.loan.amount:.2f}."
    
