# Traffic simulation

This repository contains three comprehensive scenarios for load testing, monitoring, and performance analysis of applications running on Kubernetes (K8s) with HA Proxy, Locust, and additional monitoring tools.

## Setup
1. Create a virtual environment
```bash
# Install virtualenv if you don't have it already
pip install virtualenv

# Create virtualenv
virtualenv venv

# Activate the virtual environment
# On macOS & Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```
2. Install Locust
```bash
pip3 install locust
```

## 1. Load Balancing Evaluation with HA Proxy

### Overview
This scenario focuses on measuring the performance of the system as HA Proxy distributes load to pods within a Kubernetes cluster.

### Steps
- **Run Locust**: Simulate a large number of virtual users sending requests to the application through HA Proxy.
- **Monitoring**: Use Prometheus and Icinga to monitor traffic through HA Proxy.
- **Log Collection**: Utilize Loki to collect logs from HA Proxy and the application pods to identify any errors during high load conditions.

### Running the Tests
```bash
locust -f load_test.py --host=http://your-haproxy-host
```

### Metrics to Evaluate
- **Requests per second**: Measure the number of requests handled by HA Proxy.
- **Load Distribution Performance**: Assess if the load is evenly distributed among the pods.
- **System Latency**: Monitor latency as the number of requests increases.

## 2. Heavy Load Testing with MySQL

### Overview
In this scenario, we create a substantial dataset to test MySQL's processing capabilities under high load conditions.

### Steps
- **Locust Scripting**: Develop a Locust script to simulate multiple concurrent users sending read/write queries to MySQL.
- **Gradual Load Increase**: Run Locust while gradually increasing the number of virtual users from a low to a high number.

### Running the Tests
```bash
locust -f mysql_load_test.py --host=http://your-app-host
```

### Metrics to Evaluate
- **Average Response Time**: Track the average response time of the application as the user count increases.
- **MySQL Queries per Second**: Measure the number of MySQL queries processed per second.
- **Latency and Resource Utilization**: Monitor MySQL's latency and resource usage under heavy load.

## 3. Performance Evaluation with Docker and Harbor

### Overview
This scenario evaluates the performance of the system while deploying Docker images to Kubernetes through Harbor.

### Steps
- **Build Docker Image**: Create a Docker image for the application and push it to Harbor.
- **K8s Deployment Configuration**: Prepare configuration files for deploying the application to Kubernetes.
- **Scaling and Deployment Testing**: Increase the number of replicas and monitor the time taken to deploy images from Harbor to Kubernetes.

### Running the Tests
```bash
docker build -t your-harbor-repo/your-app:latest .
docker push your-harbor-repo/your-app:latest
```
```bash
kubectl apply -f deployment.yaml
````

### Metrics to Evaluate
- **Image Retrieval and Deployment Time**: Measure the time taken to fetch and deploy the Docker image from Harbor.
- **Kubernetes Resource Usage**: Monitor CPU and RAM utilization in Kubernetes during the deployment process.
- **Log Analysis**: Analyze logs to detect and address any deployment errors.

## Conclusion

This repository provides a comprehensive framework for load testing, monitoring, and performance evaluation. Each scenario is designed to give insights into the system's behavior under various load conditions, helping to ensure a robust and efficient application deployment in a Kubernetes environment.


