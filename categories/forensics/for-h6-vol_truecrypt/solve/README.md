## Военком 

| Событие | Название | Категория | Стоимость |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | ЗГТ - Забирай Гадкий Телефон [3] | Форенсика |  4-5 курс |


### Описание
> Автор: WaffeSoul
> Сюда сдавать третий флаг задания "ЗГТ - Забирай Гадкий Телефон"

[MEGA](https://mega.nz/file/bIkg1CYI#6OP_OgOaMXAGJHbFHBU_a4FHywhtbBeP1TOEbm6h9eY)
[Yandex](https://yadi.sk/d/rGJhz7i7ZyQZmQ)
[Google](https://drive.google.com/file/d/1L9BsRnOt8lYOomy1SgnM1J61XLUC6tTD/view?usp=sharing)

Пароль к архиву: `f4a8828c5492840ad8f18ee314396a61`

### Решение 

Берем дамп из прошлого задания, используем volatility с плагином pstree

>volatility -f dump.mem --profile=Win7SP1x64 pstree

Можно увидеть запущенные truecrypt и ramdisk. Смотрим возможные пароли к хранилищам.

>volatility -f dump.mem --profile=Win7SP1x64 truecryptpassphrase
 
> Found at 0xfffff880044eaee4 length 14: Strongpassword

Осталось найти только само хранилище. Если погуглить, что такое ramdisk, можно понять, что это программа для создания в локальных дисков в оперативной памяти, дампим эту программу. 

> volatility -f dump.mem --profile=Win7SP1x64 memdump -p 2100 -D .

Открываем получившийся дамп в r-sdutio, сканируем и находим раздел на 500 мб, в котором лежит файл SecretFile.
Открываем "SecretFile" через truecrypt с паролем Strongpassword.
Открываем картинку из хранилищая и видем флаг.

**Флаг:**

>vka{c0n6r47ul4710n5_y0u_p4553d_7h3_7357_p3rf3c7ly}