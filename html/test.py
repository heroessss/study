from prettytable import PrettyTable
import  pickle
from colorama import Fore, Back, Style
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
{"name": "美女1", "price": 998},
{"name": "美女2", "price": 98},
{"name": "美女3", "price": 4998},
{"name": "美女4", "price": 3998},
{"name": "美女5", "price": 2998},
{"name": "美女6", "price": 1998},
]
user_login=True
with open("yanzheng.pkl","rb") as f:
    Userlist=pickle.load(f)

print(Userlist)
class Customer():
    def __init__(self,name,pwd,money,lists):
        self.name=name
        self.pwd=pwd
        self.money=money
        self.lists=lists
    def __str__(self):
        return  self.name
def get_form():
    table = PrettyTable(["编号", "name", "price"])
    for i in range(goods.__len__()):
        table.add_row([i, goods[i]["name"], goods[i]["price"]])
    table.add_row(["", "", ""])
    table.add_row(['',"",Fore.RED +"退出"])

    print(table)
    print(Style.RESET_ALL)
    print("-------------------------------------------------------------")

def get_my_form(lists,money):
    table = PrettyTable(["编号", "name", "price"])
    for i in range(lists.__len__()):
        table.add_row([i, goods[i]["name"], goods[i]["price"]])
    table.add_row(["","",""])
    print(table)
    print('剩余余额             '+Fore.RED +str(money))
    print(Style.RESET_ALL)

    print("-------------------------------------------------------------")
name = input("输入用户名")
pwd = input("输入用密码")
for i in Userlist:
    if name == i.get("name"):
        while True:
            if pwd==i["pwd"]:
                user = Customer(name,i["pwd"], i["money"],i["lists"])
                user_login = False
                break
            else:
                pwd = input("密码错误,重新输入用密码")
if user_login:
    while True:
        try:
            money = int(input("输入工资"))
            break
        except:
            print("请输入数字")
    user=Customer(name,pwd,money,[])
    print("欢迎新用户")
while True:
    get_form()
    shop = input("请输入购买商品的编号")
    if shop == "退出":
        get_my_form(user.lists,user.money)
        Userlist.append(user.__dict__)
        with open("yanzheng.pkl", "wb") as f:
            pickle.dump(Userlist, f)
        break
    elif shop not in user.lists:
        if int(user.money) >= goods[int(shop)]["price"]:
            user.money = user.money - goods[int(shop)]["price"]
            user.lists.append(shop)
            print("购买完成，请选择其他商品.剩余余额为:     " + Fore.RED +str(user.money))
        else:
            print("余额不足 请重新选择")
    else:

        print("商品已购买，请选择其他  ")

