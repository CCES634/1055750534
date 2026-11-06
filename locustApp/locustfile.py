from locust import HttpUser, task

@task
class Homero(self):
	def Homero(self):
		self.client.get("/1")
