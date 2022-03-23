class User():
    def __init__(self,nama,umur,gender):
        self.nama = nama
        self.umur = umur
        self.gender = gender
    def ShowInfo(self):
        print(self.nama)
        print(self.umur)
        print(self.gender)
class Bank(User):
    def __init__(self,nama,umur,gender):
        super().__init__(nama,umur,gender)
        self.balance = 0
    def deposit(self,amount):
        self.balance = self.balance + amount
        print('account balance has been update=', self.balance)
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print('account balance has been update=', self.balance)
        else:
            print('you cant withdraw')
    def view_balance(self):
        self.ShowInfo()
        print('account balance has been update=', self.balance)
        
nama = input('Masukan usernama=')
umur = input('Masukan umur=')
gender = input('Masukan gender=')
user = Bank(nama,umur,gender)

while True:
    options = int(input('1. details\n2. deposit\n3. withdraw\n4. view balance\n5. Exit\n'))
    if options == 1:
        user.ShowInfo()
    elif options == 2:
        dep = int(input('Masukan jumlah deposit='))
        user.deposit(dep)
    elif options == 3:
        draw = int(input('Masukan jumlah withdraw='))
        user.withdraw(draw)
    elif options ==4:
        user.view_balance()
    elif options ==5:
        print('exit')
        break
