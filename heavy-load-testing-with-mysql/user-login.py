from locust import HttpUser, task, between, SequentialTaskSet
import random
import json

class StudentTasks(SequentialTaskSet):
    @task(1)
    def get_all_students(self):
        self.client.get("/student/getAll")

    @task(2)
    def get_student_by_id(self):
        student_id = random.randint(1, 1000)  # Random ID, điều chỉnh theo dữ liệu thực tế
        self.client.get(f"/student/{student_id}")

    @task(3)
    def add_student(self):
        student_data = {
            "id": random.randint(1000, 9999),
            "fullName": "Student " + str(random.randint(1000, 9999)),
            "yearOfBirth": random.randint(1990, 2005),
            "course": "Course " + str(random.randint(1, 5)),
            "classCode": "Class " + str(random.randint(1, 5)),
            "phoneNumber": "098" + str(random.randint(10000000, 99999999)),
            "email": "student" + str(random.randint(1, 1000)) + "@example.com"
        }
        self.client.post("/student/add", json=student_data)

    @task(4)
    def update_student(self):
        student_id = random.randint(1, 1000)  # Random ID
        student_data = {
            "id": student_id,
            "fullName": "Updated Student " + str(student_id),
            "yearOfBirth": random.randint(1990, 2005),
            "course": "Course " + str(random.randint(1, 5)),
            "classCode": "Class " + str(random.randint(1, 5)),
            "phoneNumber": "098" + str(random.randint(10000000, 99999999)),
            "email": "updatedstudent" + str(student_id) + "@example.com"
        }
        self.client.put(f"/student/{student_id}", json=student_data)

    @task(5)
    def delete_student(self):
        student_id = random.randint(1, 1000)  # Random ID
        self.client.delete(f"/student/{student_id}")

class LecturerTasks(SequentialTaskSet):
    @task(1)
    def get_all_lecturers(self):
        self.client.get("/lecturer/getAll")

    @task(2)
    def get_lecturer_by_id(self):
        lecturer_id = random.choice(['L001', 'L002', 'L003', 'L004'])  # Random lecturer ID
        self.client.get(f"/lecturer/{lecturer_id}")

    @task(3)
    def add_lecturer(self):
        lecturer_data = {
            "id": "L" + str(random.randint(100, 999)),
            "fullName": "Lecturer " + str(random.randint(1000, 9999)),
            "degree": "PhD",
            "classCode": "Class " + str(random.randint(1, 5)),
            "email": "lecturer" + str(random.randint(1, 1000)) + "@example.com",
            "phoneNumber": "098" + str(random.randint(10000000, 99999999))
        }
        self.client.post("/lecturer/add", json=lecturer_data)

    @task(4)
    def update_lecturer(self):
        lecturer_id = random.choice(['L001', 'L002', 'L003', 'L004'])  # Random lecturer ID
        lecturer_data = {
            "id": lecturer_id,
            "fullName": "Updated Lecturer " + lecturer_id,
            "degree": "PhD",
            "classCode": "Class " + str(random.randint(1, 5)),
            "email": "updatedlecturer" + str(random.randint(1, 1000)) + "@example.com",
            "phoneNumber": "098" + str(random.randint(10000000, 99999999))
        }
        self.client.put(f"/lecturer/{lecturer_id}", json=lecturer_data)

    @task(5)
    def delete_lecturer(self):
        lecturer_id = random.choice(['L001', 'L002', 'L003', 'L004'])  # Random lecturer ID
        self.client.delete(f"/lecturer/{lecturer_id}")

class ClassTasks(SequentialTaskSet):
    @task(1)
    def get_all_classes(self):
        self.client.get("/class/getAll")

    @task(2)
    def add_class(self):
        class_data = {
            "classCode": "Class" + str(random.randint(1, 5)),
            "className": "Class Name " + str(random.randint(1, 5)),
            "lecturerId": "L" + str(random.randint(1, 5)),
            "lecturerFullName": "Lecturer " + str(random.randint(1, 5)),
            "numberOfStudents": random.randint(10, 50)
        }
        self.client.post("/class/add", json=class_data)

    @task(3)
    def update_class(self):
        class_code = "Class" + str(random.randint(1, 5))
        class_data = {
            "classCode": class_code,
            "className": "Updated Class Name " + class_code,
            "lecturerId": "L" + str(random.randint(1, 5)),
            "lecturerFullName": "Updated Lecturer " + str(random.randint(1, 5)),
            "numberOfStudents": random.randint(10, 50)
        }
        self.client.put(f"/class/{class_code}", json=class_data)

    @task(4)
    def delete_class(self):
        class_code = "Class" + str(random.randint(1, 5))
        self.client.delete(f"/class/{class_code}")

class LoadTest(HttpUser):
    wait_time = between(1, 5)
    tasks = [StudentTasks]