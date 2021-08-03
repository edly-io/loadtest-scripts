from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
    wait_time = between(3, 6)
    
    @task(1)
    def index_page(self):
        self.client.get("/")

    @task(1)
    def view_contactus(self):
        self.client.get("/contact/")

    @task(3)
    def view_courses(self):
        self.client.get("/courses/")    

    @task(1)
    def view_programs(self):
        self.client.get("/programs/")  

    @task(1)
    def view_subscriptions(self):
        self.client.get("/subscriptions/")    

    @task(1)
    def view_blogs(self):
        self.client.get("/blogs/")  

    @task(1)
    def view_instructors(self):
        self.client.get("/instructors/") 

    @task(1)
    def view_aboutus(self):
        self.client.get("/about-us/")   

    @task(1)
    def view_courses_detail(self):
        self.client.get("/course/sprint-82-course/")      
