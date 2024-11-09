from locust import HttpUser, task, between

class LoadBalancerUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_test(self):
        self.client.get("/endpoint")  # Replace with application's endpoint