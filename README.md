# Реальный опыт | Дипломный проект: реальный кейс от компании «Силант»

## _Запуск проекта локально_

### Backend:
- Требование для Backendа Python=3.11
- Заходим в папку Backend и в консоле наберем команду ниже:
    ```sh
    py -m venv venv
    venv\scripts\activate
    pip install -r requirements.txt
    cd App
    ```
- Создайте .env файл внутрь папки App и напишите SECRET_KEY = ' API_KEY ' - ключ сгенерированный джанго
- после наберите в консоль:
    ```sh
    py manage.py runserver
    ```
- Вся документация по API находятся по адресам:
    ```
    http://127.0.0.1:8000/redoc
    http://127.0.0.1:8000/swagger
    http://127.0.0.1:8000/swagger.json
    http://127.0.0.1:8000/swagger.yaml
    ```
- Backend Сервер запустили.

### Frontend:

- Откройте новый консоль и переходите в папку Frontend/app и наберите:
    ```sh
    npm i
    npm start
    ```
- Откройте новую вкладку в браузере и наберите:
    ```sh
    http://localhost:3000
    ```
