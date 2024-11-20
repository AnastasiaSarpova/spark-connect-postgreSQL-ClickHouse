# Соединение PySpark с базами PostgreSQL и Clickhouse развернутыми в Docker Compose
## Цель проекта

Проект предназначен для быстрого разворачивания базы данных PostgreSQL и ClickHouse с использованием Docker Compose и Последующим подключением к ним PySpark

## Используемые технологии

- PostgreSQL
- ClckHouse
- Docker Compose
- PySpark

## Установка и запуск

1. Клонируйте репозиторий:
   
   $ git clone https://github.com/AnastasiaSarpova/spark-connect-postgreSQL-ClickHouse.git

2. Перейдите в директорию проекта:
   
   $ cd project_name
   
3. Создайте новый файл с именем .env, скопировав содержимое из .env.example. Это можно сделать через терминал:
```cp .env.example .env```  
или вручную, создав пустой файл .env и вставив туда содержимое .env.example.  
Откройте созданный файл .env в вашем любимом редакторе и замените все значения-заглушки на ваши данные при необходимости. 
   Переменные из файла .env:
   - POSTGRES_USER = postgres
   - POSTGRES_PASSWORD = Пароль пользователя, по умолчанию: 1234qwe
   - CLICKHOUSE_USER = default
   - CLICKHOUSE_PASSWORD = Пароль пользователя, по умолчанию: 1234qwe

4. Запустите контейнеры с помощью Docker Compose с необходимой переменной POSTGRES_PASSWORD:
   
   ```$ docker-compose up --build -d ```  

5. Запустите spark_app.py для загрузки данных с помощью PySpark  
   ![Снимок экрана от 2024-11-20 15-12-46](https://github.com/user-attachments/assets/4921945e-032c-4270-b079-5f190367f405)
