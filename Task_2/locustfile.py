from locust import HttpUser, task

class WebsiteUser(HttpUser):
    @task
    def get_integral(self):
        self.client.get("/integrate/0/3.14159")
