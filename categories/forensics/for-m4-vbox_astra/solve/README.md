## Военком 

| Событие | Название | Категория | Сложность |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | Странная ОС | Форенсика | 4-5 курс |


### Описание
> Автор: WaffeSoul
> К нам в часть поступили компьютеры с, как было заявлено, абсолютно новой отечественной ОС. С первого взгляда это обычная винда, осталось лишь узнать что у нее под капотом.

[Mega](https://mega.nz/file/CEEGzKwB#Vhh8piy9Cwy60pTE4_tTl9IMa35Wmydn8jRKxUgBjZU)
[Google](https://drive.google.com/file/d/18gBSEQXz6OX85X__Vl4IJ00hYezJcukF/view?usp=sharing)
[Yandex](https://yadi.sk/d/KII053U3fVVolw)

Пароль к архиву: `fdd8e74f888e5d23511736275b957373`

### Решение 

Дан образ диска, запускаем его же virtual box, запускается система windows xp просматриваем его ничего не находим, но картинка рабочего стола это скриншот рабочего стола Astra Linux. Можно заметить, что место занимаемый XP и место занимаемы образом не совпадают. Посмотрев разделы созаданные на образе, можно заметить два не используемых. Скачеваем Grub2Win, ставим его на загрузку системы Debian. Перезапускаем. Загружаемся через Debian, вкл grub и загрузка astra linux. Пытаемся зайти, требует пароль. Перезапускаем, при выборе системы нажимаем 'e' для редактирования загрузке. В строчке с linux в конце добавляем init=/bin/bash. Нажимаем ctl+x. Загружается система через bash, пишем команду:

> cat ect/shadow

Получаем хеш паролей пользователей.

>alfa:$6$uQvXQjbc$Zzjk3tr4KPWtO/jhMsBRSGeujd2jRFZwXli6dGrSQvNGks6UZsoMBgRxzdi3MRQgJpfBzHERof5tWYAcHi48D0:18437:0:99999:7:::
>stiv:$6$709.bLDA$0fx./rjVh4JDKwpc96o8YKyRm1kuS5FnWAt6DOKF5aZov1M88YyLklpLkUH3JGati1yzSNyy02g9zb0Igabx01:18437:0:99999:7:::

Брутим через словарь rocjyou и hashcat.

>hashcat -m 1800 hash rockyou.txt

Получаем комбинацию паролей и пользователей

>alfa:spacebar
>stiv:halowars

Загружаемся через stiv в его папке лежит флаг

**Флаг:**

>vka{W7F?A5tr4_l1nux!?Y0u_cr4zy!}