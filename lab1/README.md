# Отчет по Лабораторной работе №1 (обычная)

## Задача

### Настроить nginx по заданному тз:
- Должен работать по https c сертификатом
- Настроить принудительное перенаправление HTTP-запросов (порт 80) на HTTPS (порт 443) для обеспечения безопасного соединения.
- Использовать alias для создания псевдонимов путей к файлам или каталогам на сервере.
- Настроить виртуальные хосты для обслуживания нескольких доменных имен на одном сервере.
- Что угодно еще под требования проекта


### Установка и настройка основного конфига nginx

#### Установил nginx через браузер и вставил стандартный конфиг в nginx/conf/nginx.conf :
```nginx configuration
events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    server_names_hash_bucket_size 64;

    include sites-enabled/*.conf;
}
```
### Пет-проекты для лабораторной
##### var/www/myprojectcat-test9810821.com/html/index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>CAT</title>
</head>
<body>
    <h1>Hello from Site 1!</h1>
    <p>This is a simple pet project.</p>
</body>
</html>
```

##### var/www/myprojectdog-test9810821.com/html/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>DOG</title>
</head>
<body>
    <h1>Hello from Site 2!</h1>
    <p>This is a simple pet project.</p>
</body>
</html>
```
#### команды для создания SSL сертификатов для обеих сайтов:

```commandline
sudo openssl reg -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout myprojectcat-test9810821.com.key \
-out myprojectcat-test9810821.com.crt
```

```commandline
sudo openssl reg -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout myprojectdog-test9810821.com.key \
-out myprojectdog-test9810821.com.crt
```

#### После ввода команд появились ключи и сертификаты в etc/nginx/ssl/

### Затем были созданы отдельные конфиги для сайтов в nginx/conf/sites-enabled/

#### для myprojectdog-test9810821.com

```nginx configuration
server {
    listen 80;
    server_name myprojectdog-test9810821.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name myprojectdog-test9810821.com;

    ssl_certificate C:/Users/Colorful/PycharmProjects/Clouds/lab1/etc/nginx/ssl/myprojectdog-test9810821.com.crt;
    ssl_certificate_key C:/Users/Colorful/PycharmProjects/Clouds/lab1/etc/nginx/ssl/myprojectdog-test9810821.com.key;

    root C:/Users/Colorful/PycharmProjects/Clouds/lab1/var/www/myprojectdog-test9810821.com/html;
    index index.html;

    location /static/ {
        alias C:/Users/Colorful/PycharmProjects/Clouds/lab1/var/www/myprojectdog-test9810821.com/assets/;
    }
}
```

#### для myprojectcat-test9810821.com

```nginx configuration
server {
    listen 80;
    server_name myprojectcat-test9810821.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name myprojectcat-test9810821.com;

    ssl_certificate C:/Users/Colorful/PycharmProjects/Clouds/lab1/etc/nginx/ssl/myprojectcat-test9810821.com.crt;
    ssl_certificate_key C:/Users/Colorful/PycharmProjects/Clouds/lab1/etc/nginx/ssl/myprojectcat-test9810821.com.key;

    root C:/Users/Colorful/PycharmProjects/Clouds/lab1/var/www/myprojectcat-test9810821.com/html;
    index index.html;

    location /static/ {
        alias C:/Users/Colorful/PycharmProjects/Clouds/lab1/var/www/myprojectcat-test9810821.com/assets/;
    }
}
```

<img width="1750" height="663" alt="Снимок экрана 2025-09-09 100923" src="https://github.com/user-attachments/assets/97db1417-076d-407b-b40e-5b5ce33dfc1c" />


#### Браузер ругается на самоподписанный сертификат, потому что он не подписан доверенным центром сертификации , который входит в предустановленный список доверенных организаций в браузере.

<img width="2491" height="865" alt="image" src="https://github.com/user-attachments/assets/73cfbffc-058b-4982-9545-db700c765384" />

<img width="2484" height="389" alt="image" src="https://github.com/user-attachments/assets/4438d4f2-8576-4d23-a6ff-b4e8fde647d2" />

#### Делаем исключение для нашего сайта и он теперь работает!

#### Так же "что угодно еще под требования проекта" можно добавить кастомные страницы для ошибок с помощью

```nginx configuration
error_page 404 /404.html;
```

## Ошибки, с которыми я столкнулся:
### Первая проблема была в том, что я выбрал для доменов своих сайтов dog.com и cat.com ну тут очевидно, что домены заняты..

### Вторая проблема была в том, что затем я названия сделал слишком длинными и выскакивала ошибка:

### could not build server_names_hash, *you should increase server_names_hash_bucket_size: 32

### здесь я просто увеличил размер до 64

### Третья проблема была в том, что я запускал nginx через nginx.exe и при повторных запусках предыдущие процессы не останавливались и получалось так что я долго не мог исправить ошибки в conf файлах т.к. nginx работал со старыми данными

# Итоги:
## Появились базовые знания о nginx
