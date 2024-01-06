import requests


class HunterAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.hunter.io/v2/"
        self.results = {}  # Локальное хранилище результатов

    def verify_email(self, email):
        """
        Проверка и верификация е-mail адреса.
        """
        endpoint = f"email-verifier?email={email}&api_key={self.api_key}"
        response = requests.get(self.base_url + endpoint)

        if response.status_code == 200:
            data = response.json()
            self.results[email] = data  # Сохранение результатов в локальное хранилище
            return data
        else:
            return {"error": "Ошибка при выполнении запроса"}

    def get_saved_results(self):
        """
        Возвращает сохраненные результаты проверки е-mail адресов.
        """
        return self.results

    # Дополнительные методы CRUD могут быть добавлены по необходимости
