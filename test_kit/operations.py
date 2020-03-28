


class SaySomething():
	def __init__(self, text):
		self.text = text
		self.execute()

	def execute(self):
		return self.text

class PrintSomething():
	def __init__(self, text):
		self.text = text
		self.execute()
		
	def execute(self):
		return self.text


EXECUTION_CHOICES = (
	("SaySomething", "saysomething"), 
	("PrintSomething", "printsomething")
	)