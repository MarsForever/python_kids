#BankAccount 建立一个类定义
#属性：帐户名-字符串，账号-一个字符串或整数，余额-浮点数
#显示余额，存钱和取钱
# -*- coding: utf-8 -*-
class BankAccout:
    def __init__(self,name,number):
        self.name =name
        self.number =number
        self.balance = 0.0
    def disBalance(self):
        print "The balance is:",self.balance
        
    def save(self , savemoney):
        self.balance = self.balance + savemoney
        print "You save", savemoney
        print "The new balance is:",self.balance

    def draw(self, outmoney):
        if self.balance >= outmoney:
            self.balance = self.balance - outmoney
            print "You withdraw ",outmoney
            print "The new balance is",self.balance
        else:
            print "You without", outmoney
            print "The balance is:",self.balance
            print "Withdraw denied. Not enough funds."

myBalan = BankAccout("Matsunaga",12345)
print "Acount name:",myBalan.name
print "Acount number: ",myBalan.number
print myBalan.disBalance()

myBalan.save(30.2)
myBalan.draw(50.3)
myBalan.draw(5)
