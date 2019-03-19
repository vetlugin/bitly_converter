# Обрезка ссылок с помощью Битли

Скрипт позволяет конвертировать длинные ссылки в короткие. А также подсчитывать количество кликов на созданные короткие ссылки.

### Как установить

[TODO: объясните пользователю, откуда брать ключи, куда их класть и как они выглядят]
Для работы скрипта необходим активный аккаунт на сайте создания коротких ссылок bit.ly
После чего необходимо получить токен для авторизации скрипта на сервере.
Токен прописывается в файле `.env` например,таким образом:
```
TOKEN=796ecf344015854e6846e24fa67a4051cc9ab9
```
Файл .env лежит в той же папке что и скрипт.

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как работает скрипт

Скрипт запускается в терминале с длинной ссылкой в качестве аргумента.
```
python bitly_converter.py ya.ru
http://bit.ly/2Xis04W
```
Если в качестве аргумента будет подставлена ранее созданная короткая ссылка, скрипт выдаст количество кликов по ней.
```
python bitly_converter.py http://bit.ly/2Xis04W
13
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
