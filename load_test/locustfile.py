from locust import HttpUser, task, between


class LoadTest(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def index(self):
        self.client.get("/")

    @task(3)
    def post_data(self):
        self.client.post(
            "/submit", 
            json={"key": "value"}, 
            headers={"Content-Type": "application/json"}
        )

    @task(2)
    def get_metrics(self):
        self.client.get("/metrics")
