## Военком 

| Событие | Название | Категория | Сложность |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | ЗГТ - Забирай Гадкий Телефон | Форенсика | КМБ |


### Описание
> Автор: WaffeSoul
>Наконец-таки карма настигла и службу ЗГТ! Пришло время ежегодной проверки квалификации ее сотрудников. В этот раз начальник дал необычное задание - дамп памяти, сутки на все про все и никаких дополнительных подробностей.

[MEGA](https://mega.nz/file/bIkg1CYI#6OP_OgOaMXAGJHbFHBU_a4FHywhtbBeP1TOEbm6h9eY)
[Yandex](https://yadi.sk/d/rGJhz7i7ZyQZmQ)
[Google](https://drive.google.com/file/d/1L9BsRnOt8lYOomy1SgnM1J61XLUC6tTD/view?usp=sharing)

Пароль к архиву: `f4a8828c5492840ad8f18ee314396a61`

### Решение 

Дан дамп памяти dump.mem. Сначало узнаем профиль для использования volatility.

>volatility -f dump.mem imageinfo

После смотрим содержание консолей.

>volatility -f dump.mem --profile=Win7SP1x64 consoles

Видем, строчку в которой открывался файл с флагом.
```C:\Users\lost\Desktop>type Flag.txt
https://pastebin.com/KJeeFEV5
```
Переходим по ссылке и видем флаг.

**Флаг:**

>vka{N0t3p4d_ev3rywh3re_1s_34sy}
