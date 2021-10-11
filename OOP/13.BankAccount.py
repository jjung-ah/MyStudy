class BankAccount:
    """은행 계좌 클래스"""
    
    def __init__(self, name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.name = name
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘린다"""
        self.balance += amount
    
    def withdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount 만큼 줄인다"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount 
    
    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려준다"""
        self.balance *= 1 + BankAccount.interest 