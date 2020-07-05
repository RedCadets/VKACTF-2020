## Голос из космоса

| Событие | Название | Категория | Стоимость |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | Голоса из космоса | Стеганография  | КМБ |


### Описание
> Автор: WaffeSoul
> Несколько лет назад наши военные ученые отправили дружественный сигнал в космос. И сегодня мы получили ответ, вот только кроме белого шума там ничего обнаружить не удалось. Однако один наш сотрудник уверен, что слышит голос через помехи....

### Решение 

1. Открыть в Audition, как raw data (file/import/raw data). С настройками:
```Sample Rate: 22050 HZ
Channels: 2 
Format: Raw Data
Encoding: 16-bit PCM
Byte Order: Default Byte Order 
```
2. Видно, что первый канал содержит структуру. Прослушав, понимаем, что это голос наоборот. Реверсим его в audition(Effects/Revers).

3. Прослушав, получаем такой текст и в конце флаг. 
```Voice in a galaxy far, far away...

It is a period of civil war. Rebel
spaceships, striking from a hidden
base, have won their first victory
against the evil Galactic Empire.

During the battle, Rebel spies managed
to steal secret plans to the Empire's
ultimate weapon, the Death Star, an
armored space station with enough
power to destroy an entire planet.

Pursued by the Empire's sinister agents,
Princess Leia races home aboard her
starship, custodian of the stolen plans
that can save her people and restore
freedom to the galaxy.... 
Flag is vka{reverse_is_not_only_in_binaries}
```

**Флаг:**

>vka{reverse_is_not_only_in_binaries}
