#Описание

Задание для [Хакатона в Mail.ru](https://park.mail.ru/blog/topic/view/9407/).

Асинхронный сервер на boost::asio, порт задается аргументом командной строки.
Должен по запросу из строки браузера вида: localhost:xxxx/get/file_name вернуть файл
с именем file_name из рабочей директории или ошибку

###Требования

Необходимо наличие Python 3

###Использование

Выполните "async_file_server.py" с аргументом ip:port
Перейдите в браузере по адресу ip:port/get/file_name

###Пример выполнения

```#!bash
python async_file_server.py 127.0.0.1:420
>>>...
>>>...======== Running on http://127.0.0.1:1488 ========
>>>...(Press CTRL+C to quit)
>>>...```