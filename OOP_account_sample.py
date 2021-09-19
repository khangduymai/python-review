#%%
import datetime
import pytz


class Account:
    """Simple account class with __balance"""

    # A static method is shared by all instances of the class (class method)
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(),self.__balance)]
        print("Account was created for ", self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # self._transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
            self.show_balance()
        else:
            print("You don't have enough money to withdraw")
            self.show_balance()

    def show_balance(self):
        print("Your current __balance is {}".format(self.__balance))

    def show_transaction_amount(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawed"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    khang = Account("Khang", 1000)
    khang.show_balance()
    khang.deposit(1000)
    khang.show_balance()
    khang.withdraw(200)
    khang.show_transaction_amount()
    print()
    print()
    steph = Account("Steph", 800)
    steph.__balance = 200
    print()
    steph.deposit(100)
    print()
    steph.withdraw(200)
    print(steph.__dict__)
    print()
    steph.__balance = 400
    steph.show_transaction_amount()
    steph.show_balance()
    print()
    print(steph._current_time())
    print()
    print(steph.__dict__)
# %%
