from locust import HttpUser, task

class WebsiteUser(HttpUser):
    @task
    def get_integral(self):
        self.client.get("/api/integrate?lower=0&upper=3.14159")
