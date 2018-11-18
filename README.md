# RaspbyHomebot

## Описание проекта

Бот - домашний помощник. Следит за показателями датчиков в квартире и передаёт их значения хозяевам по запросу в телеграм-чате.

Проект будет масштабироваться по мере расширения инфраструктуры. В настоящий момент это всего лишь **Raspberry Pi 3B+** и простейший датчик температуры и влажности **dht11**. В планах есть постепенное наращивание количества датчиков, приобритение нескольких ардуин (по одной на каждую комнату), которые будут управлять датчиками и отправлять готовую информацию на "малину", которая, в свою очередь, будет обрабатывать её, служа "процессором" для "умного" дома.

Проект создётся исключительно для домашнего использования. Некоторые решения выглядят сомнительно (на самом деле, большинство из них разрешится с переходом на вебхуки, но это позже) и откровенно топорно, но пока главная цель - рабочий прототип.

В проекте используются библиотеки **requests** и **Adafruit_DHT**:

```
sudo pip3 install requests
sudo pip3 install Adafruit_DHT
```

## Основные положения

- Бот отправляет сообщения только тем пользователям, идентификаторы которых присутствуют в ```conf.dictionary["authorized users"]```, на остальных любопытных реагирует холодно, высокомерно заявляя, что они "даже НЕ ГРАЖДАНИН!" (https://www.youtube.com/watch?v=UOkpO--XtH0)

- Бот запрашивает обновления (пока решение "в лоб" - /getUpdates; в процессе расширения инфраструктуры будет сделано через **WebHooks**), после установленного таймаута начинает рассылку сообщений из очереди. Сообщения отправляются **последовательно**

- Бот может изменять периодичность обращения за обновлениями, установив "ночной" режим. Также "ночной" режим можно выключить. Но в таком случае бот проснётся только по истечении установленного таймаута - режим сна нужно соблюдать. Ха-ха.

- Список доступных команд:
    
      /get_temperature - получить показатели температуры в градусах по Цельсию
      
      /get_humidity - получить показатели влажности
      
      /get_current_report - получить все показатели
      
      /enable_night_mode - установить "ночной" режим
      
      /disable_night_mode - выключить "ночной" режим
    
- На остальные запросы будет отвечать недоумением

## Ближайшие планы

- Сделать так, чтобы бот сам отправлял предупреждающее сообщение, если показатели выходят за пределы указанной нормы

- Добавить логирование

- Добавить клавиатуру (красивые кнопки в телеграм-чате с ботом)

- Добавить (пока) цитату запроса

- Добавить отправку сообщения об ошибках

## Вдаль уплывающие планы

- Расширение фермы: больше датчиков, больше устройств контроля, организация беспроводной связи между устройствами

- Вебхуки, поднять vps и т.д.
