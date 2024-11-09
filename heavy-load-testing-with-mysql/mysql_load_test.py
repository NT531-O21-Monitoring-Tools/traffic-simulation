from locust import HttpUser, task, between
import random

class MySQLUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def read_query(self):
        query_id = random.randint(1, 100)  # Adjust based on your dataset size
        self.client.get(f"/read/{query_id}")  # Replace with your read query endpoint

    @task
    def write_query(self):
        payload = {"data": "sample data"}
        self.client.post("/write", json=payload)  # Replace with your write query endpoint