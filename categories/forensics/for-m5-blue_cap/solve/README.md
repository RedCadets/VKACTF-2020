## Странное соединение 

| Событие | Название | Категория | Стоимость |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | Несанкционированный доступ | Форенсика  | 1-3 курс |


### Описание
> Автор: WaffeSoul
> Наша система обнаружила несанкционированный доступ к одному из секретных объектов. Контакт продлился недолго, но мы так и не смогли выяснить его природу. Зато трафик записали.

### Решение 

Дан файл task.pcapng, открываем в wireshake видем протокол L2CAP. Это протокол соединения bluetooth. Выясняем, что подключали клавиатуру. 
Ищем в интеренете находим только решения с USВ.

>https://github.com/TeamRocketIst/ctf-usb-keyboard-parser

Пробуем вытащить payload, через tshark 

>tshark -r task.pcapng -Y 'btl2cap && btl2cap.length == 10' -T fields -e btl2cap.payload | sed 's/../:&/g' | sed 's/^://'
>a1:01:00:00:19:00:00:00:00:00

в USB payload выглядит 

>00:00:24:00:00:00:00:00

Символ в usb храниться в 3 байте, а bluetooth в 5 байте. Поэтому редоктируем код из гида и получаем код exploit.py.
используем его и получаем
>tshark -r task.pcapng -Y 'btl2cap && btl2cap.length == 10' -T fields -e btl2cap.payload | sed 's/../:&/g' | sed 's/^://' \ > datablue
> python3 exploit.py datablue  

**Флаг:**

>vka{k3yb0ard?_blu3t00th_or_USB}
