from locust import HttpUser, task


class AppstoreCore(HttpUser):
    @task
    def landing_page(self):
        self.client.get("/trabalho-qualidade-testes")

    @task
    def menu(self):
        self.client.get("/trabalho-qualidade-testes/view/menu/menu.html")
