from django.shortcuts import render, get_object_or_404


class Default(object):
	"""This operation model is the operation that gets executed if the default execution fails"""
	def __init__(self, request, operation):
		self.request = request
		self.operation = operation
		self.connector = self.operation.connector
		self.message = "Something went wrong while trying to execute the operation in demand, you may proceed to the next stage of the test"
		try:
			self.next = self.operation.get_next_by_updated()
		except:
			self.next = None

	def execute(self):
		context = {
		"instance":self.connector.connected_from.algorithm,
		"connector":self.connector,
		"operation":self.operation,
		"message":self.message
		}
		if self.next:
			context["next_operation_id"] = self.next.id
		return render(self.request, 'test_kit/connector.html', context)

class SaySomething(Default):
	def __init__(self, request, operation, **params):
		Default.__init__(self, request, operation)
		self.message = params["message"]


class PrintSomething(Default):
	def __init__(self, request, operation, **params):
		Default.__init__(self, request, operation)
		self.message = params["message"]

EXECUTION_CHOICES = (
	#Each operation definition should be registered here in this manner else it will not be part of what users can select as operation when designing algorithm
	("SaySomething", "saysomething"), 
	("PrintSomething", "printsomething")
	)

EXECUTION_DEFINITIONS = {
	#Each operation definition should be registered here in this manner else it will not be part of what will get executed
	"SaySomething":SaySomething,
	"PrintSomething":PrintSomething,
	"Default":Default
}