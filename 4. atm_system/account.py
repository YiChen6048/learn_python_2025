import datetime

class ATMAccount:
    def __init__(self, username, data):
        self.username = username
        self.password = data['password']
        self.balance = data['balance']
        self.history = data.get('history', [])
# self 代表当前这个对象自己

    def deposit(self, amount):
        self.balance += amount
        self._add_history(f"Deposited ${amount}")
# balance += amount: 出错！因为你没有告诉 Python：要修改哪个对象的 balance   

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self._add_history(f"Withdrew ${amount}")

    def check_balance(self):
        self._add_history("Checked balance")
        return self.balance

    def _add_history(self, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {action}")
# datetime.datetime.now(): 调用类的方法，获取当前时间。datetime 模块的类有：datetime, date, time, timezone...
# .strftime(...): 将时间格式化成你指定的字符串

    def get_history(self):
        return self.history
# get_history() 返回的是一个列表 list，可能长这样：
# [
#   "[2025-07-02 22:30:15] Deposited $100",
#   "[2025-07-02 22:31:10] Withdrew $50",
#   "[2025-07-02 22:32:20] Deposited $200"
# ]
# _add_history()	添加记录（写入）	✅ 会修改
# get_history()	返回记录（只读）	❌ 不修改
    
    def to_dict(self):
        return{
            "password": self.password,
            "balance": self.balance,
            "history": self.history
        }


