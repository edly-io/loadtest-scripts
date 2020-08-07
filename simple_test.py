from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(3, 6)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def view_contactus(self):
        self.client.get("/contact/")
