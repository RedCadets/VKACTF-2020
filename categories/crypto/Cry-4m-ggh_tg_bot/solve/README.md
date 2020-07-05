### Распределитель нарядов

| Событие | Название | Категория | Сложность |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | Распределитель нарядов | Криптография | 1-3 курс |

### Описание
> Автор: iC0nst

> Мой командир написал telegram-бота, распределяющего наши наряды. Но он у нас забывчивый и умом-то не блещет. 
Наряды совершенно неравномерно распределены. Думаю если зайти от имени админа мы сможем доказать это.
Ведь всем известно, что за неравномерное распределение нарядов можно и за решётку сесть.


### Решение
Мы имеем дело с telegram-ботом, с помощью которого некоторая группа лиц узнаёт, когда им идти на дежурство. 

Помимо графического интерфейса (кнопок) с ботом можно взаимодействовать с помощью команд. Список команд можно получить, отправив **/list**. 

Но, введя "/" , меню-подсказка выдаёт на одну команду больше, а именно  команда **/dev** не числится в списке, что достаточно подозрительно. 

Отправив её, мы получаем некоторый файл и ответное сообщение следующего содержания: 
>админ : WzEyMjQ1LCAtNzYzMSwgMTQyODEsIC01MzYzLCAtMzAwMzgsIDI5NjExLCAxNDUyMiwgLTEzNjUzLCAyNzIyNywgOTkxLCAtMTgwOCwgMTI4NTdd
>ряд. Иванов : WzU0OTUsIC0zNDU1LCA2MDEyLCAtMTAzODMsIC0xMjY4MSwgMTMzODIsIDQ3MjAsIC02NjkwLCA3NjMyLCA1NTcsIC0zMTc4LCA0MDQwXQ==
>ряд. Смирнов : WzU0ODcsIC0zNDY4LCA2MDA4LCAtMTAzODAsIC0xMjY5NCwgMTMzNzQsIDQ3MjQsIC02NjkwLCA3NjEyLCA1NDcsIC0zMTg2LCA0MDI4XQ==
>ряд. Дмириев : WzMwMzAxLCA0MzksIDEwMDQ2LCAtMzQxMCwgLTE4MzAyLCAyNjg2OSwgNjc5NSwgLTM5NTYsIDU1NTgsIC0zNTUsIC0zMzAxLCAxMTg5MF0=
>ряд. Агаев : WzEzMDE3LCAtNDA2MCwgMTA1NjYsIC0yMjYyOSwgLTI0MzgzLCAzMTA4OSwgMTU0MTQsIC0xNTg0OSwgMjE3MTIsIC00MDQxLCAtNTQ1NywgMTUzMThd
>ряд. Григорьев : Wy0xNzQ3LCAtNzczOCwgMjM2NjYsIC0yNjY0NiwgLTMzNDQ3LCAzNTI3MywgMTQ0MjYsIC0xMjcwMiwgMzIwNzAsIDEzNjczLCAyNTY2LCAtMzc2OF0=
>ряд. Львов : WzEwNzQwLCAzNTQ0LCAxNzAzNywgLTE4ODIxLCAtMTMyMzQsIDI2MjY2LCA2NjYsIC05ODYsIDczNiwgLTExMzYsIC0xNTAwLCAxMDIxXQ==

Очевидно, что в правой части каждой пары строка, закодированная с помощью base64.

Для *админа* строка в правой части имеет следующий вид:
>[12245, -7631, 14281, -5363, -30038, 29611, 14522, -13653, 27227, 991, -1808, 12857]

Также нам отправлен файл с названием *ggh_public_key*, в котором матрица чисел 12x12. Исходя из названия файла, можно сделать вывод о том, что мы имеем дело с ggh-шифрованием. 

Данная схема шифрования в качестве секретного ключа использует некоторый "хороший" (ортогональный или близкий к таковому) базис линейного пространства, задаваемый матрицей чисел, и унимодулярную матрицу, а в качестве публичного ключа - произведение этих двух матриц. 
Особенность в том, что, умножив **слева** унимодулярную матрицу на базис, мы получаем новый "плохой" базис, который задаёт **то же самое** линейное пространство. 
Чтобы из нового базиса, который является открытым ключом, получить старый, базис необходимо редуцировать, что является достаточно сложной задачей для линейных пространств размерностей 80 и выше. 
В нашем случае размерность всего 12, а значит, что с этой задачей справится LLL-алгоритм. 

Ниже показано, как это сделать с помощью python.

```python
import numpy as np
import olll      #LLL-алгоритм
import json
from base64 import b64decode
import numpy as np

#Задаём исходные данные ("плохой" базис (открытый ключ), зашифрованное сообщение)

enc_basis =[[1, -39, 7, -62, -60, -18, -51, 15, -63, 49, -8, -50],
            [146, 136, 101, -64, 109, 77, -152, 145, -226, -47, -22, 66],
            [206, -120, -50, 98, -121, -39, 149, -73, 63, 67, -24, 34],
            [-134, -10, -192, 29, 116, -103, 28, -110, 19, -120, -53, 2],
            [-157, -27, 27, -33, 5, 30, -49, -92, 16, 15, -127, -132],
            [-133, -104, 32, -136, -102, 56, 52, -115, 149, 41, -21, -33],
            [-63, -14, -17, -141, -61, -11, 82, -28, 75, -34, 65, 64],
            [141, -63, 78, -69, -103, 49, 70, 5, 29, 133, 3, -43],
            [-83, 139, 93, 148, 120, 143, -19, 49, 57, -49, 64, -104],
            [-48, 4, 117, 32, -31, 53, -137, 18, -33, 7, 19, 79],
            [113, 40, 21, -40, -135, 110, 144, 40, 205, 65, 123, 96],
            [129, -17, -87, 19, -11, -55, -14, -2, -123, -117, -88, 109]]

encrypted_message = json.loads(b64decode("WzEyMjQ1LCAtNzYzMSwgMTQyODEsIC01MzYzLCAtMzAwMzgsIDI5NjExLCAxNDUyMiwgLTEzNjUzLCAyNzIyNywgOTkxLCAtMTgwOCwgMTI4NTdd").decode("utf-8")) #Зашифрованный пароль админа

#__________Атака__________
#Атака на открытый ключ путём проведения редукции базиса с помощью LLL-алгоритма
reduced_enc_basis = np.array(olll.reduction(enc_basis, 0.75))
reduced_enc_basis_inv = np.linalg.inv(reduced_enc_basis)
unimodul_m_2 = np.matmul(enc_basis, reduced_enc_basis_inv)
unimodul_m_2_inv = np.linalg.inv(unimodul_m_2)
intermediate_step = np.around(np.matmul(encrypted_message, reduced_enc_basis_inv))
result = np.around(np.matmul(intermediate_step, unimodul_m_2_inv))
print("Attack result: ",result)
password = ""
for i in result.tolist():
    password +=chr(round(i))
print("Password: ", password)
#Таким образом, открытый ключ потенциально уязвим при малых размерностях

#_____________Дополнительно_____________
#Попытка расшифровать без проведения атаки (Суть стойкости алгоритма GGH)
enc_basis_inv = np.linalg.inv(enc_basis)
pseudo_decrypted_message = np.around(np.matmul(encrypted_message, enc_basis_inv))
print("Pseudo-decrypted message",pseudo_decrypted_message)
```

Таким образом, дешифруем пароль админа, открываем админ-панель и получаем...
>vka{b3_c4r3ful_w17h_d1m3n510n}