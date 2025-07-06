# Middle Level ATM System Simulation
# Skills practiced: Control Structures, Function Definition, User Input & Output, File I/O, Class Definition, Data Persistence

import json
import os
from account import ATMAccount

DATA_FILE = os.path.join("atm_system", "users.json")

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f: # 载入用户数据
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def login(users):
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]['password'] == password: 
        print(f" Welcome back, {username}!")
        return ATMAccount(username, users[username])
    else:
        print("Invalid credentials.")
        return None
# users: 是从DATA_FILE文件中加载出来的用户数据，是总用户字典，储存所有用户资料    
# users[username]: 用户字典，储存单个用户完整资料 
# users[username]['password']: 这个用户的密码字符串
# ATMAccount("alice", {"password": "1234", "balance": 500, "history": []})
# self.username = "alice"
# self.password = "1234"
# self.balance = 500
# self.history = []

def register(users):
    username = input("New username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Set password: ")
    users[username] = {"password": password, "balance": 0, "history": []}
    print(f"Account created for {username}")
    save_users(users)

def main():
    users = load_users()

    print("Welcome to ATM system")
    while True:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            account = login(users)
            if account:
                atm_session(account, users)
        elif choice == "2":
            register(users)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")
# if account: 检查 login() 有没有成功登录，如果 account 是一个对象（不是 None），表示登录成功
# atm_session(account, users)：如果登录成功，就开始一个新的 ATM 会话，把当前登录的账号对象 account 和全部用户资料 users 一起传进去 

def atm_session(account, users):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Logout")
        choice = input("Choose: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Balance: ${account.check_balance()}")
        elif choice == "4":
            print("Transaction History: ")
            for h in account.get_history():
                print(" -", h)
        elif choice == "5":
            users[account.username] = account.to_dict()
            save_users(users)
            print("Logged out.")
            break
        else:
            print("Invalid option.")

# atm_session() 和 ATMAccount 不能直接合并，因为关乎职责分离。
# ATMAccount 类：“账户对象/数据”的代码。管理每个账户自己的数据与行为（如存款、取款、历史）。写在类内部
# atm_session()：“用户界面/流程控制”的代码。提供 ATM 菜单 + 控制用户操作流程（如输入选项、循环）。写在类外，属于主程序流程

if __name__ == "__main__":
    main()