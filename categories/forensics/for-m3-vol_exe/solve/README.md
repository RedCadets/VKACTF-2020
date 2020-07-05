## Военком 

| Событие | Название | Категория | Сложность |
|:--------|:---------|:----------|----------:|
| VKA-CTF`2020 | ЗГТ - Забирай Гадкий Телефон [2] | Форенсика | 1-3 курс |


### Описание
> Автор: WaffeSoul
> Сюда сдавать второй флаг задания "ЗГТ - Забирай Гадкий Телефон".

[MEGA](https://mega.nz/file/bIkg1CYI#6OP_OgOaMXAGJHbFHBU_a4FHywhtbBeP1TOEbm6h9eY)
[Yandex](https://yadi.sk/d/rGJhz7i7ZyQZmQ)
[Google](https://drive.google.com/file/d/1L9BsRnOt8lYOomy1SgnM1J61XLUC6tTD/view?usp=sharing)

Пароль к архиву: `f4a8828c5492840ad8f18ee314396a61`

### Решение 

В задании сказано, что на компьютере вирус, поэтому проверяем список процессов 

>volatility -f dump.mem --profile=Win7SP1x64 pstree

``` Name                                                  Pid   PPid   Thds   Hnds Time                                                                                                                                
-------------------------------------------------- ------ ------ ------ ------ ----                                                                                                                                
 0xfffffa8003391060:csrss.exe                         384    372     10    355 2020-05-13 13:37:04 UTC+0000                                                                                                        
 0xfffffa8004e2e6c0:wininit.exe                       428    372      3     82 2020-05-13 13:37:05 UTC+0000                                                                                                        
. 0xfffffa8004ee96c0:lsass.exe                        548    428      6    570 2020-05-13 13:37:07 UTC+0000                                                                                                        
. 0xfffffa8004e83b00:services.exe                     540    428      6    185 2020-05-13 13:37:06 UTC+0000                                                                                                        
.. 0xfffffa80051cc060:spoolsv.exe                    1280    540     13    304 2020-05-13 13:37:23 UTC+0000                                                                                                        
.. 0xfffffa8004f8db00:svchost.exe                     656    540     10    357 2020-05-13 13:37:10 UTC+0000                                                                                                        
... 0xfffffa80023f8710:WmiPrvSE.exe                  1772    656      8    124 2020-05-13 13:41:31 UTC+0000                                                                                                        
.. 0xfffffa800529ab00:taskhost.exe                   1412    540     11    267 2020-05-13 13:37:26 UTC+0000                                                                                                        
.. 0xfffffa80051f3b00:svchost.exe                    1308    540     17    308 2020-05-13 13:37:23 UTC+0000                                                                                                        
.. 0xfffffa8005007b00:svchost.exe                     936    540     20    447 2020-05-13 13:37:15 UTC+0000                                                                                                        
... 0xfffffa80052c9b00:dwm.exe                       1484    936      3     94 2020-05-13 13:37:26 UTC+0000                                                                                                        
.. 0xfffffa8005309b00:svchost.exe                    1584    540      9    184 2020-05-13 13:37:27 UTC+0000                                                                                                        
.. 0xfffffa80050996c0:svchost.exe                     436    540      5    115 2020-05-13 13:37:18 UTC+0000                                                                                                        
... 0xfffffa8004b2f060:csrss.exe                      448    436     11    249 2020-05-13 13:37:05 UTC+0000                                                                                                        
.... 0xfffffa80052bab00:conhost.exe                  2304    448      2     54 2020-05-13 13:38:50 UTC+0000                                                                                                        
.... 0xfffffa8002400b00:conhost.exe                   616    448      2     54 2020-05-13 13:41:25 UTC+0000                                                                                                        
.... 0xfffffa8005046060:conhost.exe                  2344    448      2     54 2020-05-13 13:38:58 UTC+0000                                                                                                        
... 0xfffffa8004e72b00:winlogon.exe                   500    436      3    113 2020-05-13 13:37:05 UTC+0000                                                                                                        
.. 0xfffffa8005018b00:svchost.exe                     968    540     13    293 2020-05-13 13:37:16 UTC+0000                                                                                                        
.. 0xfffffa8004fd0060:VBoxService.ex                  724    540     13    149 2020-05-13 13:37:12 UTC+0000                                                                                                        
.. 0xfffffa80050156c0:svchost.exe                     992    540     31    888 2020-05-13 13:37:16 UTC+0000                                                                                                        
... 0xfffffa800254d7c0:WMIADAP.exe                   2220    992      7     90 2020-05-13 13:41:29 UTC+0000                                                                                                        
.. 0xfffffa8004fe2b00:svchost.exe                     784    540      6    246 2020-05-13 13:37:12 UTC+0000                                                                                                        
.. 0xfffffa8005030060:svchost.exe                     876    540     18    471 2020-05-13 13:37:15 UTC+0000                                                                                                        
... 0xfffffa800508ab00:audiodg.exe                    392    876      4    127 2020-05-13 13:37:18 UTC+0000                                                                                                        
.. 0xfffffa8004f0e570:sppsvc.exe                     2476    540      4    164 2020-05-13 13:39:32 UTC+0000                                                                                                        
.. 0xfffffa800515c6c0:svchost.exe                    1148    540     15    372 2020-05-13 13:37:22 UTC+0000                                                                                                        
. 0xfffffa8004eeeb00:lsm.exe                          568    428     10    144 2020-05-13 13:37:08 UTC+0000                                                                                                        
 0xfffffa8002288040:System                              4      0     99    488 2020-05-13 13:36:59 UTC+0000                                                                                                        
. 0xfffffa8003484b00:smss.exe                         300      4      2     31 2020-05-13 13:36:59 UTC+0000                                                                                                        
 0xfffffa8005364060:explorer.exe                     1700   1472     31    981 2020-05-13 13:37:27 UTC+0000                                                                                                        
. 0xfffffa8002408060:RamCapture64.e                  1224   1700      6     75 2020-05-13 13:41:25 UTC+0000                                                                                                        
. 0xfffffa8005031b00:System.exe                      2336   1700      1      7 2020-05-13 13:38:57 UTC+0000                                                                                                        
. 0xfffffa800551c060:VBoxTray.exe                    1864   1700     15    154 2020-05-13 13:37:32 UTC+0000                                                                                                        
. 0xfffffa8004fcb7d0:TrueCrypt.exe                   2632   1700      9    397 2020-05-13 13:40:01 UTC+0000                                                                                                        
. 0xfffffa80052b6730:cmd.exe                         2296   1700      1     19 2020-05-13 13:38:49 UTC+0000                                                                                                        
```

В процессах можно заметить 2 system, при этом один запущенный от explorer.exe. Дампим его и проверяем.

>volatility -f dump.mem --profile=Win7SP1x64 procdump -p 2336 --dump-dir=.

Простой реверс через ida pro, и получаем флаг

**Флаг:**

>vka{r3v3r53_4nd_f0r3n51c_1n_7h3_5ymb10n7_15_600d}